import pygame
from pygame.locals import *
pygame.init()

font = pygame.font.SysFont(None, 40, False, True)
text = 'Python is Fun!'
color = (0, 255, 255)

textobj = font.render(text, 1, color)
textrect = textobj.get_rect()

Canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Text Input')

textrect.left = 200
textrect.top = 200

Canvas.blit(textobj, textrect)
pygame.display.update()
