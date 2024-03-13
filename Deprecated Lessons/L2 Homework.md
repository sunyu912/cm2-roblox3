
# Assignment 2: Pathfinding Out A Maze

  


## Review Questions

1.  When creating a Tool, what should you name the part that allows players to pick it up?  
      
      
2.  Which one is considered an Event? (Circle all that apply)
    

    1.  MouseClick
        
    2.  ClickDetector
        
    3.  Touched
        
    4.  Activated  
          
    

4.  Fill in the Blank. A KillScript is placed in a part. When the player touches the part, they immediately die:  
      
        script.Parent.Touched:Connect( function (hit)  
          
        local human = hit.Parent:FindFirstChild("_________________")  
        if human ~= nil then  
        _________.Health = 0  
        end  
          
        end)
        

## Pathfinding Questions

1.  Let's say we spawned two Part into the Workspace. One is called Start and the other is called Finish.  
      
    Below are two lines in a Pathfinding script used to calculate the shortest route between the two parts, Start and Finish. Fill in the blank with the correct answer.  
      
        -- Creates the path object  
        local path = game:GetService ("_____________________"):CreatePath()  
          
        -- Compute the path  
        path:ComputeAsync (_____________.Position , Finish._____________)