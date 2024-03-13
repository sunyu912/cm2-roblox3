## Mini Project: Pac Man

In this project, you will create a simplified recreation of the famous game of Pac Man in 3D. You will make the character to play as him and make 2 scripts. One to make the player controlling Pac Man do the "Waka Waka" sound when moving and the other a pellet to collect in the world when playing.

### Topics:

  - Parts
  - Material
  - BrickColor
  - Scripting

### Setting up the Project

A pellet a day keeps the ghosts away

1. Get 1 wedge and 2 spheres

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/a10f3bc5-30b7-47d8-a00e-aa1317f47a18.png)

2. Add BrickColor and Material

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/9cc6d08d-45a0-4dcf-a718-383fe97feadf.png)

3. Make one sphere slightly smaller and rename it to `HumanoidRootPart`, the wedge to `Mouth` and the other sphere to `Head`

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/4cef4082-de0b-4868-97ca-8d0fc8615540.png)

4. Place the `Mouth` in a way it will cut out from the `Head` to make it look like Pac Man. Don't use the small sphere yet. 

   - **Hint**: Turn off collisions so you can move the `Mouth` inside the `Head`.

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/5e119bfe-a4c4-4600-ad46-c7166ca94167.png)

5. Select the `Mouth` and make it a negative part by selecting the option from "Model" and "Negate" (red in image)

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/a5fd87be-9f4e-4986-bcd4-0898f16c6d8d.png)

6. Then select both the `Head` and `Mouth`. Click on the "Union" option (red in image). Make sure you rename the new `Union` to `Head`.

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/92b88bb1-c330-40d9-a543-c567d5734cd3.png)

7. Now place the `HumanoidRootPart` roughly in the center of the `Head` and make it transparent.

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/911a2e65-3c42-4c43-9490-12f053b30c83.png)

8. Select both parts and group them using "Ctrl + G" and rename the "Model" to `StarterCharacter`. **Note:** This rename is important to be able to play as this object.

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/7ee874d9-2680-4e86-bbb3-a9b55ddd9433.png)

9. Add a "WeldConstraint" 

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/68c27f3e-bd1a-4769-a127-f52c17701069.png)

10. Connect the `Head` to the `HumanoidRootPart` by changing the "WeldConstraint" *Part0* and *Part1* to them respectively (red in image)

    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/0025614b-eb2c-477a-84bd-b841d1323d71.png)

11. Add a "Humanoid" to the "StarterCharacter" and change its "HipHeight" property to 1. **Note:** "HipHeight" changes how far the `HumanoidRootPart` is from the floor by studs, you can make it a bigger number if necessary.

    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/94603cfa-77d8-4401-8604-36a200da6bd6.png)

12. Place the `StarterCharacter` in the "StarterPlayer" folder and click play!

    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/f1d60238-c58b-499e-8eea-773a9276d640.png)


### The Scripts

Script some pellets! Add a small sphere, rename it to `Pellet`, anchor it, turn off its collission and make it Neon.

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/2813f667-670f-4ced-813b-43f9e27084ba.png)

Add a script inside the `Pellet`, rename it to `PelletScript` and add the following code:

```lua
script.Parent.Touched:Connect(function(hit)
    if hit.Parent:FindFirstChild("Humanoid") then
        script.Parent.CanTouch = false -- So you can't touch it again
        script.Parent.Transparency = 1 -- So it becomes invisible and can play sound before dissappearing
        local eat = script.Eat         -- So you get the sound to play
        eat:Play()	                   -- Play the sound
        eat.Ended:Wait()               -- Wait for the sound to finish playing
        script.Parent:Destroy()        -- Destroy the pellet
    end
end)
```
   
In this script, we start by adding a function that is only activated when something touches the Parent object (pellet). It then checks it is a Humanoid (which players have). If it is a Humanoid it makes it invisible and untouchable to allow it enough time to play the pellet collection sound before destroying the entire object.

Inside the `PelletScript` add a "Sound" object and rename it to `Eat` (red in image). Then add the following into the SoundId property: rbxassetid://4797903038 (blue in image)

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/a1b304fc-978f-400b-8da6-ce658139523b.png)

Now you can clone it and touch them to eat them!

Now, we will script Pac Man to make sounds! We will be adding some code to have Pac Man make the famous "Waka Waka" sound when walking. Add a Local Script object on the "StarterPlayer" folder and rename it to `WalkingSound` (red in image)

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/22490a6a-1f8d-4815-ba12-32d4f2d78662.png)

Add the following code:

```lua
-- Line below gets the code block that is activated when a character walks/runs.
local walk = script.Parent.HumanoidRootPart:WaitForChild("Running")
-- You can change the code below to another walking sound ID if you wish.
walk.SoundId = "rbxassetid://5846853128"
```
     
In this script, we access the characters "Running" feature in order to change its properties. One of these properties is the sound made by the character when walking. As such we change the *SoundId* to the "Waka Waka" sound by getting the ID from one in toolbox.
   
Congratulations! You will now make the famous "Waka Waka" sound when playing as Pac Man!

### Follow Up

1. Decorate the world! 

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Pac%20Man/3b3cac6a-f645-4b1c-917b-092f87170aeb.png)

   

   

