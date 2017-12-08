#https://www.renpy.org/doc/html/screen_actions.html#SetVariable

screen tripleThreat:
    
    add enemy0.sprite  xalign enemy0.X yalign 0.0
    add enemy1.sprite  xalign enemy1.X yalign 0.0
    add enemy2.sprite  xalign enemy2.X yalign 0.0
    
    if player.currentHealth>-2 :
        text str(player.currentHealth) size 40
    if enemy1.currentHealth>=-2 :
        text str(enemy1.currentHealth) size 40 xalign .5 yalign 0.0 color "#f00"
    text str(player.stamina)  size 40 xalign 0.0 yalign 0.1 color "#98fb98"
    
    if player.blocking==False :
        text "You're open! (in melee)" size 40 xalign 0.0 yalign 0.5 color "#f00"
        
    elif player.blocking==True :
        text "You've got your guard up! (in melee)" size 40 xalign 0.0 yalign 0.5 color "#98fb98"
    
    key "focus_up" action [SetField(enemy1,"currentHealth",enemy1.currentHealth-1)]
    key "focus_left" action SetField(player, "select", enemy0.X)
    key "focus_right" action SetField(enemy1,"distance",.2)
    
    
    
    if enemy0.sprite != empty:
        $lightAttack(enemy0)
    if enemy1.sprite != empty:
        $lightAttack(enemy1)
    if enemy2.sprite != empty:
        $lightAttack(enemy2)
    $jumpoff='combat'
    timer 0.01 action Return(jumpoff)
    
label combat:
    
    python:
        jumpoff=renpy.call_screen('tripleThreat')
        
        renpy.jump(jumpoff)
    "Wahaha~"