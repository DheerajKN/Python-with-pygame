import pygame, sys
from pygame.locals import *
pygame.init()


canvas = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Mouse Input')            # Initializing the modules, and  
black = (0, 0, 0)                                    # setting up the canvas. Same as
green = (0, 255, 0)                                  # Keyboard Input.

while True:
   
    for event in pygame.event.get():
        canvas.fill(black)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:                # Drawing a green circle of 
            x = event.pos[0]                         # radius 20px wherever the 
            y = event.pos[1]                         # mouse goes.
            pygame.draw.circle(canvas, green, (x, y), 20, 0)

    pygame.display.update() 
