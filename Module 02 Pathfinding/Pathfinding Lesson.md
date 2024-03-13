## Lesson: Pathfinding

In this project you will create a basic NPC that can patrol between a pre-defined set of points continuously.

### Topics:

  - Pathfinding

### Setting up the Project

1. First let's set up the NPC. 'Navigate to the 'Avatar' tab and press 'Rig Builder'.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Pathfinding%20Lesson/2d564087-bf51-4ff3-bddc-bd26a6ccd6bf.png)

2. In the pop-up window, select your desired rig for your NPC from the options.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Pathfinding%20Lesson/c3e94018-c46a-4110-b4cc-17712ec25516.png)

3. Now create several parts around your level to act as the NPC's patrol points. Size and color them however you wish.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Pathfinding%20Lesson/af0eada6-d05b-4f98-bd88-0e9414a95f6d.png)

4. Now rename the patrol points you just created so that they are ordered, such as goal1, goal2, goal3, etc.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Pathfinding%20Lesson/4b020258-7a1e-4687-b960-5a40ffc8fc0a.png)

5. Lastly, feel free to create some geometry around and between your goal points to make the patrol more interesting and dynamic.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Pathfinding%20Lesson/1df0cdaa-d648-4ddc-8789-a11c35fd4d1c.png)

### The Script

Now we will create a script that programs our NPC to move between the patrol points you defined. Hit the plus sign next to the rig you just made and add a script. Rename it to 'NPCMoveScript'.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2002%20Pathfinding/Pathfinding%20Lesson/23061872-f9de-4c93-96c4-55dbaded704a.png)

Now open up the script so we can begin coding.

Step 1. First we need to create a list variable (also called an array) to hold references to all the patrol points we created. Lists are created the same way you make a variable, but instead you enclose all the values you want it to have in a pair of curly braces {} and make sure that each element of the list is separated by a comma.

```lua
    -- Create a list with the goals stored inside
    -- NPC's will follow them in chronological order and repeats
    goals = {
                workspace.goal1, -- goals[1]
                workspace.goal2, -- goals[2]
                workspace.goal3, -- goals[3]
                workspace.goal4, -- goals[4]
                workspace.goal5  -- goals[5]
            }
```

Step 2. Now we'll need some generic variables. Let's create one called 'NPC' which simply holds a reference to the NPC model that this script is attached to. Then we'll need a reference to the NPC's humanoid.

```lua
    -- Variables for the NPC, its humanoid, and its destination (the current 'goal' part that its moving to)
    local NPC = script.Parent
    local humanoid = NPC.Humanoid
    local destination = 1
```

Step 3. Next, we'll need to create several variables that handle the NPC's movement logic. First make a path variable from Roblox's pathfinding service that will calculate paths for us. Then create a variable called destination, which will be our marker for what patrol point the NPC is currently moving toward. Then create some waypoint variables that will keep track of the waypoints as the NPC traverses through them.

```lua
    -- Create the path object
    local path = game:GetService("PathfindingService"):CreatePath()

    -- Variables to store destination part, waypoints table and NPC's current waypoint
    local waypoints
    local currentWaypointIndex
```

Step 4. Now let's create the function to calculate a path between the NPC and its next goal part! The function takes in a variable (called objectRootPart) that refers to the goal part that we wish to create a path toward. This function will:

    1. Compute a path from the NPC's root to the target part.
    2. Empty the waypoints list
    3. Check if the path calculated successfully, and if it did:
        - setup the waypoints, set the waypoint index to the first index, then instruct the humanoid to move to it
        or if the path did not calculate successfully, then:
        - instruct the humanoid to move to itself (basically telling it to stand still)

```lua
    local function followPath(objectRootPart)
        
        -- Compute and check the path
        path:ComputeAsync(NPC.HumanoidRootPart.Position, objectRootPart.Position)
        -- Empty waypoints table after each new path computation
        waypoints = {}
        
        if path.Status == Enum.PathStatus.Success then
            -- Get the path waypoints and start NPC movement
            waypoints = path:GetWaypoints()
            -- Move to first waypoint
            currentWaypointIndex = 1
            humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
            
        else
            -- Error (path not found); stop humanoid
            humanoid:MoveTo(NPC.HumanoidRootPart.Position)
        end
    end
```

Step 5. Next we define the 'MoveToFinished' event which triggers as soon as the NPC reaches its desired waypoint. It has one parameter called 'reached' which is 'true' if the waypoint was successfully reached, and 'false' if not. In this function, we will:

    1. Check if we reached the waypoint and if there are still more to travel, and if so:
        - set the waypoint index to be the next index
        - check if the next waypoint requires us to jump, and if so, trigger the jump variable on the humanoid
        - finally, instruct the humanoid to move to the next waypoint
        or if the waypoint was not reached or the NPC traveled through all the waypoints, then:
        - Check if the value of destination is the last index of our list of goal parts, and if so, set it back to 1 (refering to the very first goal part in our list)
        - If destination is not the last goal part, simply set it to be the next index
        - Finally, instruct the NPC to calculate a path to its new destination using the function we created earlier 'followPath'

```lua
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
        else
            -- If destination is at the end, we reset back to the first goal
            -- Else, we continue onto the next goal
            if destination == #goals then -- #goal means the number of objects instead the table
                destination = 1
            else
                destination = destination + 1
            end
            
            -- Once the goal is reached and the destination is changed
            -- We call this function to restart the process
            followPath(goals[destination])
        end
    end)
```

Step 6. Now all we need to do is define one more event called 'Blocked' which triggers whenever the game detects that the NPC's path is obstructed. We first check if the blocked waypoint is ahead of us (if it is behind us, it won't matter since we already passed it), and if so call the 'followPath' to re-compute a new path.

```lua
    -- A path object has an event called Blocked
    -- Inputs an integer parameter of the blocked Waypoint index 
    path.Blocked:Connect(function(blockedWaypointIndex)
        
        -- Check if the obstacle is further down the path
        if blockedWaypointIndex > currentWaypointIndex then
            -- Call function to re-compute the path
            followPath(goals[destination])
        end
    end)
```

Step 7. Finally, we create a single call to 'followPath' at the end of our code to start the infinte chain of calculate path -> path reached -> calculate path -> path reached -> calculate path, etc.

```lua
    -- Call this function once to start the NPC movement
    followPath((goals[destination]))
```

### Follow up

For an additional challenge, create code that will program the NPC to check if it detects a player nearby after it has reached a goal part, and to follow that player instead of the next destination. In the next lesson, we will take a look at how to make an NPC chase the player instead, so you could take some inspiration from there.
