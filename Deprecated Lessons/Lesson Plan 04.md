
# Lesson 4: Chasing AI Enemy (Part 1)

  

  

# Summary and Learning Objective(s):

-   Modify the script from a previous lesson to create an enemy AI that chases.
    

# Important Notes:

-   The lessons are written in more detail and hands-on if the students are willing to see the process.
    
-   Otherwise for larger classes and for the sake of time, the Step-By-Step is provided along with a link to the scripts.
    

-   Link: [http://bit.ly/roblox3_4_zombiescript](http://bit.ly/roblox3_4_zombiescript)
    

-   From there, an overview of what has changed between the previous iteration and the current iteration can be applied.
    

# Class Schedule/Tasks:

## Turning the NPC into a Zombie

1.  There isn't a huge difference between a friendly NPC and a Zombie enemy besides dealing damage.
    
2.  Start by duplicating our NPC from Lesson 3 and renaming it to Zombie for clarification.
    
3.  Before we get started on the script, let's make the Zombie look more like a zombie.       
    
    1.  Rename zombie's Humanoid into Zombie. This helps differentiate between friend and enemy.
        
    2.  Rename the NPCMoveScript to ZombieScript for later.
        
    3.  You can recolor each zombie part to look different.
        

5.  Add an IntValue into the Zombie model and name it Damage. This will make it easier for you to change the amount of damage a zombie does instead of finding and opening the script. I set the value to 10.  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/ce3eefba-f111-42a5-a7e6-46c211eef31e.png)
    
6.  Open up ZombieScript and add 3 new variables called torso that will store the UpperTorso part, damage that will store how much damage a zombie will inflict, and detectionRange set to any number.
    
    1.  If you haven't already, also delete the goals variable from the previous NPCScript and set destination to nil.  The current variables should look like below.

    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/089e4310-0283-4e9b-944a-cf331ed7c912.png)

6.  Now let's create a function to connect when the torso is Touched. This is placed just above the Connected events.  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/88f3a825-caef-4ac7-84b3-5498a86c71ee.png)
    
7.  Connect the function to the Touched event.  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/5de0ce38-4a92-4c9f-8de0-06a7735a8751.png)
    

## Finding a Target

1.  Instead of a series of goals, we will find the nearest Humanoid and set it as the target.
    
2.  Let's add a new function right after followPath. This function will be called findNearest.  
      
![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/f8995524-df34-4111-a366-9edd7d992652.png)

3.  To make sure we find a target before calling followPath( ), we will implement a repeat-until loop right at the end.  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/4e82c67e-9c18-4ea0-8572-c2321c759758.png)
    

## Adjusting the Rest

1.  With the new function, we'd need to adjust a few lines from other functions and events.
    
2.  In the function, onWaypointReached, we will remove the incrementation of destination within the else statement and add the same repeat-loop to ensure it finds a new target after the current one is out of range or dies.
    

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/1df3aaba-cb8f-42f2-ac55-5c4c81bb854a.png)

3.  In the function, onPathBlocked, change goals[destination] to destination.  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2004/e870d739-b94b-44c2-b07f-504debff0a15.png)
    
4.  The zombie should now chase any Model with a Humanoid inside given its range. 
    
    1.  Remember, any enemies you want to create, rename Humanoid to Zombie so they don't include themselves as something to chase.
        

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.