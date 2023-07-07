## Project: Creeper

In this project, you will create a Creeper A.I. character from Minecraft that will follow nearby players and, when in range, explode after a brief delay.

### Topics:

  - Pathfinding
  - Explosion Particles
  - Playing Sound

### Setting up the Project

Follow these steps to build your very own Creeper model! Alternatively, you can download a pre-made model [here](https://www.roblox.com/library/13446853233/Rigged-Creeper).

1. Spawn two blocks, and either color them green or another color of your choice. Name one block "HumanoidRootPart," and name the other block "Head." Adjust the sizes and shapes of the two blocks so they look like a Creeper's body, as shown in the image.

![](https://drive.google.com/uc?export=view&id=1nbTvMDNIsJU9vUzsrgQqgbZ5Pu-LuKMm)

2. All parts of the Creeper must be welded together. Click the plus sign next to one of the parts and search for "WeldConstraint".

![](https://drive.google.com/uc?export=view&id=1P_2p_dq3krJQo-PWKhq6tP6cYhHmOVHc)

3. Then, in the details panel of the WeldConstraint you just created, find the properties labeled "Part0" and "Part1". These represent the parts that you are welding together. Click Part0, and when a block selection cursor appears, click on the "Head" block. Likewise, click Part1, and when a block selection cursor appears, click on the "HumanoidRootPart" block.

![](https://drive.google.com/uc?export=view&id=1Pvh3MKZYZBzAULrhxqDRVHEk6OxRMuVX)

4. Then, Ctrl-click both the "Head" and the "HumanoidRootPart" to select both of them (they should both be highlighted in blue). Use the shortcut Ctrl+G with both of them selected to group them as a model.

![](https://drive.google.com/uc?export=view&id=10-um8OT7Cp3uJFyEH0E5EM-CkwVW6cSy)

5. Now, click the plus sign next to your newly created Model group and add a "Humanoid".

![](https://drive.google.com/uc?export=view&id=1jFNycSbKrGH8o1CA4YeItdKZM4K54SoH)

6. Finally, add two more blocks to be the feet of the Creeper. Add WeldConstraints to both of them and weld both of them to the "HumanoidRootPart." You can also add a face decal to the Creeper by clicking the plus sign next to your "Head" part and adding a "Decal". In the details panel of your Decal, find the property called "Texture," and copy-paste the following link into the box to crate a Creeper face texture: http://www.roblox.com/asset/?id=50018586.

![](https://drive.google.com/uc?export=view&id=1MIgULC50lQ6W59zvAzefVGMLrgYJ1guE)

### The Script

First, let's setup the basic player-targeting movement code. This may seem unfamiliar to you, but in future lessons, it will make a lot more sense. Click the plus sign next to Model, and add a script. Copy-paste this code to the script:

```lua
-- VARIABLES

local NPC = script.Parent
local humanoid = NPC.Humanoid

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

        if waypoints[currentWaypointIndex].Action.Value == 1 then     -- We want the humanoid to Jump ahead of time, so after
            humanoid.Jump = true                                    -- the currentWaypointIndex increased by, we check to see if 
        end                                                            -- the Action is Jump.

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

-- CONNECT EVENTS

humanoid.MoveToFinished:Connect(onWaypointReached) -- Connect 'MoveToFinished' event to the 'onWaypointReached' function

path.Blocked:Connect(onPathBlocked) -- Connect 'Blocked' event to the 'onPathBlocked' function

-- START UP

repeat -- Repeat until we find a target
    wait(0.1)
    destination = findNearest()
until destination ~= nil

followPath(destination) -- Call this function once to start the forever change

```

Now we will add code to the end of the script that checks if the target (destination) is within a certain range, and if so, the Creeper will explode after a brief delay using explosion particle effects.

Below is an example of the code. Copy-paste it to the end of the script. You can also modify it to your liking.

```lua
    while true do
        wait(0.0) -- wait one frame
        if destination ~= nil then
            local magnitude = (findNearest().CFrame.Position - NPC.HumanoidRootPart.CFrame.Position).Magnitude
            if magnitude < 3 then -- if a player is within 3 units, wait one second then create an explosion
                wait(1)
                local explosion = Instance.new("Explosion")
                explosion.Parent = workspace
                explosion.Position = NPC.HumanoidRootPart.Position
                script.Parent:Destroy()
            end
        end
    end
```

### Follow-Up

For an additional challenge, play a Creeper hissing sound before the explosion delay. You can find a sound like that in the toolbox. You can also create code so after the delay, if the player exceeds a certain distance from the Creeper, it will not explode and instead will continue chasing the player. This will allow it to behave more like a real Creeper would in Minecraft.
     
