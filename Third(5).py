import pygame
from pygame.locals import *

rect1 = pygame.Rect(10, 10, 10, 10)
rect2 = pygame.Rect(15, 15, 15, 10)

a,b = rect1, rect2

if (((a.left > b.left) and (a.left < b.right) and 
  (a.top > b.top) and (a.top < b.bottom))
    or ((a.left > b.left) and (a.left < b.right) and 
  (a.bottom > b.top) and (a.bottom < b.bottom))
    or ((a.right > b.left) and (a.right < b.right) and 
  (a.top > b.top) and (a.top < b.bottom))
    or ((a.right > b.left) and (a.right < b.bottom) and 
  (a.bottom > b.top) and (a.bottom < b.bottom))):
    print ("Intersecting")
else:
  print ("Non Intersecting")
