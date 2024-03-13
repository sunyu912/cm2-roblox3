## Project: Quest Giver

In this project you will create an NPC that gives the player a simple quest to find and retrieve a lost dog, and will give the player a reward upon completion.

### Topics:

  - Dialog System

### Setting up the Project

1. Navigate to the 'Avatar' tab and press 'Rig Builder'.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/0cf88601-644f-42c4-8d3c-e0eb7a034b21.png)

2. In the pop-up window, select your desired rig for your NPC from the options.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/4d175b2f-8fcb-433f-b1b8-bc819cccbaa2.png)

3. Be sure to rename the rig to 'NPC' or whatever name you'd like. We will be using its name to find it later in our code.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/1bded967-fdc7-412b-a746-b2d29236a629.png)

4. Next, let's import the dog model that will be required for the player to find and turn in to the NPC. You can find a free dog tool at [this link](https://www.roblox.com/library/13913148143/Dog-Tool).

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/6172d897-0e53-4e8d-8e6b-497319548b23.png)

5. Press the "Get" button to add it to your inventory. Then, in Roblox Studio, click on the Inventory tab in your Toolbox. The Dog Tool should appear there, and you can drag it into your workspace.

6. After importing the model, place it inside replicated storage so that we can store it for later use from our script.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/fe7394b7-ab78-4697-be61-3fdb383a8912.png)

7. Now we must import some kind of reward item for the NPC to give to the player upon quest completion. You can use any tool you'd like from the toolbox. Roblox offers a basic sword tool that you can find [here](https://create.roblox.com/marketplace/asset/47433/Sword), or you can simply search "sword" in the toolbox and select the first option.

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/5480d8ab-2423-4d7c-a50b-2ba2af772868.png)

8. Finally, just as we did with the dog model, place the reward item in replicated storage so we can use it later from our script. If it asks you to place it in the StarterPack, select No. Rename it to "CoolSword."

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/82a6cb5d-4b4e-4cf3-bb3b-4cdc17889136.png)

### The Script

We will create all our quest system code inside a local script, as dialog choice selection events can only be detected locally on the player's machine. Let's first create a local script inside "StarterPlayerScripts" that can be found in the "StarterPlayer" folder. Rename the script to "DialogueScript".

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Module%2001%20NPCs/Quest%20Giver/02c95ae6-a68b-49fa-8d9c-c71213b34029.png)

Now place the following code within your newly created local script. Feel free to change the dialog options or even add more to customize your own kind of quest!

```lua
local Players = game:GetService("Players")
local NPC = workspace.NPC
local dogTool = game.ReplicatedStorage.dog
local swordTool = game.ReplicatedStorage.CoolSword -- This will be the reward for completing the quest, you can change it to anything you'd like

local Dialog = Instance.new("Dialog") -- Creates a dialog system object which lets use create various dialog prompts and responses with our NPC
Dialog.Parent = NPC:WaitForChild("Head") --Parent it with the NPC's head so that his dialog will appear above him
Dialog.InitialPrompt = "Hey you! I lost my dog. Can you help me find him?"
Dialog.GoodbyeChoiceActive = true -- Goodbye choices are responses the player can choose to exit the dialog without a response from the NPC
Dialog.GoodbyeDialog = "Sorry I can't right now."

local DialogChoice = Instance.new("DialogChoice") -- Adds a dialog option. Create more if you want more dialog options
DialogChoice.Parent = Dialog -- Be sure to parent it to the original dialog object we created earlier
DialogChoice.Name = "AcceptQuest"
DialogChoice.UserDialog = "Sure, I'll help you find your dog!" -- This is the dialog the player will give if they select this choice
DialogChoice.ResponseDialog = "Thank you so much! He should be around here somewhere..." -- This is the NPC's response if the player selects this dialog choice
```

We first set up the dog and sword tools. Then, we set up how the conversations go. Our NPC will first ask the player if they can help them find their dog. We set up the GoodbyeDialog to say that we can't. To add more dialog, we have to add a new DialogChoice. In our DialogChoice, we say that we will help the NPC find their dog and we state that the NPC will respond by saying "Thank you." But we want it to also have more functionality. We want the dog to appear once the player accepts. So, we have to have code execute once the event is triggered. Place the following at the end of your script.

```lua
Dialog.DialogChoiceSelected:Connect(function(Player, Choice)
    if Choice.Name == "AcceptQuest" then
        local dog = dogTool:Clone() -- Clone the dog to place it somewhere in the world
        dog.Parent = game.Workspace
        dog.Handle.CFrame = CFrame.new(-18.895, 0.5, -23.273) -- Change these coordinates to wherever you'd like the dog to spawn
        dog.Handle.ProximityPrompt.Triggered:Connect(function(player) -- Connect code to the proximity prompt button to pick up the dog when the player presses it
            dog.Parent = player.Backpack -- Manually place the dog in the player's inventory and equip it
            local humanoid = player.Character:FindFirstChildOfClass("Humanoid"):EquipTool(dog)
            dog.Handle.ProximityPrompt.Enabled = false
        end)
        
        Dialog.InitialPrompt = "Have you found my dog?"
        Dialog.GoodbyeChoiceActive = false -- We can disable the goodbye choice so that the player only has one dialog option to choose
        DialogChoice.Name = "CheckQuestObjective"
        DialogChoice.UserDialog = "Yes, I found your dog!"
    elseif Choice.Name == "CheckQuestObjective" then
        local dogObject = Player.Character:FindFirstChild("dog") -- search the player's child objects for the "dog" tool
        if dogObject ~= nil then
            dogObject:Destroy() -- Destroy the dog to remove it from the player's inventory
            DialogChoice.ResponseDialog = "Thank you for your help! Take this cool sword as a thank you from me!"
            
            local sword = swordTool:Clone() -- now we make a clone of the reward and equip it to the player
            sword.Parent = Player.Backpack
            Player.Character:FindFirstChildOfClass("Humanoid"):EquipTool(sword)
            
            Dialog.InitialPrompt = "Thanks for finding my dog for me!" -- This is what the NPC says after the quest is finished
            DialogChoice:Destroy() -- The player should not need to give any response after the quest is finished, so destroy it
        else
            DialogChoice.ResponseDialog = "I don't see him with you." -- The response if the dog is not found inside the player
        end
    end
end)
```

Basically, everytime the user selects a dialog choice, we check to see if it's the AcceptQuest dialog. if it is, then we teleport the dog to a location. We attach some code to the dog that allows it to be picked up if the player is close enough. Then we have the NPC ask if the player found the dog yet. If a dialog choice is selected and it is the CheckQuestObjective dilaog, then we check if the player is holding a dog. If they are, we switch out their dog for a sword.

### Follow up

For an additional challenge, add some code that allows the player to select a reward from a set of options to allow more than one kind of reward. You will need to add another dialog option and allow the player to give a response after completing the quest. You can also add to the quest by creating additional requirements to complete it. How would you change the dialog sequence so that there are more objectives for the player to complete?
