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
s1=Ships.Carriers(g,20,20,0,1,1)
s2=Ships.Cruisers(g,20,45,1,1,1)
s1.move(20,40)
s2.attack(s1)
g.refresh()

pygame.display.update()
input()


    