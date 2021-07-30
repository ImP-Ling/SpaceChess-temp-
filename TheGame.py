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

"""
#demo
pygame.init()
p0=Player.Player(0)
p1=Player.Player(1)
g=Graphics.Grid()
m=Graphics.Menu(g)
m.start_menu()
m.in_game_multi_player(p0,p1,0)

g.draw_grid()
b0,b1=g.draw_and_create_base()
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

m.in_game_multi_player(p0,p1,1,s3)
pygame.display.update()
input()
"""


pygame.init()
while True:
    g=Graphics.Grid()
    m=Graphics.Menu(g)


    if m.start_menu()=="S":
        #single player
        print("unfinished")


    elif m.start_menu()=="M":
        #multi player
        print("multiplayer")
        p0=Player.Player(0)
        p1=Player.Player(1)
        b0,b1=g.draw_and_create_base()
        p0.ships.append(b0)
        p1.ships.append(b1)
        round=0
        is_player0=True
        while p0.ships[0].health>0 and p1.ships[0].health>0:
            if is_player0:
                this_round=0
                round=round+1
                is_player0=not is_player0
            else:
                this_round=1
                is_player0=not is_player0
            m.in_game_multi_player(p0,p1,this_round)
            next_round=False
            ship_to_display=None
            ship_to_deploy=None
            # single round
            while not next_round:
                m.in_game_multi_player(p0,p1,this_round,ship_to_display)
                label1,val1=Input.listen1(g,m)
                if label1=="ship":
                    print(val1)
                    ship_to_display=val1
                    m.in_game_multi_player(p0,p1,this_round,ship_to_display)
                elif label1=="button":
                    print(val1)
                    ship_to_deploy=val1
                label2,val2=Input.listen2(g,m,p0,p1,this_round,ship_to_display,label1)
                if label2=="undo":
                    continue
                if label2=="move":
                    x,y=Input.listen3()
                if label2=="attack":
                    x,y=Input.listen3()
                if label2=="change":
                    continue
                if label2=="special":
                    print("unfinished")
                    #Unfinished special effects
                if label2==1 or label2==0:
                    if this_round == 0:
                        while True:
                            x,y=Input.listen3()
                            X=g.X_to_x(x)
                            Y=g.Y_to_y(y)
                            for item in g.all_ships:
                                collide=item.check_click((x,y))
                                if collide:
                                    break

                            if Y<10 and not collide:
                                print(X,Y,val1.label)
                                if val1.label=="ships/Torpedo.png":
                                    if p0.RP >=100:
                                        ship=Ships.Torpedos(g,X,Y,0,label2,val2)
                                        p0.ships.append(ship)
                                        p0.RP=p0.RP-ship.cost
                                        g.refresh()
                                    else:
                                        print("not enough RP")
                                    break
                                        
                        