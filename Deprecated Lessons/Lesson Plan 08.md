

# Lesson 8: Protective AI Companion (Part 3)

  

  

# Summary and Learning Objective(s):

-   We will stray a bit from pathfinding to create a user interface for the companion.
    
-   The UI can include commands like:  
    

-   “Standby”
    
-   “Alert”
    
-   “Heal”
    
-   Set follow distance gap
    
-   Set how far companion can go before returning to player  
    

# Class Schedule/Tasks:

## Setting Up the Companion UI

1.  Visit this  [link](https://developer.roblox.com/en-us/articles/Intro-to-GUIs)  for a refresher on GUI and positioning the UI items relative to screen size.
    
2.  Start by creating a ScreenGui in StarterGui and renaming it to CompanionGui  
    ![](https://lh5.googleusercontent.com/VNj8MgDEBqktt-VL6EGcRkewgi9YHD1i9AvZUqnC_aGqdkdTBn-QwunOtxoFprh9L8myAzpRv9nRWNWiNI2yOmoehZEY_nJHqwyEETT-iMD9PEaXb1BCavw25gDb9fA-VAZ_g-ju)
    
3.  In this lesson, we will just create settings for the companion’s detection range and healing powers.
    
4.  We will create incrementational buttons to adjust the values instead of input them manually.
    
    1.  You can if you want to. Just remember it will have to handle wrong data types inputted.
        

6.  I will start with creating a title label, signifying to the players that they opened the companion’s menu.
    
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
                ![](https://lh3.googleusercontent.com/SZ-pUHaQEjBOL9Lac5V_0aQgL7xiZzFeKv1CeQjoI5to-gvTA4XtwheXAOLzJKPVCze9g8Y2YOCEdZGx-7N3a_lJRvXu1eRIgrLUrsNxDFfHuJMXUwTfEftjgPyid4Ggyah2q4IB)
                

5.  Position - determines where it will be drawn in relation to its parent object
    
    1.  We want it centered on X, but near the top of Y.
                
        1.  Scale is a percentage of the parent’s width or height.
            
        2.  Offset is a specific number of pixels away from the origin (0,0) in either X or Y.
        
    3.  Set Position as:  
    ![](https://lh3.googleusercontent.com/Wp0s4Kdhm4T-5W36W32RCs6pW-lzU0i_3I5A_6uM3TpPeFiwKlgzVwurK6nZ2XXE2blIPDgGMe5GEGpx4eMWMFzSsrwOuWOrRiuAVdvib55Koj1z1-j5tK6jpDYFP2ewH6a6zC96)
    

7.  Size - changes the width or height of the item itself
    
    1.  This works similarly to Position.
        
    2.  If you set the sizes to be 0.1, it translates to being 1/10 of the screen size.
        
    3.  Set Size as:  
        ![](https://lh4.googleusercontent.com/uPy0VLqaoBmZyyfABS9wJCxhMb8lHmC3MxrqqE4ZbJxaG_F7f9xCsU5xWS3fMXUdH0X3Jz8sg1JLXJz2pgHDrQ-QToItkDYKluDBFQ4Hj7dntk6zqvrq-gUUmlrbNe-dGF_RMTiY)
        

8.  Follow those same steps above for a rangeLabel, but putting your own adjustments.
    
9.  Inside rangeLabel, add a TextButton and rename it to minusButton.
    
    1.  Set text to a “-” sign and adjust anchorpoint, position, and size.
        

11.  Insert a script inside minusButton and rename it to minusScript.
    1.  Let’s go over what we want:
          
        1.  When this button is pressed, decrease the Companion’s range value by 1
            
        2.  In order to do that, we need to find the companion that is assigned to us before we can access their range value.
                  
        3.  Here is what the script looks like:  
            ![](https://lh5.googleusercontent.com/kKoI-mw5oswShm49qsGJUS77OBbZ1GNVOQK1YFKmxo72vbBESf_ZPPQqMHAPzRAWfm8QicNdnpcLF3m_ncWCKJ-sNbTspVjRBAdcqCP_K6yv-O-cqk3hZnqFW40EXZez0UqSiJAD)
            
        4.  Notice how findCompanion( ) is similar to getPlayerFromName( )?
            
        5.  Try it out and you’ll notice the range values changing!
            
        6.  Duplicate the minusButton and change it to plusButton, adjusting it to add 1.
        

13.  Let’s finish up by having a button to toggle the menu on and off.            
    1.  Place a TextButton named toggleLabel inside CompanionGui.    
    2.  For the sake of time, you can adjust the position and sizes later.   
    3.  Place a script inside toggleLabel and name it toggleScript.  
        ![](https://lh4.googleusercontent.com/dwGQajUMpy2pHibWNiTpQO87t4JuIHWZEY5HnNZCQaohpSOyBWTQCM_x42w-F0RfDfZsofgDfNo0DfZWFlV7tV7HYlXhJy8TnL2dDKtDq5SWzKNsxi8YJmfYM7Rc9_DcM3oFJlSM)
        

15.  The Gui should appear as such below:  
    ![](https://lh5.googleusercontent.com/CBz5L1RI3i9j22JIYLqT2bjcZXlLo7_KOXzbXsU0gE_Tu2rLbbyIHZCL6tBw_T_rKjnxrK7z_fonkoZjvlXf8weq3us0vuzE-L_EScnH43IFQHp-2fG39upucj2b5b_3bn4p_O__)
    

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on Roblox. We will be grabbing them again and again for future lessons.