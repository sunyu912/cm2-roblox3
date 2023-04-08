import os
import json


def revise_sections_json(sections_file):
    dict = {
        "sections": []
    }

    # Load current sections.json if it exists
    # We could check other keys to see what needs to be added if they do not exist (i.e. "override")
    if os.path.exists(sections_file):
        with open(sections_file) as json_file:
            dict = json.load(json_file)

    files_to_remove = dict["sections"].copy()
    # Append all file names that are no in the sections.json
    for f in sorted(next(os.walk("./"))[1]):
        # Mark files in case we are removing them
        if f in files_to_remove:
            files_to_remove.remove(f)
        if (not "." in f and
                not f in dict["sections"]):
            dict["sections"].append(f)

    # Remove files from json if they no longer exist
    for f in files_to_remove:
        dict["sections"].remove(f)

    # Write the order.json
    with open(sections_file, "w") as f:
        json.dump(dict, f, indent=2)


def revise_order_json(module_dir, order_file):
    dict = {
        "override": False,
        "order": []
    }

    # Load current order.json if it exists
    # We could check other keys to see what needs to be added if they do not exist (i.e. "override")
    if os.path.exists(order_file):
        with open(order_file) as json_file:
            dict = json.load(json_file)

    files_to_remove = dict["order"].copy()
    # Append all file names that are no in the order.json
    for f in sorted(next(os.walk(module_dir))[2]):
        # Mark files in case we are removing them
        if f in files_to_remove:
            files_to_remove.remove(f)
        if not ".json" in f and not f in dict["order"]:
            dict["order"].append(f)

    # Remove files from json if they no longer exist
    for f in files_to_remove:
        dict["order"].remove(f)

    # Write the order.json
    with open(order_file, "w") as f:
        json.dump(dict, f, indent=2)


sections_file = module_dir = os.path.join(".", "sections.json")
revise_sections_json(sections_file)

for dir in sorted(next(os.walk("./"))[1]):
    if not "." in dir:
        module_dir = os.path.join(".", dir)
        order_file = os.path.join(module_dir, "order.json")
        revise_order_json(module_dir, order_file)
