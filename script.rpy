# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -2 python:
    import random
    import time
    import pygame
    
    #Core Variable names for images
    idleEnemy='lucy_happy.png'
    angryEnemy= 'lucy_mad.png'
    dangerEnemy= 'eileen vhappy.png'
    empty="empty.png"
    
    class enemy:
        def __init__(self, health, max, distance, sprite, X, y, bobbed, bobTick,\
                     rageTick, idle, attack, window, comboMeter, alternate, windowLength):
            self.currentHealth=health
            self.maxHealth=max
            self.distance=distance
            self.sprite=sprite
            self.X=X
            #############
            self.Y=y
            self.bobbed=bobbed
            self.bobTick=bobTick
            self.rageTick=rageTick
            self.idle=idle
            ###############
            self.attack=attack
            self.window=window
            self.comboMeter=comboMeter
            self.alternate=alternate
            self.windowLength=windowLength
            
    class player:
        def __init__(self, health, max, stamina, timeStart1, regenTime, blocking, vuln,select):
            
            self.currentHealth=health
            self.maxHealth=max
            self.stamina=stamina
            self.exhaust=timeStart1
            self.regen=regenTime
            self.blocking=blocking
            self.vuln=vuln
            self.select=select
            
    player= player(10,10, 6, 0, 0, False, 0, 0.5)
    enemy0= enemy(12,13,.6, idleEnemy, 0.2,\
                  10, "N", 0, 0,2,\
                  1,False,0,False, 1500)
    enemy1= enemy(12,13,.6, idleEnemy, 0.5,\
                  10, "N", 0, 0,2,\
                  1,False,0,False, 1500)
    enemy2= enemy(12,13,.6, idleEnemy, 0.7,\
                  10, "N", 0, 0,2,\
                  1,False,0,False, 1500)    
    
    select=enemy1
    def lightAttack(enemy):
    
        if enemy.rageTick==0:
            enemy.rageTick=renpy.get_game_runtime()
            enemy.idle = 1.5
            enemy.windowLength=.75

            
        if(renpy.get_game_runtime()-enemy.rageTick)>=enemy.idle and enemy.sprite is idleEnemy: #wind-up begins
            enemy.sprite=angryEnemy
            #windUp=renpy.get_game_runtime()
            #idle hollow to red hellow

        if (renpy.get_game_runtime()-enemy.rageTick)>=enemy.idle+enemy.attack and enemy.window is False and enemy.sprite is not idleEnemy:
            if enemy.X == player.select:
                enemy.sprite=dangerEnemy
            elif enemy.X is not player.select:
                enemy.sprite=angryEnemy
            enemy.window = True
            
        
        if (renpy.get_game_runtime()-enemy.rageTick)>=(enemy.windowLength+enemy.attack+enemy.idle) and enemy.window is True and enemy.sprite is not idleEnemy: #hit connects
            enemy.window=False
            enemy.sprite=idleEnemy
            enemy.alternate=True
            enemy.rageTick=0
            
            player.currentHealth-=2
            
            '''
            if enemy.distance ==1:
                if recovery == True:
                    #heavy damage sound
                    playerHealth-=3

                elif block == True:
                    playerHealth -=1
                    stamHealth -= 1
                    if stamHealth <=0:
                        #additional damage sound
                        playerHealth-=3

                elif recovery == False:
                    #modest damage sound
                    playerHealth -=2

            elif enemy.distance in (2,3):
                pass
                #whiff
                #print("Iudex missed a light attack due to distance")

            else:
                pass
                #print("Distance was somehow not 1, 2, or 3?")    
            '''
            

label start:
    "Howdy howdy howdy"
    jump combat
    return