## Mini Project: Item Fetcher

In this project, you will create an NPC (stand for Non-Playable Character) that fetches items with basic AI (short for Artificial Intelligence)! You will create an item of choice to retrieve infinitely. The character will be scripted and use the pathfinding service to walk towards the items it wishes to retrieve.

### Topics:

  - Parts
  - Material
  - BrickColor
  - Scripting



### Setting up the Project

Just like my dog!

1. Get 1 sphere. Add BrickColor and Material. Then rename it to `orb`.

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/4b6a5e21-716c-4df6-9c7c-e77a505739ce.png)

   

3. Get a Rig from the "AVATAR" Tab and "Rig Builder", then select any of the options from the middle of the screen. For this example, the "Block Avatar" was selected. 

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/bbc6f45a-9cfe-4adc-a769-007f14cef1ce.png)

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/e6507718-2eae-45ee-a457-f83c771b2934.png)

### The Script

1. Add a script onto the Rig and rename it to `NPCFetchScript`.

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/9c4ba4b1-d560-41d0-ae31-687c5e5efcb9.png)

2. Script the Fetch Script

   ```lua
   --You can change the name of orb to whatever part you wish to search for named that way.
   item_searched = "orb"
   
   -- Variables for the NPC, its humanoid, and its destination
   local NPC = script.Parent
   local humanoid = NPC.Humanoid
   local destination = 1
   
   -- Create the path object
   local path = game:GetService("PathfindingService"):CreatePath()
   
   -- Variables to sore waypoints table and zombie's current waypoint
   local waypoints
   local currentWaypointIndex
   
   local function searchForObject()
   	-- Search for all objects in the game until we find one with the searched name
   	for _, child in pairs(workspace:GetDescendants()) do
   		if child.Name == item_searched then
   			return child
   		end
   	end
   	-- If the object isn't found tell it to follow itself (stay in place)
   	return script.Parent.HumanoidRootPart
   end
   
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
   		-- Search for the object we want the NPC to look for
   		local object_to_follow = searchForObject()
   		
   		-- Once the goal is reached and the destination
   		-- We call this function to restart the process
   		followPath(object_to_follow)
   	end
   end)
   
   path.Blocked:Connect(function(blockedWaypointIndex)
   	--Check if the obstacle is further down the path
   	if blockedWaypointIndex > currentWaypointIndex then
   		-- Call function to re-compute the path
   		followPath(searchForObject())
   	end
   end)
   
   -- Call this function once to start the whole process
   followPath(searchForObject())
   ```

   In this script, we first set a variable that will be the name of objects the script looks for in the world (note this will work only for parts named that and if they are not inside of a Model/Tool/etc.) Then, we make a searcher which looks through all the parts in the game named the same way as the variable we mentioned before (in this case "orb"). After, we get a Pathfinder and make a function (code block) so the NPC can go to the part it wishes to retrieve. We then code another function that makes sure the NPC keeps moving until it gets to the current part it walks to. Finally, one last function to check that the path is not blocked, and if it is, skip the blocked part.

3. Add a script onto the orb object and rename it to `FetchScript`.

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/6ea7f0bf-4819-4421-9685-72d2992ebe23.png)

4. Script the Fetch Script

   ```lua
   script.Parent.Touched:Connect(function(hit)
   	if hit and hit.Parent:FindFirstChild("Humanoid") then
   		script.Parent:Destroy()
   	end
   end)
   ```

   In this script, it checks if a Humanoid touches the item, if so, it destroys it. This way, the `NPCFetchScript` can search for other parts to fetch. Keep in mind players can also destroy it since they have a Humanoid too!

5. Congratulations! Your Item Fetcher is finished. Play the game and look at it go!

### Follow Up

1. Decorate your Rig. Feel free to rename it, add images on it and change their colors. 

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/93a868a5-dfbc-4a8a-b2f4-ee3ca8d74b86.png)

1. Change how the `orb` looks to a theme of your choice and make many clones around the map for the NPC to fetch!

   ![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/96a490be-7d07-4065-8901-258e6a9859f0.png)

1. Decorate the world!


![image-20230523210644516](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Item%20Fetcher/3b02ddfd-d8b8-4443-a217-6b0e76d162f3.png)
