import pygame
import Ships
import Input
import Enemy
import Graphics
    #resolution is 1024x1024
    #64x64
    #x and y means 64x64
    #need to x16
    #weapon type 0 means kinetic energy weapon, 1 means lazer
    #resolution means (blit) x=x*16 y=(64-y)*16
pygame.init()
g=Graphics.Grid()
g.draw_grid()
b0,b1=g.draw_and_Create_base()
print("{0}{1}".format(b0,b1))
pygame.display.update()
input()


    