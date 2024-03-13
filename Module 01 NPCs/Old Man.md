## Project: Old Man

Making an Old Man character rig and making it talk in the game.

We will be utilizing the following topics:

  - Creating Humanoid Characters
  - Chat Service

### Making the Model

1. Go into play mode in Studio.
2. Locate the Workspace while in Play Mode. It has an Earth icon. Expand it.
3. Locate the model in the Workspace with your username in it. Copy this model. If you can't find it, you're probably not in Play Mode.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Old%20Man/36d69934-5398-4fc0-8b5c-4c5693094b0d.png)

4. Stop play mode, and paste it into the Workspace.
5. Find a hat you would like your character to have in Roblox marketplace.
6. Go to that hat's page and look at the link to the webpage, copy the hat ID. This is the number in the link.
7. Run this command in the console in Studio: "game:GetService("InsertService"):LoadAsset(id).Parent = game.Workspace" where id is the numbers you copied to the hat. If it doesn't work, then try another hat.
8. The hat should be imported as a model. If you expand it, you should see the hat itself with a little wizard hat icon. Drag this asset into your character model and it should automatically be positioned as if its wearing it as a hat.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Old%20Man/250654e3-a3d2-4b70-8ab3-50946129d381.png)

9. You might already be wearing a hat, so the new one that you just put on might intersect with it. In that case, you can open your player model and remove the hat that you don't want anymore.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Old%20Man/51aec18f-38f6-4456-823b-876c2cbf16cc.png)

10. You now need to pose your character. With your character model expanded in the Explorer, you can select each individual limb and move and rotate it. Do this until you reach your desired pose. Be patient!

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Old%20Man/ceff3fdb-788f-4ad6-bc6f-dcbad21ac529.png)

You could additionally build a bench or a chair for your character to sit in. Or you could make something else; be creative!

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Old%20Man/2f9d57e0-1d04-4e0b-aac8-16d5eb5633ec.png)
![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Old%20Man/883d0f15-d6bf-40b9-ae2b-89b7591334b6.png)

11. Inside the head of the rig, create a script.

### Making the Script
```lua
local cs = game:GetService("Chat")

local part = script.Parent
local oldManLines = {"What a beautiful day it is.", "I'm lost walking on the freeway.", "I can't hear you speak up!", "Achoo!", "Good morning!"}

while wait(5) do
	cs:Chat(part, oldManLines[math.random(1, #oldManLines)], "Red")
end
```
The script uses an array of phrases that the Old Man would say.
The script runs in a while loop:
- Each iteration grabs a random text line that the Old Man says from the array.
- The script uses Chat game service to call the Chat function to create a chat bubble above the Old Mans head.
- The chat bubble should contain the random line from the array.

### Challenge Steps

An added challenge to the Old Man is to animate the Old Man doing some idle pose like breathing or moving legs/arms in some idle fashion.
Another thing that could make the Old Man more interactable is to add a sound queue to some lines that the Old Man says, for example *Cough*.