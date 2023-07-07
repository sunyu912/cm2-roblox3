## Project: Temple Trap

Creating a trap that is set off whenever a player gets recognized.

We will be utilizing the following topics:
  - Raycasting
  - Events
  - Physics
  - Touched

### Making the Temple Model

1. Create some sort of tunnel, or a temple scene with walls and a ceiling. Name the ceiling part "TrapPart."

![](https://drive.google.com/uc?export=view&id=1s35RViKpTcGrTy--d1-DG7daEaZr1FiT)

2. After you have created a temple scene, you want to create a room above the ceiling where the trap will be located. That part of the ceiling should be a separate block of the ceiling, since you will be destroying it later.
3. Add a large boulder into the trap room and name it "Rock."

![](https://drive.google.com/uc?export=view&id=1nbwFPWlEUXFEPsaUfRdCHRxt8WOZHGZo)

4. In the Explorer, go through the list of parts you've made so far and anchor them (red in image). Repeat this for every part except TrapPart.

   ![](https://drive.google.com/uc?id=11IzriUY42IbJe_nsyE9_M8KqnLxTniZu)

5. Create a block part where the trap will be activated, this should be right below the trap room with the boulder in it on the wall. Name it "RayPart."

![](https://drive.google.com/uc?export=view&id=1_ChWUo-zDmHCQh8YyhBAxNg3tkzYMNh6)

6. In the Explorer, click the plus button next to RayPart and add an attachment (red in image). Name the attachment "RayStart." This is where the raycast to detect the player will start, and it should be at the end of TrapPart.

   ![](https://drive.google.com/uc?id=1xGIp9D7F8hKmqK8bzC3laMkQzvVKwhuh)

7. Make sure that the attachment is parallel to the center of TrapPart.

8. Put every part used so far in a folder and name it accordingly, for example "Temple" or "TempleTrap." Make sure its contents look like this:

   ![](https://drive.google.com/uc?id=1_K_ApKC-g_4wv-t137aAuN-Ha9QgdBKA)

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