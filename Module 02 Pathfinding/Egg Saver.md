## Mini Project: (Project Title)

In this project, you will create a minigame! In this minigame, an egg got lost, and you need to help bring it back to its nest. This egg will use the pathfinding service to create a set of waypoints to direct the player back to the nest.

### Topics:
- Modeling
- Pathfinding

### Setting up the Project
We're going to start by making the egg and the nest (I prefer eggs and bacon though...). 
1. Get 1 part and 1 sphere (red in image). 

   ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Egg%20Saver/5b3705cc-110b-4b16-84ed-fa84d4b32ab6.png)

2. Add a BrickColor and a Material (blue in image).


![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Egg%20Saver/326f8bdf-8e38-40ee-b95b-2314d9a498fe.png)

3. Rename the part to "Nest" and the sphere to "Egg."

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Egg%20Saver/ed1116c2-e1e4-4214-89a5-08cec7e7759a.png)

4. Anchor the Nest.

### The Script
We will be adding some code to have the nest detect the egg's it touches! Add a script inside the Nest Part, rename it to `Egg Detector Script` and add the following code:
```lua
     local nest = script.Parent
     local points = 0
     
     local function onTouched(hit)
     	if hit.Name == "Egg" then
     		points = points + 1 -- Add 1 to your total points
     		print("You have got "..points.." points!")
     		
     		--Minimum and Maximum distance the egg can teleport from the nest
     		local minDistance = 5
     		local maxDistance = 10
     		
     		local newX = hit.Position.X + math.random(minDistance, maxDistance)
     		local newY = hit.Position.Y + 2 -- Makes it spawn a bit up in the sky 
     		local newZ = hit.Position.Z + math.random(minDistance, maxDistance)
     		--Teleport the Egg nearby!
     		hit.Position = Vector3.new(newX, newY, newZ)	
     	end
     end
     
     nest.Touched:Connect(onTouched)
```
In this script, we have a function to determine what to do when something touches the nest. If it's the Egg object we made, then we increase a point counter and print it to the console. Then, we want to restart the game, so we teleport the egg somewhere a little away from the nest using the random functions.

We will be adding some code to have the Pathfinder indicate where the egg should go to get to the nest. Add a Model on the Workspace and rename it to `Waypoints`.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Egg%20Saver/1c3dbb59-f9bf-4983-80d2-d9472e1b997b.png)

Add a script on the Workspace, rename it to `Pathfinding Script` and add the following code:

```lua
     -- Continuously calculating
     while true do
     	-- Create the path object
     	path = game:GetService("PathfindingService"):CreatePath()
     
     	-- Compute the path
     	path:ComputeAsync(workspace.Egg.Position, workspace.Nest.Position)
     
     	-- Get the path waypoints
     	waypoints = path:GetWaypoints()
     
     	-- Clear the placed waypoints
     	game.Workspace.Waypoints:ClearAllChildren()
     
     	-- For each waypoint
     	for _, waypoint in pairs(waypoints) do
     		part = Instance.new("Part")
     		part.Shape = "Ball"
     		part.Material = "Neon"
     		part.Size = Vector3.new(0.6, 0.6, 0.6)
     		part.Position = waypoint.Position
     		part.Anchored = true
     		part.CanCollide = false
     		part.Parent = game.Workspace.Waypoints
     		wait(0.5)
     	end
     end
```

In this script, we first refer to the pathfinding service. Then, we use `ComputeAsync` to compute the path from the egg's position to the nest's position. This will generate a set of points from the egg to the nest, and we can get it by using `GetWaypoints`. After that, for every waypoint, we can spawn a small glowing ball to basically dot the line.

Congratulations! Your Egg and Nest are finished. Push it around and try to score!

### Follow Up
1. Add a surrounding pen so the Egg doesn't roll away.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Egg%20Saver/5b6b6916-6190-4bd7-805c-86274c8b697c.png)

2. You can use Meshes to make the objects look more like an egg and nest respectively. Feel free to use the Toolbox for this.

![image-20230508231831001](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Egg%20Saver/9b9fc7f3-06c7-46fc-9101-c612bbba65c3.png)

3. Add decorations!

![image-20230512164927553](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Egg%20Saver/f869945e-f076-4e78-abae-3ac3c8315f86.png)