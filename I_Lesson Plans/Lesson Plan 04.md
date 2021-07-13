
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

1.  There isn’t a huge difference between a friendly NPC and a Zombie enemy besides dealing damage.
    
2.  Start by duplicating our NPC from Lesson 3 and renaming it to Zombie for clarification.
    
3.  Before we get started on the script, let’s make the Zombie look more like a zombie.       
    
    1.  Rename zombie’s Humanoid into Zombie. This helps differentiate between friend and enemy.
        
    2.  Rename the NPCMoveScript to ZombieScript for later.
        
    3.  You can recolor each zombie part to look different.
        

5.  Add an IntValue into the Zombie model and name it Damage. This will make it easier for you to change the amount of damage a zombie does instead of finding and opening the script. I set the value to 10.  
    ![](https://lh6.googleusercontent.com/vFNaabhzry1WmDhT7XM65MywULXFkeAwu-716EyFrjVqHyRyKH5EBMNBag5Cj8dJFcs6mz9-Fj7NTXL1jqXkQ_HgTavJEFCF_x3B5jN6xb2Zj-rMsDOsoADOQP59OVI_OYEp69zr)
    
6.  Open up ZombieScript and add 3 new variables called torso that will store the UpperTorso part, damage that will store how much damage a zombie will inflict, and detectionRange set to any number.
    
    1.  If you haven’t already, also delete the goals variable from the previous NPCScript and set destination to nil.  The current variables should look like below.

    ![](https://lh6.googleusercontent.com/zfuywidj2i3rJg74JETLcrVzp2VlqfyPVit5uO9aQ1BeUVavXpNRe3IIqGdvxm2UFlHVDuQG1ORGQOwnvbzM5-z4dxJK4h6Z6r4X_s3IhHHKhP609UBmzqrfrAWQKcwZ0aZjaQzz)

6.  Now let’s create a function to connect when the torso is Touched. This is placed just above the Connected events.  
    ![](https://lh4.googleusercontent.com/KiCqrOKXV0fuu0d_9w0qkkbLrf39iO20FOnUkZbcDsGKIwjamLTO44_EyB9yxLLm2f8eihzRr2ClXHotwpLi9yLFrLClAHJP06h5xa5EoqRcyQ2ejivrIiuZiWBB6BTkVsnxGcM_)
    
7.  Connect the function to the Touched event.  
    ![](https://lh6.googleusercontent.com/Ud8-xUwJyrWa7HrCrWOzcMreKod4FTKzziAMRE4pR-QagdlPx-pVY3MNwV8HMBcaEFgwJbgkWy35AySjnJW9jCRoGvMHXr0P1LUkXYDIfUBBU3MJZ3zLz0PEOWT1FddhxDulTR2U)
    

## Finding a Target

1.  Instead of a series of goals, we will find the nearest Humanoid and set it as the target.
    
2.  Let’s add a new function right after followPath. This function will be called findNearest.  
      
![](https://lh6.googleusercontent.com/xwXzYZB-IxxoWhO1CS9eKkOunGLA4KSrthrij1wcpDs8khKoqhRRvG2ex-cT0OmaO7f6a1OqP8NZ90fYSbxXVmzcbSYelywnpFeF2UKvnQ8KbwBqG48ySW6LbQeTLjaukurWCyTS)

3.  To make sure we find a target before calling followPath( ), we will implement a repeat-until loop right at the end.  
    ![](https://lh6.googleusercontent.com/CtFkG_cJr549FwnzT3FxeSCj6O_4EOM1CwWcH0kGT1SmFpUOXGQxrtySwE4mwGCfsQYGYQ2rC92aEalxEpOzvMOSRdR_nxGvqt-CGUNsYIbWnvVw7Hs7HJ6s0F495l-pfgWYAZuO)
    

## Adjusting the Rest

1.  With the new function, we’d need to adjust a few lines from other functions and events.
    
2.  In the function, onWaypointReached, we will remove the incrementation of destination within the else statement and add the same repeat-loop to ensure it finds a new target after the current one is out of range or dies.
    

![](https://lh5.googleusercontent.com/N9Lw0qkEw9lU8IUff6BQuEapCmEiBDm3jBQSlUVtf82HQMlMH5LwaPxywuLQgbS0PLCgheTC2ZFxemIPugUsbXOYRzM1zSAToEtRS-7I9K11lWldB2cGVdqEEvsNLUD8Sj8meE9X)

3.  In the function, onPathBlocked, change goals[destination] to destination.  
    ![](https://lh5.googleusercontent.com/LE6GEN4GBeX1BPt9w6GZ0A8NA2m9Vt7Xte67dRmeuz-K2DbZpaY_g6em-E4VVXELwhaCJlQr3pOhN0usclIffM9g0dW8QmRwiTgmn362h3YhFsy2Aps08QUsRLEYaFCbsZjs-AzG)
    
4.  The zombie should now chase any Model with a Humanoid inside given its range. 
    
    1.  Remember, any enemies you want to create, rename Humanoid to Zombie so they don’t include themselves as something to chase.
        

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.