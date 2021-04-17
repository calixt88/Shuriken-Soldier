import pygame
import os
import time

from StartScreen import *
from Constants import *
from pygame import mixer


#Window Initialize
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Sets window title and icon
pygame.display.set_caption("Shurkien Soldier")
shurikenIcon = pygame.image.load(os.path.join('Assets','Images', 'maroonShuriken.png'))
pygame.display.set_icon(shurikenIcon)

#Updates the screen
def update():
    pygame.display.update()

#draws the game screen
def drawGameScreen():
    WIN.fill((WHITE))
    update()

#Runs the code for the gameLoop
def gameLoop():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawGameScreen()

#Main function
def main(): 
    startScreen()
    gameLoop()
    pygame.QUIT()


#Keeps from running the main method after importing
if __name__ == "__main__":
    main()