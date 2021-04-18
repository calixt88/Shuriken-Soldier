import pygame
import os
import time


from Constants import *
from main import *
from pygame import mixer

def startScreenSound():
    pygame.mixer.init()
    mixer.music.load('Assets/Sounds/FetchQuest-EvanKing.wav')
    mixer.music.play(-1)

def startScreen():
    startScreenSound()
    clock = pygame.time.Clock()
    pygame.font.init()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #Loading images

        WIN.fill((GREY))
        Shuriken_Soldier_Logo = pygame.image.load(os.path.join('Assets','Images', 'shurikenSoldierLogo.png'))
        Shuriken_Soldier_Image = pygame.image.load(os.path.join('Assets','Images', 'shurikenSoldier.png'))
        Shuriken_Soldier_Image_Scaled = pygame.transform.scale(Shuriken_Soldier_Image, (300,300))
        WIN.blit(Shuriken_Soldier_Logo, [90,0])
        WIN.blit(Shuriken_Soldier_Image_Scaled, [600, 150])
        WIN.blit(shurikenIcon, [10, 15])
        WIN.blit(shurikenIcon, [800, 15])
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render('START', False, (BLACK))
        WIN.blit(textsurface,(200,150))
        textsurface = myfont.render('OPTIONS', False, (BLACK))
        WIN.blit(textsurface,(200,200))
        textsurface = myfont.render('CREDITS', False, (BLACK))
        WIN.blit(textsurface,(200,250))
        textsurface = myfont.render('QUIT', False, (BLACK))
        WIN.blit(textsurface,(200,300))
        
        update()
            
        

    