import pygame as pg
import random
import sys
import math
from pygame import mixer
import time
import os

pg.init()
mixer.init()

SCREEN=pg.display.set_mode((800,600))
NAME=pg.display.set_caption("SPACE FIGHT WITH KING")
BG=pg.image.load(("spacebg.jpg")).convert_alpha()
BG=pg.transform.scale(BG,(800,700)).convert_alpha()
PLAYER=pg.image.load(("spaceship.png")).convert_alpha()
ENEMY=pg.image.load(("alien.png")).convert_alpha()
BULLET=pg.image.load(("bullet.png")).convert_alpha()
FPS=40
SCORE=0
FONT=pg.font.SysFont(None,30)
BG_MUSIC=mixer.music.load("BG.mp3")


#GAME_OVER=True
#WELCOME=True
clock=pg.time.Clock()
def welcome():
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RETURN:
                    #WELCOME=False
                    GAME_OVER=False
                    return
                
        SCREEN.blit(BG,(0,0))
        SCREEN.blit(BULLET,(400,300))
        screen_text=FONT.render("press enter to continue",True,(255,255,255))
        SCREEN.blit(screen_text,(450,500))
        pg.display.update()
        clock.tick(FPS)


def maingame():
    BG_MUSIC=mixer.music.play(-1)
    
    playerX=380
    playerY=490
    playerX_change=0
    playerY_change=0


    enemyX=[]
    enemyY=[]
    enemyX_change=[]
    enemyY_change=[]
    enemyls=[]
    for i in range(15):
        enemyls.append(ENEMY)
        enemyX.append(random.randint(2+(i*5),730-(i)))
        enemyY.append(-60-(i*70 ))
        enemyX_change.append(0)
        enemyY_change.append(1)
    def enemy (x,y,i):
        for i in range(15):
            SCREEN.blit(enemyls[i],(x,y))

    bulletX=0
    bulletY=480
    bulletX_change=0
    bullety_change=-30
    bullet_state ="ready"
   

    def iscollision(enemyX,enemyY,bulletX,bulletY):

        distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
        distance1=math.sqrt(math.pow(enemyX-bulletX+10,2)+math.pow(enemyY-bulletY,2))
        if  distance<=40 or distance1<=40 :
            return True
        else:
            return False

    def text_screen(text,color,x,y):
        screen_text=FONT.render(text,True,(255,255,255))
        SCREEN.blit(screen_text,(x,y))
    while  True:

        pg.display.update()
        for event in pg.event.get():

            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RIGHT:
                    playerX_change=20
                    
                if event.key==pg.K_LEFT:
                    playerX_change=-20

                if event.key==pg.K_SPACE and  bullet_state=="ready":
                    
                    bullet_state="fire"
                    bulletX=playerX
                if event.key==pg.K_LSHIFT:
                    bullety_change=-40
                    for i in range(15):
                        enemyY_change[i]=0.9999
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    playerX_change = 0

                if event.key == pg.K_LEFT:
                    playerX_change = 0

                    
              

             
   
        playerX+=playerX_change
        playerY+=playerY_change
        if playerX<0:
            playerX=0
        if playerX>736:
            playerX=736

        SCREEN.blit(BG,(0,0))
        SCREEN.blit(PLAYER,(playerX,playerY))
        for i in range(15):
            if enemyX[i]<=0 and enemyY[i]+20==493:
                pass
                #enemyY[i]+=enemyY[i]-493
            elif enemyX[i]<=0 and enemyY[i]+20!=493:
                pass
                #enemyY[i]+=40
                #enemyX_change[i]=8
            if enemyX[i]>=736 and enemyY[i]+20==493:
                pass
                #enemyY[i]+=enemyY[i]-493
            elif enemyX[i]>=736 and enemyY[i]+20!=493:
                pass
                #enemyY[i]+=40
                #enemyX_change[i]=-8
            if enemyY[i]>=430:
               # GAME_OVER=True
                time.sleep(1)
                sys.exit()



            enemyX[i]+=enemyX_change[i]
            enemyY[i]+=enemyY_change[i]

            collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
            if collision:
                bullet_state="ready"
                bulletY=495
                enemyX[i]=random.randint(2,730)
                enemyY[i]=random.randint(-100-(i*15),-60-(i*5))
                global SCORE
                SCORE+=10
                
            enemy(enemyX[i],enemyY[i],i)
            text_screen("score:"+str(SCORE),(255,255,255),2,2)



        if bulletY<=0:
            bulletY=495   
            bullet_state="ready"
        if bullet_state == "fire":
            #print(bulletX,bulletY)
            SCREEN.blit(BULLET,( bulletX,bulletY))
            SCREEN.blit(BULLET,( bulletX+10,bulletY))
            bulletY+=bullety_change




        pg.display.update()
        clock.tick(FPS)
if __name__ == "__main__":
    welcome()
    maingame()

    
