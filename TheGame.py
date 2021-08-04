import pygame
import Ships
import Input
import Enemy
import Graphics
import Player
    #resolution is 1024x1024
    #64x64
    #x and y means 64x64
    #need to x16
    #weapon type 0 means kinetic energy weapon, 1 means lazer
    #resolution means (blit) x=x*16 y=(64-y)*16
pygame.init()
g=Graphics.Grid()
m=Graphics.Menu(g)
p0=Player.Player(0)
p1=Player.Player(1)
m.start_menu()
m.in_game_multi_player(p0,p1)

g.draw_grid()
b0,b1=g.draw_and_Create_base()
print("{0}{1}".format(b0,b1))
s1=Ships.Carriers(g,20,30,0,1,1)
s2=Ships.Cruisers(g,10,30,1,1,1)
s1.move(20,40)
s2.move(20,48)
s2.attack(s1)
g.refresh()

s3=Ships.Cruisers(g,30,30,0,0,0)
s4=Ships.Destroyers(g,40,30,1,0,0)
s4.attack(s3)
g.refresh()

pygame.display.update()
input()


    