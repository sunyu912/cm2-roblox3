
# Lesson 2: Pathfinding Out A Maze





# Summary and Learning Objective(s):

-   Students will have a more hands-on experience as they witness how obstacles affect the pathfinding calculations.

-   Students will transform the script into a usable tool in-game as a hint system for escaping a maze, this works as a review for past Roblox lessons.

-   This lesson serves as a review where they compile previous lessons into a project. (Tool, Transparency, CanCollide, ClickDetector, Touched event)


# Preparations:

-   If needed there is a Step-By-Step sheet that can be printed for each students to keep and refer back to.


# Class Schedule/Tasks:

## Review Pathfinding

1.  Have a quick review showing the students what was done in Lesson 1.

2.  Remind them what each line in the script does.


## Create a maze

1.  Give students time to create a maze.

2.  Students just need a Part called Finish located in the Workspace.

3.  In the meantime, spend some time yourself to create one that also has varying heights.

    1.  This is a good time to review basic scripts such as:

        1.  Making doors appear/disappear with Transparency and CanCollide

        2.  Creating ClickDetector buttons

        3.  Using Touched event to trigger death when colliding


## Synthesize a Maze Hint Tool

1.  As some students are working, explain that we can transform the visualized pathfinding script into a hint tool that lights a temporary path to the exit.

2.  Let's first start by adding a Tool into the Workspace. We can rename this to HintTool.

    1.  The students can design the tool however they like, however one part and only one part must be named Handle (with a capital H).

    2.  Place the Handle as a child of the HintTool.

    3.  Create a script and place it inside HintTool. We can rename this to HintToolScript.

    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2002/0ec975cc-aa38-42e0-a581-bd1feb7254c9.png)

3.  Open the script and insert the following code:


![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2002/bd9c89c3-7b3c-4357-a8a4-54a2fde7d1c3.png)


Important: If students have the script from lesson 1, make sure to disable the PathfindingScript if you want the HintToolScript to work correctly as it interferes with each other!

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.

2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.