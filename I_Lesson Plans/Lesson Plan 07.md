
# Lesson 7: Protective A.I. Companion (Part 2)

Let's learn how to improve our protective A.I. companion! We will make another mode for healing the player, and if it is with the player, we will allow it to slowly regenerate the player’s health back.

We will be utilizing the following topics:

- Scripts

- Values

  

## Letting Companions Regenerate the Player

How do we want the companion to heal?

- It should only regenerate the player's health only when it is following them.

- The regeneration should occur every few seconds.

- If the companion is attacking an enemy, we want it to stop regenerating health until it returns to the player.

  

1.  Click the + button next to the companion's Config (red in images), and add the following values:
    
    - One BoolValue named `Heal`. We will be using this to toggle healer mode.
    
      ![image](https://user-images.githubusercontent.com/28936305/230853400-57907804-c57b-473c-8168-d6e3bbec46c8.png)
    
    - Two IntValues called `healPower` and `healDelay`, respectively. These will allow for easy configuration. For now, set `healPower` to 10 and `healDelay` to 2.
    
      ![image](https://user-images.githubusercontent.com/28936305/230853417-9ca52d36-d9b4-4e19-95dd-e25e87eff758.png)
    
    - One ObjectValue called `PlayerCharacterObject`. This will store Player.Character after getPlayerFromName( ) in CompanionMoveScript returns the object. It will save us scripting time and space since we can call the function once.
    
      ![image](https://user-images.githubusercontent.com/28936305/230853443-16217727-cbef-463f-b3dc-ea93520117d6.png)
    
    - Make sure you see this under Config:
    
      ![image](https://user-images.githubusercontent.com/28936305/230853470-d142741b-d24b-4ad6-8af1-b647818328e1.png)

2. To save us from cluttering the CompanionMoveScript with more lines, let's create a new script just for healing. Click the + button next to Companion, add a script (red in image), and rename it to `HealScript`.

   ![image](https://user-images.githubusercontent.com/28936305/230853500-4e47e28b-6bd6-468f-b241-4c6858cd3f1e.png)

3. Open up `HealScript`, and add this code: 
   ```lua
   local leader = nil
   local healPower
   local healDelay
   local config = script.Parent.Config
   
   -- Wait until the Player's Character is found through the CompanionMoveScript.
   repeat
   	wait(0.1)
   	leader = config.PlayerCharacterObject.Value
   	healPower = config.healPower.Value
   	healDelay = config.healDelay.Value
   until (leader ~= nil) and (healPower ~= nil) and (healDelay ~= nil)
   
   -- The wait will prevent the Player from being instantly healed.
   while wait(healDelay) do
   	if config.Heal.Value == true then
   		leader.Humanoid.Health = leader.Humanoid.Health + healPower
   	end
   end
   ```

4. All we need to do now is add a few lines in `CompanionMoveScript`. Open it up, and we will assign it to the PlayerCharacterObject we created. Add this code:

   ```lua
   -- START UP
   
   repeat -- Repeat until we find a target
   	wait(0.1)
   	leaderName = config.Leader.Value
   	detectionRange = config.detectionRange.Value
   	gapRange = config.gapRange.Value
   until (leaderName ~= nil) and (detectionRange ~= nil) and (gapRange ~= nil)
   
   leader = getPlayerFromName(leaderName)
   config.PlayerCharacterObject.Value = leader
   destination = leader.HumanoidRootPart
   
   followPath(destination) -- Call this function once to start the forever change
   ```

5. Lastly, in the onWaypointReached function else statement, we will add an if-else statement to flip Heal on or off. If the destination is the leader, then Heal will be true, else it will be false. Replace the function with this new code:

   ```lua
   local function onWaypointReached(reached)
   	
   	if reached and not attack and (currentWaypointIndex < #waypoints) and (maxDist < #waypoints) then -- Calculate a gap when following player and not attacking.
   		currentWaypointIndex = currentWaypointIndex + 1
   		maxDist = currentWaypointIndex + gapRange
   		
   		if waypoints[currentWaypointIndex].Action.Value == 1 then 	-- We want the humanoid to Jump ahead of time, so after
   			humanoid.Jump = true									-- the currentWaypointIndex increased by, we check to see if 
   		end															-- the Action is Jump.
   		
   		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
   		
   	elseif reached and attack and (currentWaypointIndex < #waypoints) then -- When attacking. No gap in order to touch zombies.
   		currentWaypointIndex = currentWaypointIndex + 1
   		maxDist = currentWaypointIndex + gapRange
   
   		if waypoints[currentWaypointIndex].Action.Value == 1 then
   			humanoid.Jump = true
   		end
   		
   		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
   	else
   		destination = findNearest()
   		
   		if destination == leader.HumanoidRootPart then
   			config.Heal.Value = true
   		else
   			config.Heal.Value = false
   		end
   		
   		followPath(destination)
   	end
   end
   ```

Congratulations—your A.I. companion is now improved! Click play to test out its new functions!

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.

2.  For this class, remember to always have them publish their script on to Roblox. We will be grabbing them again and again for future lessons.

3.  Solution: https://bit.ly/roblox3_7_2
