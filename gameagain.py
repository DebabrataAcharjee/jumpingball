import pygame
import time
from random import *

pygame.font.init()
font=pygame.font.SysFont(None,50,0,0,None)
score=pygame.font.SysFont(None,1,0,0,None)

pygame.init()

spx=300
spy=150
def screenmess(msg,color,):
    screen_text=font.render(msg,True,color)
    GD.blit(screen_text,[spx,spy])

def scoremess(msg,color,):
    screen_text=font.render(msg,True,color)
    GD.blit(screen_text,[710,40])


white=(255,255,255)
Black=(0,0,0)
red = [255, 0, 0]
Yellow=[255,255,0]


GD=pygame.display.set_mode((800,600))

x=800
y=0
j=0
r1=0
r2=0
v1=0
v2=0
x1=400
a=0
J=0

r1=randint(-30,30)
r2 = randint( 30, 70 )
gravity=0
speed=0

clock=pygame.time.Clock()

gameexit=False
gameover=False
#Menu
while not gameover:
    GD.fill(white)

    pygame.draw.rect(GD,red,[20,20,760,560],2)
    spx = 290
    spy = 100

    screenmess("WELCOME",Black)
    spx = 290
    spy = 200

    screenmess("Avoid Walls",Black)
    spx = 230
    spy = 300

    screenmess("Jump with Up arrow ",Black)

    spx = 220
    spy = 400

    screenmess("HighJump with Space ", Black)

    pygame.display.update()
    time.sleep(4)

#Actual Game
    while not gameexit:
        for catch in pygame.event.get():
            if catch.type== pygame.QUIT:
                gameexit = True
            elif catch.type== pygame.KEYDOWN:
                if catch.key == pygame.K_UP:
                    j=1
                elif catch.key==pygame.K_SPACE:
                    J=1
   #         if catch.key == pygame.K_DOWN:
   #             y-=10
    #Draw shapes
        GD.fill(white)
        pygame.draw.circle(GD, Black, [100, 475 - y], 26, 3)
        pygame.draw.circle( GD, Yellow, [100,475-y], 25, 0)


        pygame.draw.line( GD, Black, [0, 500], [800,500], 2 )
    #if x<500:
        v1=x+r1
        v2=x1+r2
        pygame.draw.line(GD, Black, [v1, 420], [v1, 500], 5)

        pygame.draw.line(GD, Black, [v2, 420], [v2,500], 5)

    #Text Score
        a+=1
        scoremess(str(a),Black)
    #movement of walls
        x -= 4 + speed
        x1 -= 4 + speed

        if v1<10:
            x=800
            r1=randint(-150,-40)
        if v2<10:
            x1=800
            r2=randint(140,270)
        if a%200==0:
            speed+=1

    #Making sure walls are atleast a bit far

        if v1-v2 < 130:
            v2+=100
        if v1-v2 >600:
            v2-=100


        clock.tick(30)
        pygame.display.update()


    #collision
        if v1<105 and v1>95 and y<75:
            pygame.draw.line(GD, white, [v1, 440], [v1, 500], 5)
            pygame.draw.circle(GD, red, [100, 475 - y], 25, 0)

            pygame.draw.line(GD, Black, [v1+20, 430], [v1, 500], 5)

            gameexit=True



        if v2<105 and v2>95 and y<75:
            pygame.draw.line(GD, white, [v2, 420], [v2, 500], 5)
            pygame.draw.circle(GD, red, [100, 475 - y], 25, 0)

            pygame.draw.line(GD, Black, [v2+20, 430], [v2, 500], 5)

            gameexit=True

    #jump
        if j==1:
            y+=15-gravity
            gravity+=1
        if y==0:
            j=0
            gravity=0
    #Highjump
        if J==1:
            y+=20-gravity
            gravity+=1
        if y==0:
            J=0
            gravity=0


    gameover=True
spx=300
spy=150
screenmess("GAME OVER",red)
pygame.display.update()
time.sleep(4)
pygame.quit()
quit()