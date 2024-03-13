import os
import urllib.request 
from PIL import Image 
import re
import uuid
import shutil
from google_drive_downloader import GoogleDriveDownloader as gdd

# initialize firebase app
from firebase_admin import credentials, initialize_app, storage
cred = credentials.Certificate("C:/Users/victo/Downloads/cm-image-repository-firebase-adminsdk-9oas6-c597160f42.json")

# get reference to firebase storage
initialize_app(cred, {'storageBucket': 'cm-image-repository.appspot.com'})
bucket = storage.bucket()

'''
This .py file is stored in a folder. There are other folders stored alongside it known as "module" folders.
Each "module" folder contains several markdown files known as "lessons."
Each lesson may contain one or more image elements that display an image via URI. 
We want to scrape these images, but we might get rate limited (receive a 403) if we read too much.
'''

script_directory = os.path.dirname(os.path.abspath(__file__))

# downloads an image. different procedures take place depending on if it is a drive image or a standard image.
def download_image(module_name, lesson_name, image_url, image_uuid):
    # it's already been uploaded
    if "storage.googleapis" in image_url and "cm-image-repository" in image_url:
        print("\t\tSkipped downloading " + image_url + ", already been uploaded")
        return False

    try:
        #if image url is a google drive link (ex: https://drive.google.com/uc?export=download&id=1vURF4juXNr8kIU9widtxEhG4TD08iGxe or https://drive.google.com/uc?export=view&id=1vURF4juXNr8kIU9widtxEhG4TD08iGxe)
        if "drive.google.com" in image_url and ("export=download&id=" in image_url or "export=view&id=" in image_url):
            output_filename = os.path.join(script_directory, "output", module_name, lesson_name, image_uuid + ".png")
            extracted_id = image_url.split("id=")[1]
            gdd.download_file_from_google_drive(file_id=extracted_id, dest_path=output_filename)
            # the library prints out its own confirmation message
        else:
            # make sure the folder location exists (urllib throws an error if it doesn't already exist)
            output_directory = output_filename = os.path.join(script_directory, "output", module_name, lesson_name)
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            output_filename = "output/" + module_name + "/" + lesson_name + "/" + image_uuid + ".png"
            urllib.request.urlretrieve(image_url, output_filename) 
            print(f"\t\tDownloaded: {image_url} -> {output_filename}")
        return True
    except Exception as e:
        print(f"\t\tFailed to download: {image_url} " + str(e))
        return False
    
# uploads an image to firebase storage. returns the public blob url.
def upload_image(curriculum_name, module_name, lesson_name, image_uuid):
    output_filename = os.path.join(script_directory, "output", module_name, lesson_name, image_uuid + ".png")

    # save the downloaded image in firebase storage at path curriculum_name/module_name/lesson_name/UUID
    upload_filename = curriculum_name + "/" + module_name + "/" + lesson_name + "/" + image_uuid + ".png"
    blob = bucket.blob(upload_filename)
    blob.upload_from_filename(output_filename)
    blob.make_public()

    # return the blob's image url
    return blob.public_url

# downloads and transfers an image.
def transfer_image(curriculum_name, module_name, lesson_name, image_url, image_uuid):
    if download_image(module_name, lesson_name, image_url, image_uuid):
        return upload_image(curriculum_name, module_name, lesson_name, image_uuid)
    else:
        return image_url

# preprocesses a lesson, scrapes all images from the lesson, and then reformats the markdown file.
def scrape_lesson(curriculum_name, module_name, lesson_name):
    # Assuming markdown file path is constructed using curriculum, module, and lesson names
    file_path = os.path.join(script_directory, module_name, lesson_name + ".md")
    print("\tScraping lesson " + file_path)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the content of the markdown file
        markdown_content = file.read()

        # remove smart apostrophes
        markdown_content = markdown_content.replace('“', '"')
        markdown_content = markdown_content.replace('”', '"')
        markdown_content = markdown_content.replace('‘', "'")
        markdown_content = markdown_content.replace('’', "'")
        markdown_content = markdown_content.replace('—', "--")
        markdown_content = markdown_content.replace('±', "+=")
        markdown_content = markdown_content.replace('\u2212', "--")
        markdown_content = markdown_content.replace('\u200b', "")
        markdown_content = markdown_content.replace('\ufeff', "")
        markdown_content = markdown_content.replace('\u2303', '')
        markdown_content = markdown_content.replace('\u2713', '')
        markdown_content = markdown_content.replace('\u2318', 'COMMAND')
        markdown_content = markdown_content.replace('\u30fb', '')
        markdown_content = markdown_content.replace('\u0085', '')
        markdown_content = markdown_content.replace('\u2192', '->')
        markdown_content = markdown_content.replace('�', "")
        markdown_content = markdown_content.replace('�', '')
        markdown_content = markdown_content.replace('…', "...")
        markdown_content = markdown_content.replace("é", "e")
        
        # Find all image links using regular expression
        image_links = re.findall(r'!\[.*?\]\((.*?)\)|<img.*?src=["\'](.*?)["\'].*?>', markdown_content)

        image_links = [link[0] if link[0] else link[1] for link in image_links]

        if len(image_links) > 0:
            for image_url in image_links:
                # Generate a UUID for each image
                image_uuid = str(uuid.uuid4())

                # Transfer the image using the transfer_image function
                new_url = transfer_image(curriculum_name, module_name, lesson_name, image_url, image_uuid)

                # Edit the image element in the markdown with the new URL
                markdown_content = markdown_content.replace(image_url, new_url)
        else:
            print("\t\t There are no images present in this lesson.")

    # Save the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(markdown_content)

# scrapes every markdown file present in a module folder.
def scrape_module(curriculum_name, module_name):
    folder_path = os.path.join(script_directory, module_name)
    print("Scraping module " + folder_path)

    # get the names of every markdown file under this module folder
    markdown_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]

    # for each markdown file lesson_name,
    for lesson_name in markdown_files:
        scrape_lesson(curriculum_name, module_name, lesson_name.replace(".md", ""))
    
# determines if a folder is a module or not.
def folder_is_exception(module_name):
    exceptions = ["__pycache__", ".github", ".git", ".idea", "output"]
    for exception in exceptions:
        if exception in module_name:
            return True
    return False

# scrapes all sibling module folders.
def scrape_curriculum(curriculum_name):
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # modules are folders that are not exceptions (such as .github)
    modules = [ f.name for f in os.scandir(script_directory) if f.is_dir() if not folder_is_exception(f.name)]

    # for each module
    for module_name in modules:
        scrape_module(curriculum_name, module_name)

# removes the output directory so that we don't upload way too much data on pushing.
def remove_output_directory():
    output_root = os.path.join(script_directory, "output")
    if os.path.exists(output_root):
        shutil.rmtree(output_root, ignore_errors=True)
        print(f"Removed output directory.")

scrape_curriculum(input("Please enter the curriculum name: "))
remove_output_directory()