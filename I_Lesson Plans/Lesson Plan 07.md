
# Lesson 7: Protective AI Companion (Part 2)

  

  

# Summary and Learning Objective(s):

-   We will make another mode for healing the player.
    
-   If the companion is with the player, it will slowly regenerate the player’s health back.
    

# Important Notes:

-   Link: [https://bit.ly/roblox3_7_2](https://bit.ly/roblox3_7_2)
    

# Class Schedule/Tasks:

## How Do We Want the Companion to Heal

1.  Let’s go through what we want:
     
    1.  Only when the Companion is following the Player do we want it to regenerate the Player health.
        
    2.  We want to have the regeneration happen every few seconds.
        
    3.  If the Companion is off to attack an enemy, we want to stop regenerating until they come back to the Player.
    

## Giving Companions the Ability to Regenerate the Player

1.  Inside the companion’s Config folder, add the following Values:
    
    1.  First, let’s add a BoolValue called Heal.![](https://lh4.googleusercontent.com/b2T0bPOrocSx1UiTexVfa3n0AmkJubcrgJI1L9O906gt9za4SVlcKZ1kBOj3lN-Nwmi1zSP-1Hu8mG-7XJbzK86wZjhFwtoQDnl61gtwn-JWQg8ttRGKft5Aqk1tBjtu6W8QJQBQ)
        
        1.  We will be using this to toggle healer mode.
        

3.  Add two IntValue called healPower and healDelay.
    
    1.  This is for easy configuration. For now set healPower to 10 and healDelay to 2
        

5.  Next, add an ObjectValue called PlayerCharacterObject.  
    
    1.  This will store the Player.Character after getPlayerFromName( ) in CompanionMoveScript returns the object.
        
    2.  It is used to save us scripting time and space from duplicating the function when we can just write and call it once.
        
    3.  To save us from cluttering the CompanionMoveScript with more lines, we will create a new script just for healing.               
        
        1.  Place a new script into Companion and name it HealScript.
            
        2.  Here is what the entire script looks like:  
            ![](https://lh3.googleusercontent.com/Tty14Uqylw5RXmIX42YKUoj5eW0kAQyIEfsCtfIosdiA6FU9PCModjIG7Bhlo3oYWwafBbVmthWdFA3LNk6bLS1kTcZQSi1tyIsZwMmn-DMhONpL11qSFEMyH_iXKlUmvI5RCl9J)  
              
            

5.  All we need to do now is add a few lines in CompanionMoveScript.

    1.  Near the end, just after we assign the leader value with the Player’s Character object, we will also assign it to the PlayerCharacterObject we created.

    ![](https://lh3.googleusercontent.com/nV6rron-4qSZtucMk-Zs6sUCN8RH1n04I0g9nMziAfnIq8-kDCsY_fw82EWA8B77B-wCVf1-zgQ69V16H592vhIeoIjd6nlR-2bnh4hjVz1d1F6-PVhGkvRNilt-jnPfmdQrzODg)  

    2.  Lastly in the onWaypointReached function else statement, we will add an if-else check to flip Heal on or off.
        
    3.  If the destination is the leader then Heal will be true, else it will be false.
        
    ![](https://lh4.googleusercontent.com/UQFIno3BwkemUpS4yUPLS-L9WNcOI1zPB1vP5roNDuqpGjhdGzQutYG0duFbFTxOXvg1x6Stsf__VQCsyfMZcjLfm_Ejsunf9Nb6cBPb9q6BEeQaa9Bb6IiwkpDlSxWfFh7gvbdL)

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.