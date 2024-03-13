## Project: Temple Trap

Creating a trap that is set off whenever a player gets recognized.

We will be utilizing the following topics:
  - Raycasting
  - Events
  - Physics
  - Touched

### Making the Temple Model

1. Create some sort of tunnel, or a temple scene with walls and a ceiling. Name the ceiling part "TrapPart."

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Temple%20Trap/eeb1e314-ba2b-4518-bf7b-d3468b19ea7a.png)

2. After you have created a temple scene, you want to create a room above the ceiling where the trap will be located. That part of the ceiling should be a separate block of the ceiling, since you will be destroying it later.
3. Add a large boulder into the trap room and name it "Rock."

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Temple%20Trap/a3eac78f-087a-492e-b8aa-bf5975c155e0.png)

4. In the Explorer, go through the list of parts you've made so far and anchor them (red in image). Repeat this for every part except TrapPart.

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Temple%20Trap/a577fda1-e2b7-41f1-a8a6-6235656d3e80.png)

5. Create a block part where the trap will be activated, this should be right below the trap room with the boulder in it on the wall. Name it "RayPart."

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Temple%20Trap/6aec35da-2b23-4e80-aa54-3f2a284113d7.png)

6. In the Explorer, click the plus button next to RayPart and add an attachment (red in image). Name the attachment "RayStart." This is where the raycast to detect the player will start, and it should be at the end of TrapPart.

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Temple%20Trap/30c41b80-7bdb-46d1-aca2-5d651a7df108.png)

7. Make sure that the attachment is parallel to the center of TrapPart.

8. Put every part used so far in a folder and name it accordingly, for example "Temple" or "TempleTrap." Make sure its contents look like this:

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Temple%20Trap/66e23f2d-6fd7-43df-b187-fce711aa9c5f.png)

9. Click the plus button next to this folder and add a script.

### Making the Script
```lua
local folder = script.Parent
local rayPart = folder.RayPart
local rayStart = rayPart.RayStart

local rock = folder.Rock

local rayOrigin = rayStart.WorldPosition
local direction = (rayStart.WorldPosition - rayPart.Position).unit
```
Firstly, you need to create the variables for your trap raycast to work.
- You first need to reference every part that plays a role in the Temple Trap, such as Rock, TrapPart, which holds the rock, and the player detector. If you named all parts exactly as you were instructed in the lesson, there is nothing to change in the code. However, if you used different names, you need to edit these variables to match what you named your parts.
- rayOrigin is the world position of the point from which the player detector raycast will be shot.
- direction is the .unit (Unit is a single vector 3 with amplitude of 1 in every axis) direction that the raycast will shoot in.

```lua
while wait(0.1) do
	local raycastResult = workspace:Raycast(rayOrigin, direction * 100)

	if raycastResult then
		if raycastResult.Instance and raycastResult.Instance.Parent:FindFirstChild("Humanoid") then
			folder.TrapPart:Destroy() --Alternatively, you can disable the CanCollide property of the TrapPart so the rock will just fall through it by doing TrapPart.CanCollide = false
			
			rock.Touched:Connect(function(hitPart) --The reason this is here is because we only want to check if the rock touched the player after the trap has been set off
				if hitPart.Parent:FindFirstChild("Humanoid") then
					hitPart.Parent:FindFirstChild("Humanoid").Health = 0
				end
			end)
			
			break
		end
	end
end
```
The script works in a while loop, where with each iteration a new raycast is shot to detect the player.
- If the raycast hits something with a humanoid inside it, then the trap will activate.
- To activate the trap you can destroy the ceiling part which holds the boulder, or alternatively you can disable the CanCollide property of the same ceiling part.
- Only once the trap has been activated, we want to check if the rock touches a player, and if it does, then set the humanoids health to 0.

### Challenge Steps

- Create a different temple trap, just now we made a boulder trap, you could also try doing an arrow trap from the top, or even a spike pit trap.
- Create a string that breaks as a trap detector, right now we have a simple trap detector, but to make it more realistic you could create a string from the detector to the wall and destroy it when it has been successfully set off by a player.