## Project: Stationary Turret

Creating a turret that shoots if a humanoid object appears in front of it.

We will be utilizing the following topics:

  - Raycasting
  - RunService
  - Physics

### Making the Turret Model

1. First you need to create the turret. Start off with the legs, you could have 3 legs similar to a tripod, or one thick leg that the turret would be standing on.
2. Add the center for the turret, a base to serve the turret and it should be standing on the legs.
3. Add some lights or accessories to the turret to make it look unique.
4. Create a barrel that the turret would shoot the bullets out of, it should be attached to the center of the turret.

![](https://drive.google.com/uc?export=view&id=1TNjz_iDLPYvu8U4WBLeUZu63uV-5F9FS)

5. Insert an attachment at the tip of the barrel. Name this "RayStart."

![](https://drive.google.com/uc?export=view&id=1URaI6PJxwx_6kcyGtGWtZLI7kHw0xgEU)

6. Name the barrel with the attachment "ShootPart".
7. Inside the attachment "RayStart", create a point light.
8. Make sure that all the related parts of the turret are anchored and grouped in a Model called "Turret".
9. Create a script inside the Turret model.

### Making the Bullet Model

1. For the turret to shoot, it needs to shoot something. Create a cylindrical part slightly smaller than the width of the turret barrel.
2. Set the material of the bullet to neon and the color to whichever color you prefer.

![](https://drive.google.com/uc?export=view&id=1-OXzmb3KVonWeXmSaifl_fNZPXOjA8eg)

3. Set the bullets CanCollide and Anchored to false.
4. Name the bullet "Bullet" and put the bullet part inside of ServerStorage.

### Making the Script
```lua
local runService = game:GetService("RunService")

local turret = script.Parent
local shootPart = turret.ShootPart
local rayStart = shootPart.RayStart

local rayOrigin = rayStart.WorldPosition
local direction = (rayStart.WorldPosition - shootPart.Position).unit

local cooldown = false

runService.Stepped:Connect(function() --This can be replaced with an infinite while loop, however this is highly recommended 
	local raycastResult = workspace:Raycast(rayOrigin, direction * 1000)
	
	if raycastResult then
		if raycastResult.Instance and raycastResult.Instance.Parent:FindFirstChild("Humanoid") then
			local humanoid = raycastResult.Instance.Parent:FindFirstChild("Humanoid")
			Shoot(humanoid, raycastResult.Position)
		end
	end
end)
```
The script uses RunService, an event which works similarly to a while loop.
- Inside the loop, during each iteration a raycast is casted from the attachment to the direction in which the turret should be facing.
  - To get the direction of the raycast, you could get the .unit vector of 2 subtracted positions from the turret, to get the real direction that it is facting.
  - Multiply the direction by how far you want the raycast to shoot.
  - If the raycast hits a model which has a humanoid, then the Turret shoots using a Shoot function.
The reason we use a while loop is because if we used a while loop, every time we called the shoot function,
the more wait() methods there are in the function, the more the script would have to wait before the next iteration happens.
However, the Rendered() function of runService is like a world event which executes after every frame has been rendered,
so it is more of a while loop event rather than a generic while loop, allowing the script to execute the Shoot function every frame if need be.

```lua
local function Shoot(humanoid, position)
	if cooldown then
		return
	end
	cooldown = true
	
	local bullet = game.ServerStorage.Bullet:Clone()
	bullet.Position = shootPart.Position
	
	local bv = Instance.new("BodyVelocity")
	bv.MaxForce = Vector3.new(math.huge, math.huge, math.huge)
	bv.Velocity = direction * 500
	bv.Parent = bullet
	bullet.Parent = game.Workspace
	
	local sound = Instance.new("Sound")
	sound.SoundId = "rbxassetid://9114727096"
	sound.Parent = shootPart
	sound:Play()
	
	rayStart.PointLight.Enabled = true
	wait(0.1)
	cooldown = false
	rayStart.PointLight.Enabled = false
	humanoid:TakeDamage(10)
	
	wait(2)
	bullet:Destroy()
end
```
- In the Shoot function, we pass the humanoid that we detected in the loop.
- The script should have a cooldown variable so that the Turret can't shoot every frame.
  - The shoot function clones the Bullet that we created from ServerStorage.
  - Creates a new instance of BodyVelocity and set the velocity according to what the bullets speed should be, and set the parent of BodyVelocity to the clone of the bullet.
  - Enable the point light of the attachment so that every time the turret shoots, some light appears at the tip of the barrel.
  - Find a gunshot sound id in the toolbox, and create a new instance of that sound and play it every time the turret shoots.
  - After a few seconds, destroy the bullet so the game will not create an infinite amount of bullet clones.

### Challenge Steps

- Create particle effects for when the gun shoots, besides the light you could have some smoke or some sparks come out after each gunshot.
- Create a lazer that turns off whenever a humanoid object steps out of it, or even more advanced to have the lazer stop at the position which the raycast hits.