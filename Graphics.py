'''
this file should include the choosing UI and the grid（playing UI)

'''
import pygame
import Ships

class Grid:
    '''
    a grid class that automaticaly creates a grid with a surface
    '''
    def __init__(self):
        self.display=pygame.display.set_mode((1024,1024))
        self.surface=pygame.Surface((1024,1024))
        self.draw_grid()
        self.display.blit(self.surface,(0,0))
        self.all_ships=[]
    
    def x_to_X(self,x):
        X=16*x-1
        return X
    def y_to_Y(self,y):
        Y=16*(64-y)-1
        return Y

    def draw_grid(self):
        self.surface.fill((255,255,255))
        for i in range(0,64):
            pygame.draw.line(self.surface,(0,0,0),(16*i,0),(16*i,1023))
            pygame.draw.line(self.surface,(0,0,0),(0,16*i),(1023,16*i))
        pygame.draw.line(self.surface,(0,0,0),(1023,0),(1023,1023))
        pygame.draw.line(self.surface,(0,0,0),(0,1023),(1023,1023))

    def draw_and_Create_base(self):
        player0_base=Ships.Base(self,0,0,0)
        player1_base=Ships.Base(self,0,0,1)
        self.all_ships.append(player0_base)
        self.all_ships.append(player1_base)
        self.display.blit(player0_base.image,(self.x_to_X(player0_base.x),self.y_to_Y(player0_base.y)))
        self.display.blit(player1_base.image,(self.x_to_X(player1_base.x),self.y_to_Y(player1_base.y)))
        self.refresh()
        return player0_base,player1_base

    def new_ship(self,ship):
        self.all_ships.append(ship)
        self.display.blit(ship.image,(self.x_to_X(ship.x),self.y_to_Y(ship.y)))
        self.refresh()

    def refresh(self):
        self.display.blit(self.surface,(0,0))
        for item in self.all_ships:
            self.display.blit(item.image,(self.x_to_X(item.x),self.y_to_Y(item.y)))
            print("refreshed{0}".format(item))
        pygame.display.update()

    def attack(self,ship1,ship2):
         if ship1.weapon_type == 1:
                i=0
                while(i<60):
                    clock.tick(60)
                    pygame.draw.line(self.display,(255,0,0),(self.x_to_X(ship1.x),self.y_toY(ship1.y)),(self.x_to_X(ship2.x),self.y_to_Y(ship2.y)),int(i/6))
                    i=i+1
                    self.refresh()
class Menu:
    def __init__(self):
       pass 
