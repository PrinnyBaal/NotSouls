screen threeHollows:
    
    python:
        if player1.select<0:
            player1.select=2
            
        elif player1.select==0:
            selected=enemy0
        elif player1.select ==1:
            selected=enemy1
        elif player1.select ==2:
            selected=enemy2
        elif player1.select >=2:
            player1.select=0
            selected=enemy0
            
    if enemy1.distance==0:
        $aligned=.6
    elif enemy1.distance==1:
        $aligned=.2
    elif enemy1.distance==2:
      pass
      
    add enemy1.sprite anchor (0.5,0.5) xalign aligned yalign 0.0
    
    if player1.currentHealth>-2 :
        text str(player1.currentHealth) size 40
    if enemy1.currentHealth>=-2 :
        text str(enemy1.currentHealth) size 40 xalign .5 yalign 0.0 color "#f00"
        
    if player1.stamina>6:
        $player1.stamina=6
        
    text str(player1.stamina)  size 40 xalign 0.0 yalign 0.1 color "#98fb98"
    
    if player1.blocking==False :
        text "You're open! (in horde)" size 40 xalign 0.0 yalign 0.5 color "#f00"
        
    elif player1.blocking==True :
        text "You've got your guard up! (in horde)" size 40 xalign 0.0 yalign 0.5 color "#98fb98"

    key "focus_left" action SetField(enemy1,"distance",0)
    key "focus_right" action SetField(enemy1,"distance",.2)

    if renpy.get_game_runtime()-player1.vuln >=4:
        pass
    if renpy.get_game_runtime()-player1.regen >=7:
        if player1.blocking==True:
            $player1.stamina+=1
            $player1.regen=renpy.get_game_runtime()
        elif player1.blocking==False:
            $player1.stamina+=2
            $player1.regen=renpy.get_game_runtime()
            
    if player1.stamina>=2 and player1.blocking==False:
        if renpy.get_game_runtime()-player1.exhaust >=.5:
            key "focus_up" action [SetField(enemy1,"currentHealth",enemy1.currentHealth-5), \
                SetField (player1, "stamina", player1.stamina-2), SetField(player1,"exhaust",renpy.get_game_runtime())]
        else:
            key "focus_up" action [SetField(enemy1,"currentHealth",enemy1.currentHealth+1), SetField(player1,"exhaust",renpy.get_game_runtime())]
            
    if player1.stamina>=1 and player1.blocking==False:
        if enemy1.sprite=="hamster loc.png" and renpy.get_game_runtime()-player1.exhaust >=5:
            key "focus_down" action [SetField(player1,"currentHealth",player1.currentHealth-4),SetField(enemy1,"distance",0), SetField(enemy1,"sprite", "hamster loc.png"),\
                Return("fightMany")]
        elif enemy1.sprite=="tiredHollow.png" and renpy.get_game_runtime()-player1.exhaust >=5:
            key "focus_down" action [SetField(player1,"stamina",player1.stamina+2),SetField(enemy1,"distance",0), SetField(enemy1,"sprite", "hamster loc.png"),\
                Return("fightMany")]
        elif enemy1.sprite=="tiredHollow.png" and renpy.get_game_runtime()-player1.exhaust <5:
            key "focus_down" action [SetField(enemy1,"currentHealth",enemy1.currentHealth+1), SetField(player1,"exhaust",renpy.get_game_runtime())]
        elif enemy1.sprite=='empty.png':
            pass
    
    key "p" action ShowMenu('preferences')
    
    if player1.blocking==False and player1.stamina>=1:
        key "dismiss" action [SetField(player1, "blocking", True), SetField (player1, "stamina", player1.stamina-1)]
        
    elif player1.blocking==True:
        key "dismiss" action SetField(player1, "blocking", False)
    
    python:
        if enemy1.currentHealth <=0:
            enemy1.sprite="empty.png"
        #timer 0.1 action Return("victory")
    
        #attack
   
            
    
screen attacking:
    
    timer 2.0 action [SetField(enemy1,"distance",0), SetField(enemy1,"sprite", "hamster loc.png")\
            ,Return(player1.blocking)]
    
    
screen neutral:
    
    timer 5 action [SetField(enemy1,"distance",1), SetField(enemy1, "sprite", "tiredHollow.png"), Return("restMany")]
# The game starts here.
#Single Mellee Combat

label fightMany:
       #"RAH!  RAH!  RAH!"
    #breaks loop if player health hits 0
    python:
        if player1.currentHealth<=0:
            renpy.jump("gameOver")
    #while enemy1.
    
    show screen threeHollows
    python:
        jumpOff= renpy.call_screen("neutral")
        renpy.jump(jumpOff)
    
    "RAH!  RAH!  RAH!"
 
    
label restMany:
    python:
        jumpOff=renpy.call_screen("attacking")
        if jumpOff==True:
            player1.stamina-=2
            player1.currentHealth-=0
            jumpOff="fightMany"
            renpy.jump(jumpOff)
        elif jumpOff==False:
            player1.currentHealth-=1
            jumpOff="fightMany"
            renpy.jump(jumpOff)
        else:
            renpy.jump(jumpOff)
        
