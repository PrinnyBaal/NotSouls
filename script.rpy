define e = Character("Eileen")


# The game starts here.

init -2 python:
    import time 
    class Coordinate:#this one is to manage the hamster's location on the screen
        def __init__(self,x,y,xmin,ymin,xmax,ymax, distance):
            #self explanatory
            self.x,self.y,self.xmin,self.ymin,self.xmax,self.ymax=x,y,xmin,ymin,xmax,ymax
            #whenever possible, xoffset and yoffset will be added to x and y
            #these offset variable are needed because Ren'Py lack Action
            #that let you add to variable
            self.xoffset,self.yoffset=0,0
            self.distance=distance
            return 
        #this transform method will be called every few milisecond
        #argument d is the object this transform will act on
        #ignore the time arguments for now, we don't need them
    
    #create an object to manage out hamster's location
    class enemy:
        def __init__(self, health, max, distance, sprite, x, y, bobbed, bobTick,\
                     rageTick, pause, window, comboMeter, alternate, windowLength):
            self.currentHealth=health
            self.maxHealth=max
            self.distance=distance
            self.sprite=sprite
            self.X=x
            self.Y=y
            self.bobbed=bobbed
            self.bobTick=bobTick
            self.rageTick=rageTick
            self.pause=pause
            self.window=window
            self.comboMeter=comboMeter
            self.alternate=alternate
            self.windowLength=windowLength
            
    class player:
        def __init__(self, health, max, timeStart1, timeTry1):
            
            self.currentHealth=health
            self.maxHealth=max
            self.exhaust=timeStart1
            self.recover=timeTry1
            
    player1= player(10,10, 0, 0)
    enemy1= enemy(13,13,.6,'idleHollow', 10,10, "N", 0,\
              0,0,False,0,False, 1500)
    hamster_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95, 1.0)
    
#this screen show a hamster and you can move them in 4 direction with arrow key
screen hamster_cage:
    
    #first we add the image of the hamster to the screen
    #an image named "hamster loc" must be defined of course
    #anchor (0.5,0.5) ensure that we will set the value of d.pos above
    #the coordinate will refer to the position of the exact centre of the image
    #at Transform(function=hamster_coordinate.transform) will make
    #the function hamster_coordinate.transform responsible for
    #various properties of the image "hamster loc"
    #these properties are passed in through the d argument
    #this function will be called every few milisecond
    
     

    add "hamster loc.png" anchor (0.5,0.5) xalign enemy1.distance yalign 0.0
    
    
    if player1.currentHealth>-2:
        text str(player1.currentHealth) size 40
    if enemy1.currentHealth>=-2:
        text str(enemy1.currentHealth) size 40 xalign .5 yalign 0.0 color "#f00"
        
    #now we add in all the keyboard control
    #here the higher-level keymap is used instead of listening to arrow button directly
    #because some device don't technically have arrow key, such as joystick
    #so instead of "K_LEFT" we use "focus_left" for example
    #we give each of these key event the appropriate Action
    #for example, for left button, we want to set the field
    #hamster_coordinate.xoffset to a negative number
    #SetField do exactly that job
    
    
        
  
    key "focus_left" action SetField(enemy1,"distance",0)
    key "focus_right" action SetField(enemy1,"distance",.2)
    
    if renpy.get_game_runtime()-player1.exhaust >=5:
        key "focus_up" action [SetField(enemy1,"currentHealth",enemy1.currentHealth-1), SetField(player1,"exhaust",renpy.get_game_runtime())]
    else:
        key "focus_up" action [SetField(enemy1,"currentHealth",enemy1.currentHealth+1), SetField(player1,"exhaust",renpy.get_game_runtime())]
    
    if enemy1.sprite=="idleHollow" and renpy.get_game_runtime()-player1.exhaust >=5:
    
        key "focus_down" action [SetField(player1,"currentHealth",player1.currentHealth-4),SetField(enemy1,"distance",0.6), SetField(enemy1,"sprite", "idleHollow"),\
            Return("start")]
    
    elif enemy1.sprite=="tiredHollow" and renpy.get_game_runtime()-player1.exhaust >=5:
        key "focus_down" action [SetField(player1,"currentHealth",player1.currentHealth+1),SetField(enemy1,"distance",0.6), SetField(enemy1,"sprite", "idleHollow"),\
            Return("start")]
        
    elif enemy1.sprite=="tiredHollow" and renpy.get_game_runtime()-player1.exhaust <5:
        key "focus_down" action [SetField(enemy1,"currentHealth",enemy1.currentHealth+1), SetField(player1,"exhaust",renpy.get_game_runtime())]
    
    #key "focus_down" action SetField(hamster_coordinate,"yoffset",+0.005)
   # if enemy1.distance == 0: #player adjacent to enemy
    #    action SetField(hamster_coordinate,"distance",0)

   # elif enemy1.distance == 1: #player near enemy
   #     action SetField(hamster_coordinate,"distance",2)
            
   # elif enemy1.distance == 2: #player far from enemy
   #     action SetField(hamster_coordinate,"distance",1)
    
    #"dismiss" is a whole collection of keys that are use to read dialogue
    #such as spacebar and enter key
    #action Return is use to quit this screen, without it you cannot quit
    #the argument for Return can be anything, it will be return to whatever call the screen
    
    key "p" action ShowMenu('preferences')
    
    key "w" action SetField(enemy1, "currentHealth", enemy1.currentHealth-1)
    
    key "s" action SetField(player1, "currentHealth", player1.currentHealth-1)
    
    
   # key "dismiss" action Return("noEscape")
    
    key "a" action SetField(enemy1,"distance",2)
    
    
    if enemy1.currentHealth <=0:
        timer 0.1 action Return("victory")
    
        
  #  if enemy1.sprite == "idleHollow":
  #      timer 5.0 action [SetField(enemy1,"distance",0), SetField(enemy1, "sprite", "tiredHollow")]
            
   # if enemy1.sprite == "tiredHollow":
    #    timer 2.0 action [SetField(enemy1,"distance",0.6), SetField(enemy1,"sprite", "idleHollow")]
    
    
screen timing2:
    timer 2.0 action [SetField(enemy1,"distance",0.6), SetField(enemy1,"sprite", "idleHollow")\
        ,SetField(player1, "currentHealth", player1.currentHealth-1), Return("start")]
    #if enemy1.sprite="idleHollow" action Return(start)
    
    
screen timing:
    
    timer 5 action [SetField(enemy1,"distance",.2), SetField(enemy1, "sprite", "tiredHollow"), Return("rest")]
    #if enemy1.sprite == "tiredHollow" action Return("rest")

label start:
    
    #"RAH!  RAH!  RAH!"
    #breaks loop if player health hits 0
    python:
        if player1.currentHealth<=0:
            renpy.jump("gameOver")
    #while enemy1.
    
    show screen hamster_cage
    python:
        jumpOff= renpy.call_screen("timing")
        renpy.jump(jumpOff)
    
    "RAH!  RAH!  RAH!"
 
    
label rest:
    python:
        jumpOff=renpy.call_screen("timing2")
        renpy.jump(jumpOff)
        
label noEscape:
    python:
        renpy.say(e, "Haha...no you're not getting out of this that easily.")
        renpy.jump("noEscape")
        
label victory:
    "Ya did it buddy."
    return
        
label gameOver:
    "Ya dun goofed."
return
