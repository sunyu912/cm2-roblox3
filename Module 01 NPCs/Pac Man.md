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

   ![](https://drive.google.com/uc?export=view&id=1_W24pSI0nCf3bVvVuq6bED7bV_JTdjmY)

2. Add BrickColor and Material

   ![](https://drive.google.com/uc?export=view&id=13zYGSdGEGqw3kvueN1s5JW4st5VBllHa)

3. Make one sphere slightly smaller and rename it to `HumanoidRootPart`, the wedge to `Mouth` and the other sphere to `Head`

   ![](https://drive.google.com/uc?export=view&id=1k96II8e47xumOZwlVCf88gnN5sjP2GIC)

4. Place the `Mouth` in a way it will cut out from the `Head` to make it look like Pac Man. Don't use the small sphere yet. 

   - **Hint**: Turn off collisions so you can move the `Mouth` inside the `Head`.

   ![](https://drive.google.com/uc?export=view&id=1UKhM7yWmnIh_PDvtwi1gNSVJrZWU0NZ4)

5. Select the `Mouth` and make it a negative part by selecting the option from "Model" and "Negate" (red in image)

   ![](https://drive.google.com/uc?export=view&id=1Mmuee04ZZU0m8jwWunfYxDaE3oJRoje-)

6. Then select both the `Head` and `Mouth`. Click on the "Union" option (red in image). Make sure you rename the new `Union` to `Head`.

   ![](https://drive.google.com/uc?export=view&id=1M0aVMdlTImzXv-pH5v1YOH54i6i2cnUL)

7. Now place the `HumanoidRootPart` roughly in the center of the `Head` and make it transparent.

   ![](https://drive.google.com/uc?export=view&id=19G8vkhFA0bMM_rVnWYvEj-yDGL52KUOl)

8. Select both parts and group them using "Ctrl + G" and rename the "Model" to `StarterCharacter`. **Note:** This rename is important to be able to play as this object.

   ![](https://drive.google.com/uc?export=view&id=1NOsjmlW2WTyKb6PcPK6R9LO6VIa2fzkU)

9. Add a "WeldConstraint" 

   ![](https://drive.google.com/uc?export=view&id=1IYSa1qOKMe7Grvt4Z6k1npdxwgzKk-E_)

10. Connect the `Head` to the `HumanoidRootPart` by changing the "WeldConstraint" *Part0* and *Part1* to them respectively (red in image)

    ![](https://drive.google.com/uc?export=view&id=1gRmg2Y4zBjRR-Gad2g_uAQSXafIMs55I)

11. Add a "Humanoid" to the "StarterCharacter" and change its "HipHeight" property to 1. **Note:** "HipHeight" changes how far the `HumanoidRootPart` is from the floor by studs, you can make it a bigger number if necessary.

    ![](https://drive.google.com/uc?export=view&id=1AUNSzFcEATuSSMHUH78AG4buBrfWqlOb)

12. Place the `StarterCharacter` in the "StarterPlayer" folder and click play!

    ![](https://drive.google.com/uc?export=view&id=1gp1aDtkxTSwaFc8auDsFsiGR5HKnlkHG)


### The Scripts

Script some pellets! Add a small sphere, rename it to `Pellet`, anchor it, turn off its collission and make it Neon.

   ![](https://drive.google.com/uc?export=view&id=1LnE3ATw2KPXoagjGK0wNphkfJn3j7aSQ)

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

![](https://drive.google.com/uc?export=view&id=16uFRwZrM93OYqBZaD9xtV4tomKc5iKxj)

Now you can clone it and touch them to eat them!

Now, we will script Pac Man to make sounds! We will be adding some code to have Pac Man make the famous "Waka Waka" sound when walking. Add a Local Script object on the "StarterPlayer" folder and rename it to `WalkingSound` (red in image)

![](https://drive.google.com/uc?export=view&id=1cgGEnceF9hbkk1Z12CtRTbOR8P20w4wZ)

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

   ![](https://drive.google.com/uc?export=view&id=14pTw_Ltfn-73iLl_PlnFBKBD_rU32rrP)

   

   

