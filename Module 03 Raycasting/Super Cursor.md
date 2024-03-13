## Project: Super Cursor

Granting your cursor the ability to mess with in-game objects and changing the cursors icon.

We will be utilizing the following topics:
  - Mouse
  - RunService
  - Physics
  - Camera
  - Server Events

### Making the Prerequisites
1. In your game, create a few parts and scatter them wherever you feel like, these parts can be any shape.
2. Name all the parts you created "Interactable".
3. Inside of ReplicatedStorage, create a new RemoteEvent and name it "SuperClick".

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2003%20Raycasting/Super%20Cursor/900d66fa-ff61-4b41-8b83-2e309e60439b.png)

### Making the Local Script
- In the explorer, create a new local script inside of StarterPlayerScripts which is located inside of StarterPlayer.
- Making the script:
```lua
local runService = game:GetService("RunService")

local player = game.Players.LocalPlayer
local mouse = player:GetMouse()

local normalIcon = "rbxasset://SystemCursors/Arrow"
local targetIcon = "rbxassetid://12057597405"
```
- First, initialize all the variables that you will need.
  - You need to initialize the player, and that players mouse.
  - You should also create variables that will hold the normal cursors icon and the second cursors icon. You can find a cursor that you like in the toolbox.

```lua
runService.RenderStepped:Connect(function()
	if mouse.Target and mouse.Target.Parent then
		local target = mouse.Target
		if target.Name == "Interactable" then
			mouse.Icon = targetIcon
		else
			mouse.Icon = normalIcon
		end
	else
		mouse.Icon = normalIcon
	end
end)
```
- To check if the mouse is hovering over the right target that it can interact with, we use a loop event which is fired every frame.
  - Inside the loop we check if the mouse is hovering over anything at all, and if it is then we check if the thing that it is hovering over is the right object.
  - To specify and be able to check that the mouse is hovering over the right target, we name every object that the mouse can interact with as "Interactable" and then check the targets name.
  - If it is hovering over the interactable target, we set the mouses icon to its seconady icon.
  - If it isn't hovering over the interactable target, or if it isn't hovering over anything at all, then we set the cursor to its normal icon.

```lua
mouse.Button1Down:Connect(function()
	if mouse.Target and mouse.Target.Parent then
		local target = mouse.Target
		if target.Name == "Interactable" then
			local cameraPosition = game:GetService("Workspace").CurrentCamera.CFrame.Position
			local mousePosition = mouse.Hit.Position
			local direction = (mousePosition - cameraPosition).unit
			game.ReplicatedStorage.SuperClick:FireServer(direction, target)
		end
	end
end)
```
- Whenever the player clicks the mouse while on the Interactable object, we want the object to do something.
- To check when the player clicked the mouse we use the mouses Button1Down event.
  - In here, we once again check for the target in the same way that we checked it in the RunService event.
  - If the mouse is hovering over the Interactable object we use the previously created ServerEvent "SuperClick" to tell the server what to do with the object.
  - As a super cursor, we want to fling the Interactable object that we clicked on. To do so, we have to pass a few arguments to the SuperClick event:
    - The direction that the camera is looking at based on the mouse position.
    - The target that we want to fling.

### Making the Server Script
- ServerEvents can only be fired through server scripts, create a new script inside of ServerScriptService.
- Making the script:
```lua
game.ReplicatedStorage.SuperClick.OnServerEvent:Connect(function(player, direction, target)
	local bodyForce = Instance.new("BodyForce")
	bodyForce.Force = direction * 100000 --The force at which the object will be launched with
	bodyForce.Parent = target
	wait(0.1)
	bodyForce:Destroy()
end)
```
- When the player has clicked on the Interactable object, the client fires an event which will be activated in this script.
- In our scenario, we want to fling the Interactable object that we clicked on based on where the camera is looking at the object.
  - Create a new Instance of a BodyForce object.
  - Set that the Force of the BodyForce to the direction that we passed from the client, and multiply it by the amount of force we want to fling it with.
  - Set the parent of the BodyForce object to the target.
  - We only want to fling the object momentarily, so wait a few seconds and then destroy the BodyForce object in the target.

### Challenge Steps
- Create your own Interactable action, just now we created a flinging action, you could program a different object to change colors for example.
- Add some effects, you could add a noise whenever an Interactable object is pressed. You can also createa a custom room full of Interactable objects.