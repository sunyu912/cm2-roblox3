

# Lesson 8: Protective AI Companion (Part 3)

  

  

# Summary and Learning Objective(s):

-   We will stray a bit from pathfinding to create a user interface for the companion.
    
-   The UI can include commands like:  
    

-   "Standby"
    
-   "Alert"
    
-   "Heal"
    
-   Set follow distance gap
    
-   Set how far companion can go before returning to player  
    

# Class Schedule/Tasks:

## Setting Up the Companion UI

1.  Visit this  [link](https://developer.roblox.com/en-us/articles/Intro-to-GUIs)  for a refresher on GUI and positioning the UI items relative to screen size.
    
2.  Start by creating a ScreenGui in StarterGui and renaming it to CompanionGui  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2008/11f0b47c-bbf8-4ecb-abeb-8f6a2965ba6b.png)
    
3.  In this lesson, we will just create settings for the companion's detection range and healing powers.
    
4.  We will create incrementational buttons to adjust the values instead of input them manually.
    
    1.  You can if you want to. Just remember it will have to handle wrong data types inputted.
        

6.  I will start with creating a title label, signifying to the players that they opened the companion's menu.
    
    1.  Inside CompanionGui, insert a textLabel and rename it to companionLabel.
                
        1.  The difference between TextLabel and TextBox is that Label cannot be clicked on and changed during the game while Box can.
            
        2.  If you want to do inputs instead of incremental buttons, use TextBoxes.
                           
        3.  There are 4 main properties we will be using for all UI items:
               
    1.  Text - holds all things related to text visuals
        
        1.  Change the Text property to Companion Menu
            
        2.  Turn on TextScaled so that it resizes to as big as your label size.

        3.  AnchorPoint - a specific point on the object to align with the screen position you set
            
            1.  We want ours in the complete center of the label to make positioning easier.
                
            2.  Set AnchorPoint as:  
                ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2008/92e0f07e-d9c2-40ea-9896-8075443d99c6.png)
                

5.  Position - determines where it will be drawn in relation to its parent object
    
    1.  We want it centered on X, but near the top of Y.
                
        1.  Scale is a percentage of the parent's width or height.
            
        2.  Offset is a specific number of pixels away from the origin (0,0) in either X or Y.
        
    3.  Set Position as:  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2008/829e9966-6597-4eef-97e8-8a0444691652.png)
    

7.  Size - changes the width or height of the item itself
    
    1.  This works similarly to Position.
        
    2.  If you set the sizes to be 0.1, it translates to being 1/10 of the screen size.
        
    3.  Set Size as:  
        ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2008/58e8196d-e6d1-4aee-ba27-cf5ed86744ad.png)
        

8.  Follow those same steps above for a rangeLabel, but putting your own adjustments.
    
9.  Inside rangeLabel, add a TextButton and rename it to minusButton.
    
    1.  Set text to a "-" sign and adjust anchorpoint, position, and size.
        

11.  Insert a script inside minusButton and rename it to minusScript.
    1.  Let's go over what we want:
          
        1.  When this button is pressed, decrease the Companion's range value by 1
            
        2.  In order to do that, we need to find the companion that is assigned to us before we can access their range value.
                  
        3.  Here is what the script looks like:  
            ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2008/60b83612-1a99-4cd4-b970-1c34201434fe.png)
            
        4.  Notice how findCompanion( ) is similar to getPlayerFromName( )?
            
        5.  Try it out and you'll notice the range values changing!
            
        6.  Duplicate the minusButton and change it to plusButton, adjusting it to add 1.
        

13.  Let's finish up by having a button to toggle the menu on and off.            
    1.  Place a TextButton named toggleLabel inside CompanionGui.    
    2.  For the sake of time, you can adjust the position and sizes later.   
    3.  Place a script inside toggleLabel and name it toggleScript.  
        ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2008/7575dce2-2570-4527-805e-7c340bc186a7.png)
        

15.  The Gui should appear as such below:  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2008/a696f675-f1fe-4bb7-af4e-5a37bb8812e4.png)
    

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on Roblox. We will be grabbing them again and again for future lessons.