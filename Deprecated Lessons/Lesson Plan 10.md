

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
        
    2.  We want to create a folder with the Player’s Name to store all of the Follower clones.
        
    3.  We want a script to constantly compare the current amount of Followers versus the max amount of Followers we want.
        

1.  If it is too little or too much, we will clone more or destroy more Followers.
    

4.  Let’s first create a script in ServerScriptService (does not matter if you place this in the Workspace too! This is just for organizational purposes)  named SpawnScript that will set up the data values that we need when a new Player spawns in:
    
    1.  This script will create 2 IntValues named, maxFollowersInt and currFollowersInt.
        
    2.  This script will also create a Folder with the Player’s Name to store cloned Followers.  
        ![](https://lh6.googleusercontent.com/L273aQeaWKHpb2piDVYj-Kv1IkFhDFdVSZ84SGOaVDQRXKYYU6Vbkre0Vaddxn5kHOzEoSJ8DrxPEnSDOoaRkvBA5cXwt5r09Mpp7Y_l8mquI9aam5cyQMBYmwMgSeYgpZqq3yFw)
        

6.  Now create another script that will constantly check the amount of Followers the Player wants:
    
    1.  Place it inside ServerStorage for duplication when the Player respawns.
        
    1.  You do not want to put it in StarterPlayerScripts as it will not persist when the Player respawns.
        
    3.  I will name this script, FollowerHandlerScript
        
    4.  For the variables, create one to store the Player’s character, one to store the location of the Follower Folder, and one to keep track of who’s last in line:  
        ![](https://lh5.googleusercontent.com/N8iWWxIekPObsAz67OuK08jGI1RzZN1VCL6e6nL6ObyA0HnaaZ0R0JKcb-lQKBO2_WCYqBw2n6ShdZGIuoz_bVHimFmTpjE3eg8SKbpIBej_tZwyshHVGCHtn1b-dTukhngSlrT_)
        
    5.  It will constantly check if currFollowers matches maxFollowers and balance the difference.
        
        1.  Cloning a Follower will search the Folder for the one last in line.
            
        2.  Deleting a Follower will find the one last in line and destroy it.
            

7.  To do so, we will use the while wait(0.1) loop to prevent timeout while still constantly checking.
    

![](https://lh4.googleusercontent.com/bNnmyrVQIcnz4EsmNy7FkjxidKVJQlky8cfEXfZEb7Fkqj4fR2P_ZgukSVQA88X71VHtZ-ltSSc4S-KyI8N1ApCCL2U71D5uk5-PDxj2kbS6I5C5PGfbxXTXU5aKZmOBoOPCPPpo)

## The Power to Influence the Line

1.  Lastly, we need to set up the buttons to influence our Follower numbers.

    1.  **Reference Lesson 8 for more UI details
    

3.  In the StarterGui folder, create a ScreenGui and name it FollowerGui.
    
4.  Create a label for the Follower configuration and place it however you’d like.
    
    1.  Mine will be called FollowerLabel.
    

6.  Child a TextButton under FollowerLabel and name it minusButton.  
    **Note: Having the buttons as a child of the label allows us to move the whole thing and keep the buttons relative to the label’s position.
    
    1.  Child a script under minusButton and name it minusScript.
    

![](https://lh5.googleusercontent.com/v1XG8sf54HEkZgpNfFfNxdiNtizHw8ixuAKfxBNSeWlxoxtUShoZVCwZPH-J3v8EWCnYh7_RvBcK4lSHavG59XlNi9UgAVY5OxEHb3ze6BfkFyUC4B2NWo4UEzoRliwDMRNNv285)

5.  Duplicate the minusButton and name the clone plusButton.
    
    1.  Change minusScript to plusScript.  
    ![](https://lh4.googleusercontent.com/LY919JYJQGWhtju3-6hDk6GVHiyGQeMMH0i2bwWwRErqkC3NXtvgOno0QiBkuA9CNxZlX-aM0xEhrcEgRgG1IxZh39Z07RSifY4R3wiyG1Zu33dyxS-m6q6r9OZqznO_pfNo1Baj)
    

7.  Of course, adjust the placement of the minus and plus buttons.
    

![](https://lh4.googleusercontent.com/xPtKHZVRxyklK2adEX56pRGoV5H0_mmnlmCocSqj_11H6MO5FvCdnocsZB00Ksfj4j0BKOjevLEZ0NNHfffy9JIDEoYqthp7qoW2pADMjTpTB5IYxh7IYceyc8QY_HJAPfT9y9yK)

7.  Alright, everything should be set! Test out that conga line. The Followers would still be jittery, I have yet to find a way to smooth out it’s movements.
    

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.