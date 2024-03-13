## Project: Maze Solver

In this project you will create an maze solving A.I. that will automatically calculate the shortest path to its destination and follow it.

### Topics:

  - Pathfinding

### Setting up the Project

1. Navigate to the 'Avatar' tab and press 'Rig Builder'.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Maze%20Solver/8f8b4604-560b-4e49-abc7-981363182952.png)

2. In the pop-up window, select your desired rig for your maze solver A.I. from the options.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Maze%20Solver/dd2b80fe-cdf7-49a7-b99d-111d69643166.png)

3. Now that you have a character model, click the plus sign next to it and add a script. Rename it to "MazeSolverScript".

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Maze%20Solver/626d0ea5-df48-4166-b305-8b46c8933856.png)

4. Now create your very own maze, or look through the toolbox to find a maze you would like to test out your A.I. with. Also be sure to enclose your A.I. character at the start of the maze (highlighted in red) so that the A.I. will not try to cheat by going around the maze. Remember: Roblox's pathfinding system will always try to find the shortest path to the target!

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Maze%20Solver/dd737614-934f-47cf-9773-2c0e340bb037.png)

5. Lastly, create a part at the end of the maze and rename it to "goal". We will use this part to tell the pathfinding system where to navigate to inside our script.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Maze%20Solver/a9ceda45-be61-4f7c-b820-71c6b6fca097.png)

### The Script

Inside of our MazeSolverScript, we will need to make a reference variable to our goal part and then integrate Roblox's pathfinding service to calculate a series of waypoints to our target location. We will need to set up a few functions to do so.

Open the script we added to our NPC model and add the following code.

```lua
    local goal = workspace.goal -- Create a variable the goal the NPC should attempt to reach

    -- Variables for the NPC, its humanoid
    local NPC = script.Parent
    local humanoid = NPC.Humanoid

    -- Create the path object
    local path = game:GetService("PathfindingService"):CreatePath()
    
    -- Variables to store waypoints table and zombie's current waypoint
    local waypoints
    local currentWaypointIndex
    
    local function followPath(objectRootPart)
        
        -- Compute and check the path
        path:ComputeAsync(NPC.HumanoidRootPart.Position, objectRootPart.Position)
        -- Empty waypoints table after each new path computation
        waypoints = {}
        
        if path.Status == Enum.PathStatus.Success then
            -- Get the path waypoints and start zombie walking
            waypoints = path:GetWaypoints()
            -- Move to first waypoint
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
            -- the currentWaypointIndex increased by, we check to see if 
            -- the Action is Jump.
            if waypoints[currentWaypointIndex].Action.Value == 1 then
                humanoid.Jump = true
            end
            
            humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
        end
        
    end)

    -- A path object has an event called Blocked
    -- Inputs an integer parameter of the blocked Waypoint index 
    path.Blocked:Connect(function(blockedWaypointIndex)
        
        -- Check if the obstacle is further down the path
        if blockedWaypointIndex > currentWaypointIndex then
            -- Call function to re-compute the path
            followPath(goal)
        end
    end)
    
    followPath(goal)
```

### Follow up

For an additional challenge, change your script so that it will try to reach other kinds of goals, such as your player. How would you change the logic so that the pathfinding system targets your player model instead of the goal part?
