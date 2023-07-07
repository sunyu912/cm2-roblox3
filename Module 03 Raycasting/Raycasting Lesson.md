## Mini Project: Raycasting Intro

In this project, you will create a simple raycasting introductory project. You will make 2 objects that look for each other based on whether there is something between them or not.

### Topics:

  - Parts
  - Material
  - BrickColor
  - Scripting

### Setting up the Project

Pew Pew Pew

1. Get 2 spheres and one block.

2. , Add BrickColor, specifically color one green and the other one blue. Any color shade works. 

   ![](https://drive.google.com/uc?export=view&id=12palzytAMdsSVePz5SMklO_FzoCLHrME)

3. Rename the blue sphere to "Shooter" and the Green one to "Target" (case sensitive). Rename the block to "Window".

   ![](https://drive.google.com/uc?export=view&id=1GmXHtubGuCNc9g3NctfljguI9GraJ_Ap)

4. Make the block longer, anchor it, turn collisions off, set the transparency to 0.5 and place it between both spheres.

   

   ![](https://drive.google.com/uc?export=view&id=1HBnCu3dolwI9rTfVc5_iYiOBcrpyTGHX)

   



### The Script

1. Script the Raycaster!

   - Add a script on the `Workspace`, rename it to `RaycastScript` and add the following code:

     ```lua
     local shooter = workspace.Shooter
     local target = workspace.Target
     
     while true do
         -- Calculates which direction the raycast will be shot for you
     	local direction = target.Position - shooter.Position
     
     	-- Gets the result of where the raycast is going to shoot
     	local raycastResult = workspace:Raycast(shooter.Position, direction)
     	
     	-- If we shoot something between the shooter and the target...
     	if raycastResult and raycastResult.Instance then
     		-- Color it Red!
     		raycastResult.Instance.BrickColor = BrickColor.Red()
     	end
     	-- Waiting 1 second each shot
     	wait(1)
     end
     ```

     In this script, we get the Target and Shooter parts so we can have a raycast being shot from one to another.  The while loop will make it repeat the whole process forever, so it can keep shooting. The code itself first gets the direction to shoot and then checks what it shot. If something between the Target and Shooter is hit, it turns red. If there is nothing between them, the Target gets hit and turns red.

   - Now play to see how it turns red in real time! Push the balls so they see each other and the Target turns red too!

2. Extra Script for the Target!

   - Add a script to the "Target" part and rename it to `NormalizeScript`

     ```lua
     local target = script.Parent
     
     -- Repeats forever
     while true do
     	-- Turns target part color to green
     	target.BrickColor = BrickColor.Green()
     	-- Wait 2 seconds before turning it green again.
     	wait(2)
     end
     ```

     This script is meant to turn the ball back to its original green color every 2 seconds so you can see how the `RaycastScript` keeps turning it back to red as long as it can see the "Target". 

3. Congratulations! You have finished the introductory lesson to Raycasting!

### Follow Up

1. Add a Beam!

   - Select the Target and add a Beam from `Model` => `Effects` => `Beam` (red in image)

     ![](https://drive.google.com/uc?export=view&id=1dIL76Ai5N-7mK10nEu7MakbQyTXlulKQ)

   - Add an `attachment` to both the Target and Shooter parts. Rename them to Attachment1 and Attachment2 (red in image). Naming order doesn't matter.

     ![](https://drive.google.com/uc?export=view&id=1WlHgnWRrb-qO9rkcmuZnyTpRiBD06JN1)

   - In the `Beam` properties, select the Attachments in both slots (red in image). Order does not matter.

     ![](https://drive.google.com/uc?export=view&id=14-f0jpY_A31nvKrQyeWkIHa20rcnmbCk)

   - Congratulations! Now a beam will show you the raycast shot direction!

     ![](https://drive.google.com/uc?export=view&id=1HBnCu3dolwI9rTfVc5_iYiOBcrpyTGHX)

2. Decorate it!

   ![](https://drive.google.com/uc?export=view&id=1fgoxPTywloZ7l43eVR9Z_XioAOGJIrP0)

   

   

