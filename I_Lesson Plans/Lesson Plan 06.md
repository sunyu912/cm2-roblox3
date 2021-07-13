
# Lesson 6: Protective AI Companion (Part 1)

  

  

# Summary and Learning Objective(s):

-   Create a companion that follows the player around given a specified distance (so they are not colliding against the player).
    
-   The companion should sense any “enemies” nearby.
    

# Important Notes:

-   The lessons are written in more detail and hands-on if the students are willing to see the process.
    
-   Otherwise for larger classes and for the sake of time, the Step-By-Step is provided along with a link to the scripts. **The Step-By-Step is now updated. The directions including the link below should be updated as of 2021 July 7 for clarification.
    

-   Link: [https://bit.ly/roblox3_6_1](https://bit.ly/roblox3_6_1)
    

-   From there, an overview of what has changed between the previous iteration and the current iteration can be applied.
    

# Class Schedule/Tasks:

## Creating Your Companion

1.  We are going to be creating a similar script like our Zombie from the previous lesson with some tweaks to turn it into a protective companion.
    
2.  There are three things we would want for a basic companion:
           
    1.  They should follow us with some distance between the player and the companion.
        
    2.  They should sense any enemies around the player given a detection range and go attack.
        
    3.  They should come back to the player once they can’t sense any enemies.  
          
        ![](https://lh4.googleusercontent.com/7OUOVGP_2rG38jqYY5SH8c5ujaMmsjHkWjNuuKfB9HamBGd8lVy-B_MWc3xv8FXfuyrmz4uEoJW7jOBtH5mfHqhdwRdbcaLaa0ULWatXF9m3nTxaUCmeQg6MkBpZWiIuQSShi3uG)
            
    4.  Spawn in a Dummy and rename it to whatever you’d like (Ex: Companion).
                
        1.  Take some time to color the companion.
            
        2.  Rename the Humanoid to Companion.
            
        3.  Create a new script and rename it to CompanionMoveScript.  
              
            ![](https://lh5.googleusercontent.com/Nd589L89XE4tI4vO78_rvHbdwWbR_zG72F2rp0kLcbj65AG9sjYCw078yeuj5WHAUzL8C0htSZfqMAAbWXpm-PXTZxNR8f7ZJbHwaWt8motHODDELpf5EqU9UGCSqdlkxNTfYYi-)
            

6.  Add a Configuration folder (you can find this by clicking on the plus sign, just like how you add a script) and rename it to Config. Inside the folder, add the following:
        
    1.  Add a StringValue renamed to Leader.
           
        1.  This will be used to store the name of the player they are supposed to follow once they spawn.
         
    3.  Add three IntValue renamed to Damage, detectionRange, and gapRange.     
    
        1.  These will be used to allow us to change the Companion’s ranges and attack power without opening the script.
        

## Spawning with a Companion

1.  Place the companion model into ServerStorage so we can easily duplicate.
    
2.  Add a script to the ServerScriptService and name it SpawnScript.
    
3.  Inside we will add an event and a function:        
    
    1.  When a player spawns in, a companion is cloned and assigned that player’s name. The companion is also teleported on top of the player.  
        ![](https://lh3.googleusercontent.com/Bxax8bKN5zvwB0pydLyd9aXPJU3YJgmPCd1zQJDrDfnJbzNaARzB1izAzH8GJ-gsnN9H3335zRKEOkD4qCaf5Y581D_ePxYIgOYtmAFmaI1cDndEzYbfKgmInoqEzXOqG6GRGorM)
        

## Coding the CompanionMoveScript

1.  Like the previous lessons, we’ll be typing a similar script, modifying some of the functions and variables to fit our needs.
    
2.  **HEADS-UP Just so this is said ahead of time, this script would make the companion walk jittery as it is constantly updating to follow the player. This will need improvement for the future.
    
3.  These will be the variables we are working with:![](https://lh6.googleusercontent.com/9AC0i6SoFWJXDKvN55C4ISQiA9TTOdakkBRB5I3Pdu6MYOQxXysJzLkuAL9SNnQEjn3bGW1qu94RJeuTqAmOeRcEb49c5rR2NY451GKbRlZWmSQ6L99_ZIIF-oyy602eClLhJcot)
    
4.  Let’s write the function we have been using for the past lessons now, followPath().  
    ![](https://lh3.googleusercontent.com/MnU_D36LmTTxinF8G1_5tEnf_4WfZ6txLuMYLEKwBsAtyj6SVFEi2UFOp5wQnn4PrBYh4IH5QZJFNUPmbyRmXSLpdIM8KKvBUlH4Heo-Sm4XwG8apegzBH4_0Vt49_nzGyQWTrUE)
    
5.  Next is the function findNearest() which has been adjusted to remove the chase parameter from the Zombie version. It will now shuffle through to see if a zombie is nearby, else follow the player.  
    ![](https://lh3.googleusercontent.com/wjB5_ME-K_XGpjjyROBfzWJVEf15xSbJKxfoG6d4CPdiakIkD9Nb_Hex0FDQ1L9JNstYx7L9UlZF6HA6NXTuXLm3mGtQ0TDp-N38cnJFVaRP0k8YpahTKDCGOm0VwvBI4uilZdga)
    
6.  Compared to the Zombie script, we adjusted an if statement to gauge if the companion found an enemy or not. This will decide how the companion moves. Following the player will leave a gap between them. Following the zombie will not, thus it will touch to attack.  
    **This part is where the jittering occurs due to the calling of findNearest on line 69.  
    ![](https://lh4.googleusercontent.com/Glu7ruEb7DE4mpGuc8-2qoHlS7W1oWebndGSn58_tXIfBr5abNkcLGQWMpY9kMtFY_IJTmGVuMM4bz1LstYpJo0Nd4t3j6ydWZZpfYlZI8wI6hF1uWzFFjXJinxtlmx1qV8RGs8Z)
    

  

7.  Next, let’s write the functions for onPathBlocked() and onTorsoTouched() so that the companion can check for obstacles and deal damage if it touches a Zombie type humanoid.  
    ![](https://lh5.googleusercontent.com/-gY_8nELHBfKvf5IFEFPkCZko5sJvRIMAYlNCVlTbIuJI_-Oux-SuOQVRifd90tgoYM-PQ8Z6x9yD6XjADI8LUfPMbLaHaX5xX27Ez1OPfr2809iuzHmGPv9iEAJw5nhD0_ye6Ml)  
      
    
8.  Last thing we would want is to take the name of the player assigned and search for their Character in order to get their Position in the game. Thus we’ll define a new function called getPlayerFromName. Let’s also not forget to Connect the functions to the events!  
    ![](https://lh3.googleusercontent.com/9NBfDKEMkJ9Ig8grbp89nhkalEIQZA4gUW5T5ep-AWA5N6h06k3g8bZI_aAap9zFQ86AAtlKuf6RHAAEm__--zGNR-lyNdq4oOyrcgus6aicryYIJRp2A0PT0s9jL8bD2rZXgj61)  
      
    
9.  You’ll notice repeat-loop assigning the Leader’s value to our leaderName variable. This is because it isn’t immediately registered and needs some time before it updates. That is why we wait till we get the information we need before continuing.
    

  

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on Roblox. We will be grabbing them again and again for future lessons.