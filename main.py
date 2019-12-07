#Libraries:

import pygame
import random
import time
import math

#Initation of PyGame:

pygame.init()

#Screen config:

display_width = 1000
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Baddelsheep")

#Colours:

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN 	 = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

global rectColour
global m_x, m_y
 
global follower_x, follower_y
global displayImage
global health
global imagecount


#Start screen





#Crusor Coordinates:
m_x, m_y = pygame.mouse.get_pos()



#HP:
health = 600
hp6_6 = pygame.image.load("6_6_HP.png")
hp5_6 = pygame.image.load("5_6_HP.png")
hp4_6 = pygame.image.load("4_6_HP.png")
hp3_6 = pygame.image.load("3_6_HP.png")
hp2_6 = pygame.image.load("2_6_HP.png")
hp1_6 = pygame.image.load("1_6_HP.png")
hp0_6 = pygame.image.load("montana.png")

hp_pos = (10, 500)

#Battleship Sprite:
bb = pygame.image.load("yamato.png")
bb_rect = bb.get_rect()
bb_x = bb_rect.centerx = display_width/2
bb_y = bb_rect.centery = display_height/2

bb_blit_x, bb_blit_y = bb_x - 107, bb_y - 107


#Battleship Sprite Movement:
bb_down30 = pygame.image.load("yamato_down30.png")
bb_down45 = pygame.image.load("yamato_down45.png")
bb_down60 = pygame.image.load("yamato_down60.png")
bb_mov_down = [bb, bb_down30, bb_down45, bb_down60]
animation_up = [bb_down60, bb_down45, bb_down30, bb]
animation_done = False
up = False
down = False
imagecount = 0
returncount = 0

    #Turret A:
def turretA(bb_x, bb_y):
    screen.blit(turret_bb_A, (bb_x + 35, bb_y - 8 ))    

turret_bb_A = pygame.image.load("turret_bb_A.png")
turret_bb_A_rect = turret_bb_A.get_rect()
turret_bb_A_rotcenter = (turret_bb_A_rect.centerx - 6,turret_bb_A_rect.centery)

    #Turret B:
def turretB(bb_x, bb_y):
    screen.blit(turret_bb_B, (bb_x + 17, bb_y - 8))
    
turret_bb_B = pygame.image.load("turret_bb_B.png")
turret_bb_B_rect = turret_bb_B.get_rect()
turret_bb_B_rotcenter = (turret_bb_B_rect.centerx - 6,turret_bb_B_rect.centery)

    #Turret X:
def turretX(bb_x, bb_y):
    screen.blit(turret_bb_X, (bb_x - 72, bb_y - 8))  

turret_bb_X = pygame.image.load("turret_bb_X.png")
turret_bb_X_rect = turret_bb_X.get_rect()
turret_bb_X_rotcenter = (turret_bb_X_rect.centerx - 6,turret_bb_X_rect.centery)



def yamato():
    global imagecount
    global returncount
    if (imagecount >= 3):
        imagecount = 3

    if down:
        screen.blit(bb_mov_down[imagecount], (bb_blit_x, bb_blit_y))
        imagecount += 1
    
    else:
        global returncount
        global animation_done
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                animation_done = True


        if animation_done == False:
            screen.blit(bb, (bb_blit_x,bb_blit_y))
            
        if animation_done == True:    
            screen.blit(animation_up[returncount], (bb_blit_x,bb_blit_y))
            returncount += 1
            
        if returncount >= 3:
            returncount = 3
            animation_done == False
    

    pygame.display.update()
    
    
    
clock = pygame.time.Clock()  
keepgoing = True

while keepgoing:
    pygame.time.delay(50)

    #Background:
    screen.fill(WHITE)

    #Checking for exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepgoing = False
            
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT] == True):
        bb_x += 5
        bb_blit_x += 5
        
    if (keys[pygame.K_LEFT] == True):
        bb_x -= 5
        bb_blit_x -= 5
        
    if (keys[pygame.K_UP] == True):
        bb_y -= 5
        bb_blit_y -= 5
        up = True
        down = False
        
    if (keys[pygame.K_DOWN] == True):
        bb_y += 5
        bb_blit_y += 5
        down = True  
        up = False
        
    else:
        down = False
        up = False

    m_x, m_y = pygame.mouse.get_pos()
    
    
    
    
    if health == 600:
        screen.blit(hp6_6, hp_pos)
    elif 500 <= health < 600:
        screen.blit(hp5_6, hp_pos)
    elif 400 <= health < 500:
        screen.blit(hp4_6, hp_pos)
    elif 300 <= health < 400:
        screen.blit(hp3_6, hp_pos)
    elif 200 <= health < 300:
        screen.blit(hp2_6, hp_pos)
    elif 100 <= health < 200:
        screen.blit(hp1_6, hp_pos)
    elif health < 100:
        screen.blit(hp1_6, hp_pos)

    yamato()
    turretA(bb_x, bb_y)
    turretB(bb_x, bb_y)
    turretX(bb_x, bb_y)


#####
    if (keys[pygame.K_x] == True):
        print (bb_rect.center)
        print (m_x, m_y)
        health -= 25
#####    

    pygame.display.flip()

    
    #FPS:
    clock.tick(60)
    

pygame.quit()
