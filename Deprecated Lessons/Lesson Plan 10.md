

# Lesson 10: Conga Line (Part 2)

  

  

# Summary and Learning Objective(s):

-   For this lesson, we will then use are completed Follower to clone and form the line.
    
-   We will also create a UI to configure how long we want the line to be.
    

1.  The line will be dynamic.
    
2.  Decreasing line by one will destroy the farthest follower.
    

-   Increasing line by one will add onto the last in line.  
      
      
    

# Class Schedule/Tasks:

## Form the Line!

1.  Everything seems set. Now we will transfer the Follower model into ServerStorage for cloning.
    
2.  When the player spawns, we want to:
    
    1.  Have 0 Followers along with a UI to add or subtract the amount of Followers we want.
        
    2.  We want to create a folder with the Player's Name to store all of the Follower clones.
        
    3.  We want a script to constantly compare the current amount of Followers versus the max amount of Followers we want.
        

1.  If it is too little or too much, we will clone more or destroy more Followers.
    

4.  Let's first create a script in ServerScriptService (does not matter if you place this in the Workspace too! This is just for organizational purposes)  named SpawnScript that will set up the data values that we need when a new Player spawns in:
    
    1.  This script will create 2 IntValues named, maxFollowersInt and currFollowersInt.
        
    2.  This script will also create a Folder with the Player's Name to store cloned Followers.  
        ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2010/c82f7745-ae72-404c-a9e2-c2f767de1dbc.png)
        

6.  Now create another script that will constantly check the amount of Followers the Player wants:
    
    1.  Place it inside ServerStorage for duplication when the Player respawns.
        
    1.  You do not want to put it in StarterPlayerScripts as it will not persist when the Player respawns.
        
    3.  I will name this script, FollowerHandlerScript
        
    4.  For the variables, create one to store the Player's character, one to store the location of the Follower Folder, and one to keep track of who's last in line:  
        ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2010/244f8144-1acb-4bfc-ba45-5df6d99a65c1.png)
        
    5.  It will constantly check if currFollowers matches maxFollowers and balance the difference.
        
        1.  Cloning a Follower will search the Folder for the one last in line.
            
        2.  Deleting a Follower will find the one last in line and destroy it.
            

7.  To do so, we will use the while wait(0.1) loop to prevent timeout while still constantly checking.
    

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2010/20d0bcfb-7cef-4d4f-b1bf-e7043f7f9600.png)

## The Power to Influence the Line

1.  Lastly, we need to set up the buttons to influence our Follower numbers.

    1.  **Reference Lesson 8 for more UI details
    

3.  In the StarterGui folder, create a ScreenGui and name it FollowerGui.
    
4.  Create a label for the Follower configuration and place it however you'd like.
    
    1.  Mine will be called FollowerLabel.
    

6.  Child a TextButton under FollowerLabel and name it minusButton.  
    **Note: Having the buttons as a child of the label allows us to move the whole thing and keep the buttons relative to the label's position.
    
    1.  Child a script under minusButton and name it minusScript.
    

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2010/3868e155-5f35-4a36-95d0-1ec55958d5cd.png)

5.  Duplicate the minusButton and name the clone plusButton.
    
    1.  Change minusScript to plusScript.  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2010/78a40748-0606-4024-aa3a-0548e3d6e70e.png)
    

7.  Of course, adjust the placement of the minus and plus buttons.
    

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2010/d718338e-f1b5-47aa-9aca-22f6af1854d8.png)

7.  Alright, everything should be set! Test out that conga line. The Followers would still be jittery, I have yet to find a way to smooth out it's movements.
    

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.