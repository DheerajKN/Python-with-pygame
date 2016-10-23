import pygame,sys
from pygame.locals import *
pygame.display.init()
canvas=pygame.display.set_mode((300,300))
color=(0,0,0)
canvas.fill(color)
pygame.display.set_caption('CANVAS')
pygame.draw.rect(canvas,(0,255,0),(90,90,120,120),2)
pygame.draw.circle(canvas,(255,0,0),(150,150),50,2)
pygame.draw.polygon(canvas,(255,255,255),((100,100),(200,200),(100,200),(200,100)),2)
pygame.display.update()
