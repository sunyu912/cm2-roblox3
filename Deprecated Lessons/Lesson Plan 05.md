
# Lesson 5: Chasing AI Enemy (Part 2)

  

  

# Summary and Learning Objective(s):

-   Using the zombie from the last lesson, we will make a zombie act a bit "smarter".
    
-   When their health reaches a certain threshold, the zombie will "run away" (path find) to the nearest regenerating spot.
    
-   Once they reach 100% health, they will return back to chasing.
    

# Important Notes:

-   The lessons are written in more detail and hands-on if the students are willing to see the process.
    
-   Otherwise for larger classes and for the sake of time, the Step-By-Step is provided along with a link to the scripts.
    

-   Link: [http://bit.ly/roblox3_5_zombiescript](http://bit.ly/roblox3_5_zombiescript)
    

-   From there, an overview of what has changed between the previous iteration and the current iteration can be applied.
    

# Class Schedule/Tasks:

## Setting Up Zombie Recovery Locations and the Zombie

1.  Let's make a recovery point for the zombie to head towards.
    
2.  This is simple to create and can be anything, but for the sake of simplicity I'll be duplicating the goal platforms we made in Lesson 1 and renaming it to ZombieHealSpot.  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2005/c55599c5-01e5-4b6d-a377-f30355027532.png)
    
3.  When the zombie touches the platform, we want the zombie to heal to 100%.
    
4.  Add new variables to be used: leg, healthThreshold, and retreat  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2005/de0c9f94-7b21-427d-8ae3-32c6e49404db.png)
    

## Adjusting the findNearest() in ZombieMoveScript

1.  Remember from the previous lesson that we had the function findNearest taking a boolean parameter, chase? We're going to handle when chase is false. For this, we will just add an else.
    

![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2005/fbb97a79-e88d-416b-bdfb-7839ffaf95d9.png)

## When Touching a Heal Spot

1.  The zombie needs to know when it is touching a heal spot.
    
2.  We will make a function to connect when a leg touches a healing platform.
    
3.  Just below the onTorsoTouched function, create onLegTouched:  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2005/294bf6d6-1e7b-41e9-b001-d6cdcd6663ab.png)
    
4.  Then connect it with the event. Here is the current list of connected events:  
    ![](https://storage.googleapis.com/cm-image-repository.appspot.com/roblox_3/Deprecated%20Lessons/Lesson%20Plan%2005/cb1b0c42-8947-43df-bb01-57f41bf39a05.png)
    
5.  All that's needed now is to test the script. Have students create or spawn a weapon.
    
6.  Make sure the weapon's script is server side or else the zombie's health won't register.
    
7.  Adjust the weapon's damage so that it won't instantly kill the zombie.
    

## Post-Class Deliverables

1.  Help students finish up their programs. Ensure students save their product, give it a title, and upload it to ShareMyWorks. Greet parents as they arrive and passout/explain homework to students and ensure their parents know they have homework to bring back.
    
2.  For this class, remember to always have them publish their script on Roblox. We will be grabbing them again and again for future lessons.