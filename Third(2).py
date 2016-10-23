import pygame, sys                             # Importing the pygame
from pygame.locals import *                    # Module and initializing it.
pygame.init()                                  #


canvas = pygame.display.set_mode((500,500))    # 
pygame.display.set_caption('Keyboard Input')   #
black = (0,0,0)                                # Creating a canvas of size 500*500 and
canvas.fill(black)                             # setting caption as "Keyboard Input".
pygame.display.update()                        #


while True:                                    #
    for event in pygame.event.get():           #
        if event.type == KEYDOWN :             # Detecting a keyboard input and 
            if event.key == K_ESCAPE:          # ending the program if it is escape.
                pygame.quit()                  #
                sys.exit()  
