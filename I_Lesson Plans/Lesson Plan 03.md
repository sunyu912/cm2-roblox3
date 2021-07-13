
# Lesson 3: NPC Going from Point to Point

  

  

# Summary and Learning Objective(s):

-   Using the Rig Builder to create a basic Character
    
-   Implementing the Pathfinding script into the Character and giving them goal points to reach
    

# Preparations:

-   If needed there is a Step-By-Step sheet that can be printed for each students to keep and refer back to.
    
-   This lesson’s script will be longer thus a link will be provided so that students can download the script and insert it into the NPC.
    

-   Link: [https://www.roblox.com/library/4640071191/NPCMoveScript](https://www.roblox.com/library/4640071191/NPCMoveScript)
    
-   Shorten: [http://bit.ly/roblox3_3_npcmovescript](http://bit.ly/roblox3_3_npcmovescript)
    

# Class Schedule/Tasks:

## Creating the NPC’s Body

1.  In order to make a Non-Player Character move, it needs a body first.
    
2.  The easiest way to get a premade humanoid type body is to use the Rig Builder and choose any type.  
    ![](https://lh6.googleusercontent.com/r6r7CAEQTVQ0KHwyeHoMgcP8Ym-xbOFkjOeq8WyNdDuy6vRj8csq79sjUXinH-BdatqbIhOEzm0FeW4UV2psThglAGsqGGn7ATZGOLw1Y5yxUFm679nlUhUf0wFJO031owEMrH--)
    
3.  Important** Make sure to unanchor the HumanoidRootPart as they come anchored by default.        
    
    1.  If you don’t unanchor, then the NPC will not move.
        

## Plotting Down the NPC’s Route

1.  For this lesson, we’ll create physical goal points for the NPC to traverse towards.
          
    1.  We’ll start by spawning in block/cylinder Parts (the preference is up to you) into the Workspace.
        
    2.  Flatten the Part into a platform and recolor to differentiate between them.
        
    3.  Spread them around a flat surface.  
        ![](https://lh6.googleusercontent.com/c_gZoAgBgIXipvwaij7yjJuAtbCb_VNoGFM5hLKbWrrmU2sogNNfzB5qcY5BThhVSlU5Q0DRpuEKwbQKlChzXrOyjEYpli0ZP9hJMTcbem97gHf6EXrVwYyOd3YxVlh-KPAso4PA)
        
    4.  You’ll notice I have them on 2 platforms with a gap in between. This is to demonstrate the NPC jumping later.
        

## Creating the NPC’s Script

1.  **Note: You should have the students download the script linked at the Preparations section, then go over what it does. Most students will become overwhelmed with the length
    
2.  Inside the NPC model, create an empty script.
           
    1.  For the sake of differentiation, I named the script NPCMoveScript.  
        ![](https://lh4.googleusercontent.com/RrlNJFnjMPgkv0kFlKxuyz5PE-VGV-9h4U9ZwHNtnyjPg5n_lbBmwQZn0qYjilGCbq4Z5NkN5xgVAj7HgZAewLdoxWxBnDtdX-R3q0YloyL2NxFxwT8pyoxlTsnLAq4c841L6SBX)
        

4.  Let’s type the script.
   
    1.  Begin by creating a variable to hold our table (what Lua calls an array) of goal Parts
        
    2.  Afterwards we’ll add 6 more variables:
   
        1.  NPC - holds the Parent object which is out NPC model
            
        2.  humanoid - holds our NPC’s humanoid
            
        3.  destination - holds an integer and will be used as indices to access our table of goals
            
        4.  path - holds the path object we created from PathfindingService
            
        5.  waypoints - holds a table of positions/actions
            
        6.  currentWaypointIndex - holds the current index to the waypoint the zombie is  
            currently heading towards.
             ![](https://lh6.googleusercontent.com/oJs84uprUFuJUHpR2IVuDsDB2TJk6ywIiDK_MUSK3Bm3I0kP2gjwTtxID3cf1XT3Uk5ZklY9HkNoUF0f-pN5b72DInM0xnMfqOIFJU14-IN90y6aiMuveQLe11lWsX1fX_36VIsW)

4.  Take what we used for the previous 2 lessons and putting it in a function so that we can easily call it.  
    ![](https://lh5.googleusercontent.com/IaIa4XUfYU9lcvllW20TdkdH0D94lC00JUP4VmZ-ZDOfo2-G3tSgdSpiiPw9fwfshFT9_Hlp3Rl_VS46EZb1ryf8XUSaLsGVyf8_QEFVZz9FDVhVAkdizp1ZrEyEtJKAkiXj72PN)
    
5.  Let’s look at what is different.
       
    1.  We took away the for-loop that goes through each waypoint, calling MoveTo for each iteration.
                
        1.  The reason why we took it away was to be able to handle a blocked route situation.
            
        2.  We don’t want to stop a for-loop midway and have it recalculate.
                        
        3.  Instead, we decide if the path is currently a success, then MoveTo the first waypoint while keeping track using the currentWaypointIndex.
            

7.  You might be wondering how the NPC is going to go through each waypoint if the followPath function only goes through the first. That is when we introduce a humanoid event called MoveToFinished.  
    ![](https://lh6.googleusercontent.com/BHHMpMNYHCZ3AaD05KQtag_s_JTyGYW36mByLsCfFPTSktO1gt-KghtpmI5XETGBH1SetS3vCeJM3-TRof7cj-Lxgico8y02CN_rdiNKH7Mb9JjW7f7JruBHyYxP2kq1Qay16pj2)
    
8.  Let’s take a look.
        
    1.  The humanoid’s event, MoveToFinished, is triggered whenever MoveTo is happening.
        
    2.  MoveToFinished has a boolean parameter called reached. [Link](https://developer.roblox.com/en-us/api-reference/event/Humanoid/MoveToFinished)
        
    3.  If the NPC successfully reached the goal and there is more waypoints to go, continue moving.
               
        1.  Check to see if the next waypoint has the Action, Jump, to tell the NPC to jump ahead of time.
            
    5.  Else we increment/set the destination to the next goal and call the followPath function to start the loop again.
    

10.  Finally, let’s handle the case when obstacles suddenly fall in front of the NPC and blocks its route. We need it to recalculate a step before it decides to move onto the blocked waypoint.
    
11.  Introducing the path’s event called Blocked with parameter blockedWaypointIndex.  
    ![](https://lh4.googleusercontent.com/7PxuMN_Lvnfb2edkBYDL4dXDfp1X_yzfJjp6aWIkVCSfIV5Wmo50nVsTZH_P8bQEOhydERJ6kJc-f-OzvlsoWsG9GWhCDkFDPJCnvouAO2wn-jhC64wCBEP794KmxxblFW8RQtom)
    
12.  The blocked index is checked to see if it is ahead of the current index instead of behind. It won’t matter if it is behind since the NPC would have already passed it.
    
13.  Finally, we will call followPath at the end of the script to start the infinite process.  
    ![](https://lh3.googleusercontent.com/kvvNaEtg7qHzkbxQK12eaJcyGBpSvbmBh337iSkRPom_JO4CYrhgagK7DUWcOtiq3x2ODsoBAfq8_dEs_ZXQE4b8qMIay9jlmshVwCzFQ5eeexUOkST-NwN_LhdshywoyiR2JyZb)
    

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on Roblox. We will be grabbing them again and again for future lessons.