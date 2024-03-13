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

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/12dec863-b2b3-4870-bf85-e3a7762b024a.png)

3. Rename the blue sphere to "Shooter" and the Green one to "Target" (case sensitive). Rename the block to "Window".

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/3973f83d-55a6-4020-8f1a-935f98ab54e6.png)

4. Make the block longer, anchor it, turn collisions off, set the transparency to 0.5 and place it between both spheres.

   

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/fb91718f-a744-4795-856b-ec5186d6e10f.png)

   



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

     ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/f36b7070-8c8a-421c-a0a8-abb146ccdb16.png)

   - Add an `attachment` to both the Target and Shooter parts. Rename them to Attachment1 and Attachment2 (red in image). Naming order doesn't matter.

     ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/f6c621a5-2de7-4673-a38d-cd1629636fa8.png)

   - In the `Beam` properties, select the Attachments in both slots (red in image). Order does not matter.

     ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/b25a73b6-5db0-4584-bf7a-fcfdcb224d04.png)

   - Congratulations! Now a beam will show you the raycast shot direction!

     ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/fb91718f-a744-4795-856b-ec5186d6e10f.png)

2. Decorate it!

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Raycasting%20Lesson/a2c89ea9-cd75-4a7d-b587-44940c3119a1.png)

   

   

