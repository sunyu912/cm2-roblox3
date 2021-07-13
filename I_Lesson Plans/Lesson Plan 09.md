

# Lesson 9: Conga Line (Part 1)

  

  

# Summary and Learning Objective(s):

-   Made as a two-parter in-case students need help catching up or would like to take the time to review.
    
-   A fun lesson where we create a line of Humanoids following the Player.
    
-   This spans for 2 lessons to make sure students can take their time and understand how to create step-by-step.
    
-   For this lesson we will focus on creating the Follower, the FollowerMoveScript.  
      
      
    

# Class Schedule/Tasks:

## Creating a Follower

1.  Use this as a review to recreate a Companion, but this time the Follower will have no other features except to follow their assigned target.
    
2.  Using the Rig Builder from the Plugins Tab, spawn in a model. I used the R6 Block Rig.
    
    1.  For this lesson, I’ll be naming the model and its Humanoid to Follower
    

4.  Next, Un-Anchor the HumanoidRootPart of your newly spawned rig. This will allow the model to actually move!
    
5.  Place an ObjectValue into the model and name it FrontObject.
    
    1.  FrontObject will store who the Follower it is following.
    

## Is the target moving and how do I follow?

1.  Create a script inside the Follower model and name it FollowerMoveScript.
    
2.  Just like how we created the NPC, Zombie, and Companion MoveScripts, this will almost be the same minus the extra features.
    
3.  First, we will lay out the variables:  
    ![](https://lh5.googleusercontent.com/J3idXNE0-mMM21H4Gg9zWYPhPxbGuD0BFhkVMfX-eBXRSaReJauA75MI66PsbC22HjvYPC1Dwlf57Dl5bdAk6VgSN4TrwRUyBMNDuNzzAJqONNJbAODdH0Bh63I_tIorvAEupeIV)
    
    1.  You will see 2 variables that are not familiar: front and frontPosition.
        
        1.  front will hold the object the follower is following such as Player or another Follower.
            
        2.  frontPosition will hold the position of the one it is following and will only update after we have reached its snapshotted position. This will be useful to prevent every Follower from constantly updating and calculating a path.
            

5.  Next, create the functions needed to calculate and move to the specified target.
    
6.  First function is followPath( ):  
    ![](https://lh5.googleusercontent.com/HhG-yI7AQG-MLqvHj1Nl5rheO8-661bxBq6dQehGFV7_UNatPhhtlYKTyJwnA5TdBNWt9-5Og1hWiSkUXIngmEFD3KW9Hmor-Hlp_h4yYRKK5VGG6utR2hhOilmosGuieeNuKJMn)
    
    1.  Nothing different than before. This function will take in a root Part in order to access its position.
        
    2.  Once the calculated path is deemed successful, it will proceed to move the Follower to the first position.
    

8.  Second is the event MoveToFinished connected with a function:  
    ![](https://lh6.googleusercontent.com/JaCILeisp20-GNrWESMviKqDFNNS_enrMxDEWVdovCScJlmnqapDwXqQUkph-VpsMxuPAZuqweGNKWSfARjSsrWmyiYtLniroeP1vn6Yc-Fu2GHlMY88-qvjTq_bywNbc4XzPJty)
        
    1.  This event will trigger as the Follower moves to its destinations, minus a few so there is a gap between each Follower.
        
    2.  Once it reached every single waypoint, it will repeat-loop to check if it’s front leader has moved or not.
        
        1.  If it hasn’t, keep looping and doing nothing.
            
        2.  If the position has changed, break out of the loop, update the new position, and calculate a new path again.
    

10.  Finally, we’ll kick start the program to loop after we receive all the information we need.  
    ![](https://lh5.googleusercontent.com/LYZjTircZC3cPuFZT5N2Vh7omfEqaA7NFPlbnNfycFiiZpdl8GDBKfWyd7fZ3Ht0Qr88nQqdEP_NaDVllXZ1m4hIkOJQwapivTcFttKdwvaQC_HE7rD9nRvlZErHz8o8Cn3xGca1)
    1.  Similar to what we have seen previously, we are using a repeat-loop to make sure we get front assigned with a value and not nil.     
    2.  After it has been assigned and we have saved it’s current Position, we can proceed with the program by calling followPath.
        

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.