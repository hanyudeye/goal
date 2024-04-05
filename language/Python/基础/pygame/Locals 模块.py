# Locals 里相当于定义了一个全局的常量

import pygame,sys
from pygame.locals import *
pygame.init()
canvas=pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello")
canvas.fill((0,0,0))
while True:
   for event in pygame.event.get():
      if(event.type == QUIT):
         pygame.quit()
         sys.exit(1)
 