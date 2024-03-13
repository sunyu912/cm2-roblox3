## Mini Project: NPC Patrolling

In this project, you will create a moving NPC (short for Non-playable character)! You will add 3 goals the NPC will walk between in an infinite loop. The NPC will be scripted and use the pathfinding service to be able to walk between said goals.

### Topics:

  - Parts
  - Material
  - BrickColor
  - Scripting



### Setting up the Project

Just like my dog!

1. Get 3 cylinders and make them flat against the ground. Add BrickColor and Material.

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/NPC%20Patrolling/ed20571e-9ee2-4361-9274-b2a1da0d3cae.png)

   

2. Rename them to `goal1`, `goal2` and `goal3`. 

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/NPC%20Patrolling/4dacb332-ffa1-4b5b-8371-270b4b85661c.png)

3. Get a Rig from the "AVATAR" Tab and "Rig Builder", then select any of the options from the middle of the screen. For this example, the "Block Avatar" was selected. 

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/NPC%20Patrolling/47afd85d-4c1b-4ff7-b4df-60ed3003273a.png)

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/NPC%20Patrolling/1acdcf45-fca8-41d3-ae33-caa6c4a9bc50.png)

### The Script

1. Add a script onto the Rig and rename it to `NPCMoveScript`. You can also download it via Roblox from [here](http://bit.ly/roblox3_3_npcmovescript).

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/NPC%20Patrolling/54c8f414-a99a-4e7b-a089-dcc2ab8cb422.png)

2. Script the Movement Script (unless you downloaded it from the previous step)

   ```lua
   -- Create a list with the goals stored inside
   -- NPC's will follow them in chronological order and repeats
   goals = {
   			workspace.goal1, -- goals[1]
   			workspace.goal2, -- goals[2]
   			workspace.goal3, -- goals[3]
   		}
   
   -- Variables for the NPC, its humanoid, and its destination
   local NPC = script.Parent
   local humanoid = NPC.Humanoid
   local destination = 1
   
   -- Create the path object
   local path = game:GetService("PathfindingService"):CreatePath()
   
   -- Variables to sore waypoints table and zombie's current waypoint
   local waypoints
   local currentWaypointIndex
   
   local function followPath(objectRootPart)
   	
   	--Computer and check the path
   	path:ComputeAsync(NPC.HumanoidRootPart.Position, objectRootPart.Position)
   	-- Empty the waypoints table after each new path computation
   	waypoints = {}
   	
   	if path.Status == Enum.PathStatus.Success then
   		-- Get the path waypoints and start zombie walking
   		waypoints = path:GetWaypoints()
   		-- Move to the 1st waypoint
   		currentWaypointIndex = 1
   		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
   		
   	else
   		-- Error (path not found); stop humanoid
   		humanoid:MoveTo(NPC.HumanoidRootPart.Position)
   	end
   end
   
   -- A humanoid object has an event called MoveToFinished
   -- Inputs a boolean parameter determining whether humanoid reached goal before 8 sec timeout.
   humanoid.MoveToFinished:Connect(function(reached)
   	-- If a waypoint is reached and there is still more waypoints to go...
   	if reached and currentWaypointIndex < #waypoints then
   		currentWaypointIndex = currentWaypointIndex + 1
   		
   		-- We want the humanoid to Jump ahead of time, so after
   		-- the current waypointindex increased by, we check to see
   		-- if the Action is Jump
   		if waypoints[currentWaypointIndex].Action.Value == 1 then
   			humanoid.Jump = true
   		end
   		
   		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
   	else
   		-- If destination is at the end, we reset back to the first
   		-- Else, we continue onto the next goal
   		if destination == #goals then
   			destination = 1
   		else
   			destination = destination + 1
   		end
   		
   		-- Once the goal is reached and the destination
   		-- We call this function to restart the process
   		followPath(goals[destination])
   	end
   end)
   
   path.Blocked:Connect(function(blockedWaypointIndex)
   	--Check if the obstacle is further down the path
   	if blockedWaypointIndex > currentWaypointIndex then
   		-- Call function to re-compute the path
   		followPath(goals[destination])
   	end
   end)
   
   -- Call this function once to start the whole process
   followPath((goals[destination]))
   ```

   In this script, we first get the goals in the workspace for the Rig/NPC to follow. Then, we get a Pathfinder and make a function (code block) so the NPC can follow the goals. We then code another function that makes sure the NPC keeps moving until it gets to the current goal it walks to. Finally, one last function to check that the path is not blocked, and if it is, skip the blocked goal.

3. Congratulations! Your Patrolling NPC is finished. Play the game and look at it go!

### Follow Up

1. Decorate your Rig. Feel free to rename it, add images on it and change their colors.

   ![image-20230512164927553](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/NPC%20Patrolling/34554235-eef2-4e25-ac05-d6c9d0fef433.png)

1. Add decorations!


![image-20230512164927553](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/NPC%20Patrolling/855cfb0f-66b0-4b32-a1d7-4a5fb4c255d8.png)
