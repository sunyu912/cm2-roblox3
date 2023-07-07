## Project: Haunted Statue

In this project you will create a haunted statue A.I. that will only follow the player if they are not facing the statue, or else they will be frozen if the player is looking at them.

### Topics:

  - Pathfinding
  - Raycasting

### Setting up the Project

1. Navigate to the 'Avatar' tab and press 'Rig Builder'.

![](https://drive.google.com/uc?export=view&id=1F-y7XuTK_NJtcD-27xhSyY6fGc8cFemK)

2. In the pop-up window, select your desired rig for your haunted statue from the options.

![](https://drive.google.com/uc?export=view&id=1nPoSTLtFRmAgUY89yMIy4TsPbxVDKOV1)

3. Add a "Script" object to your "Rig" model.

4. Add an "IntValue" object to your "Rig" model. Rename it to be named "Damage." Then, look in the properties window and change the "Value" number to be any number you want.

![](https://drive.google.com/uc?export=download&id=1qVknJ3nxI_vJYY5NVsFrfnAS93LSkrMP)

### The Script

Let's start this script by introducing some of the basic setup once again.

```lua
-- VARIABLES

local NPC = script.Parent
local humanoid = NPC.Humanoid
local damage = NPC.Damage.Value
local torso = NPC.UpperTorso

local destination = nil
local detectionRange = 50

local path = game:GetService("PathfindingService"):CreatePath() -- Create Path object

local waypoints = nil
local currentWaypointIndex = nil

local frozen = false

-- FUNCTIONS
local function followPath(objectRootPart)

	path:ComputeAsync(NPC.HumanoidRootPart.Position, objectRootPart.Position) -- Compute and check the path

	waypoints = {} -- Empty waypoints table after each new path computation

	if path.Status == Enum.PathStatus.Success then
		waypoints = path:GetWaypoints() -- Get the path waypoints and start Humanoid walking
		currentWaypointIndex = 1 -- Move to first waypoint
		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)	
	else
		humanoid:MoveTo(NPC.HumanoidRootPart.Position) -- Error (path not found); stop humanoid
	end

end

function findNearest()
	local list = game.Workspace:children()
	local range = detectionRange
	local nearest = nil

	for x = 1, #list do
		local object = list[x]
		local currentHP = script.Parent.Humanoid

		if (object.className == "Model") and (object ~= script.Parent) then -- If this child is a Model type and not the Humanoid Model
			local targetRoot = object:findFirstChild("HumanoidRootPart")
			local human = object:findFirstChild("Humanoid")

			if (targetRoot ~= nil) and (human ~= nil) and (human.Health > 0) then -- If model has a RootPart, Humanoid, and above 0 HP...
				if (targetRoot.Position - NPC.HumanoidRootPart.Position).magnitude < range then
					nearest = targetRoot
					range = (targetRoot.Position - NPC.HumanoidRootPart.Position).magnitude
				end
			end
		end
	end

	return nearest -- After going through the whole workspace, it will return the nearest Humanoid model.
end

local function onWaypointReached(reached)
	if frozen then
		return
	end

	if reached and currentWaypointIndex < #waypoints then -- If a waypoint is reached and there is still more waypoints to go...
		currentWaypointIndex = currentWaypointIndex + 1

		if waypoints[currentWaypointIndex].Action.Value == 1 then 	-- We want the humanoid to Jump ahead of time, so after
			humanoid.Jump = true									-- the currentWaypointIndex increased by, we check to see if 
		end															-- the Action is Jump.

		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
	else
		repeat
			wait(0.1)
			destination = findNearest()
		until destination ~= nil

		followPath(destination) -- Call this function once to start the forever change
	end
end

local function onPathBlocked(blockedWaypointIndex)

	if blockedWaypointIndex > currentWaypointIndex then -- Check if the obstacle is further down the path
		followPath(destination) -- Call function to re-compute the path
	end
end

local function onTorsoTouched(otherPart)
	local targetHumanoid = otherPart.Parent:FindFirstChild("Humanoid")

	if targetHumanoid ~= nil then
		targetHumanoid:TakeDamage(damage)
	end
end

-- CONNECT EVENTS

humanoid.MoveToFinished:Connect(onWaypointReached) -- Connect 'MoveToFinished' event to the 'onWaypointReached' function

path.Blocked:Connect(onPathBlocked) -- Connect 'Blocked' event to the 'onPathBlocked' function

torso.Touched:Connect(onTorsoTouched) -- Connect 'Touched' event to the 'onTorsoTouched' function

-- START UP

repeat -- Repeat until we find a target
	wait(0.1)
	destination = findNearest()
until destination ~= nil

followPath(destination) -- Call this function once to start the forever change

NPC.UpperTorso.Touched:Connect(function (obj)

end)
```

Our humanoid model will need to determine the nearest Humanoid model in the workspace (`findNearest()`), create a set of waypoints to follow (`followPath()`), determine what to do after they reach a waypoint (`onWaypointReached()`), what to do if they can't reach a waypoint (`onPathBlocked()`), and lastly what to do if they bump into another Humanoid (`onTorsoTouched()`). Be sure to look through the code and reach it thoroughly if you're confused.

Now it's time for us to use the NPC move script and modify it so that the script checks if the player is 'looking' at the NPC.

- Check if the NPC has a target by checking the 'destination' variable.
- Create a variable to store the result of a raycast from the player's head to the NPC's head. To make a raycast, you can use 'workspace:Raycast(rayOriginPoint, direction)'.
- Check the variable that stores the raycast's result. If the variable is anything but the NPC's head, it means there is no line-of-sight, so the NPC is allowed to move. You can read the name of the object hit by using 'result.Instance.Name'.
- If the variable IS the NPC's head, then the player does have line-of-sight, but we also need to check if the player is facing the NPC. You can use dot product to check the angle between the direction the player is facing and the direction torward the NPC. You can find a guide on using dot product [here](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984)
- You can get the direction that the player is facing using 'player.Character.CFrame.LookVector', and you can get the direction to the NPC by getting the NPC's position and subtracting the player's position. If the dot product is greater than 0.15 or so, we can say that the player IS looking at the NPC, so set the NPC's destination to be its own position so that it doesn't move.

Here's the code that will do so. Paste this at the end of the script that you've written so far.

```lua
while true do
	wait(0.0)
	local inSight = false

	-- if there's a player we're targeting, cast a ray to it to check for line-of-sight
	if destination ~= nil then
		local player = destination
		local rayOrigin = player.Parent.Head.CFrame.p
		local result = workspace:Raycast(rayOrigin, NPC.Head.CFrame.p - rayOrigin)
		if result.Instance.Name == "Head" then 
			local angle = player.Parent.Head.CFrame.LookVector:Dot((NPC.Head.CFrame.p - rayOrigin).unit)
			if (angle > 0.15) then -- 1 means looking directly at them, -1 means looking opposite direction
				frozen = true
				humanoid:MoveTo(NPC.HumanoidRootPart.Position)
			else
				frozen = false
				repeat -- Repeat until we find a target
					wait(0.1)
					destination = findNearest()
				until destination ~= nil

				followPath(destination) -- Call this function once to start the forever change
			end
		end
	end
end
```

### Follow up

For an additional challenge, check if ANY of the players in the game are looking at the statue using a for-loop, so that it can only move if no one in the game is looking at it instead of just the target. You can get a list of all connected players using `game.Players:GetPlayers()`.