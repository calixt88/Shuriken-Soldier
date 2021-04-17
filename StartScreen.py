import pygame
import os

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
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        startScreen_backgroundImage = pygame.image.load(os.path.join('Assets','Images', 'maroonShuriken.png'))
        WIN.blit(startScreen_backgroundImage, [0,0])
        update()


    