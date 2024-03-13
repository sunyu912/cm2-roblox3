## Project: Slime

Making a slime humanoid and programming to jump around whenever a player gets inside the Slime's range.

We will be utilizing the following topics:

  - Creating Humanoid Characters
  - Player Service

### Making the Model

1. Create a sphere and a cube of the same size
2. Negate the cube in the 'Model' section of Studio.
3. Select both the sphere and the cube, and union them to create semisphere, the resulting object should look like a semisphere.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Slime/ff57479b-e489-488c-8119-00a5ca4e8a0b.png)

4. Name the resulting semisphere "Head" and put it inside a model called (Slime). You can set the Heads material and color to whatever you like.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Slime/9f6ff2aa-91b5-4034-8689-2bcb0f3b9ba0.png)

5. Create an invisible cube of the same size as the Head and name it HumanoidRootPart.
6. Put the HumanoidRootPart into the Slime Model and set that cubes position the same as the Heads.
7. Set the Slime Models PrimaryPart property to the HumanoidRootPart and turn off the collision on the Head.
8. And finally, insert a Humanoid object inside the model.

### Making the Script
First, add a Script object to the Slime model. Now, let's define some variables that this script will be using.
```lua
local slime = script.Parent

local detectionDistance = 50
local target
```
We want to note the slime's detection range as well as who it's targetting.

```lua
function getNearestPlayer()
	local nearestPlayer
	local nearestDistance = math.huge
	for i, player in pairs(game.Players:GetPlayers()) do
		local char = player.Character
		local distance = player:DistanceFromCharacter(slime.HumanoidRootPart.Position)
		if (distance < nearestDistance and distance < detectionDistance) then
			nearestPlayer = player
		end
	end
	return nearestPlayer
end
```
The GetNearestPlayer function loops through all the players and returns the player that is closest to the Slime. This function checks the closest player out of all the characters, and if the closest resulting player is within the Slime's detection range, it then calls the Jump function.

```lua
function Jump()
	local humanoid = slime.Humanoid
	humanoid.Jump = true
	humanoid.WalkSpeed = 16
	wait(humanoid.JumpPower * 0.02) --50 is normal JumpHeight and it takes 1 second for a full jump (50 * 0.02 = 1 second), the higher the jump the more time it takes.
	humanoid.WalkSpeed = 0
end
```
In the Jump function, we make the Slime jump up and temporarily set the WalkSpeed to 16. When the slime has landed, set the walkspeed of the slime back to 0, and repeat.

Now, let's use these two functions by pasting this at the end of our script.
```lua
while wait(1) do
	target = getNearestPlayer()
	if target ~= nil and target.Character and target.Character:FindFirstChild("Humanoid") then
		local targetChar = target.Character
		slime.Humanoid.WalkToPoint = targetChar.HumanoidRootPart.Position
		Jump()
	end
end
```
The script for the slime works in an infinite while loop that periodically calls our 2 functions. We first get the closest player and set that as our target. We then look at that target, and start jumping towards it.

### Challenge Steps

- One improvement you could add to the slime is whenever the Slime hits the player, the player could take damage.
- Another improvement is to redo the slime model to make it similar to that of minecraft, made up of many little slime rectangles that expand and contract per Slime's jump.