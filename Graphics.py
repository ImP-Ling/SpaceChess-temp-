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
        self.surface=pygame.display.set_mode((1024,1024))
        self.draw_grid()
    
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
        player0_base=Ships.Base(self.surface,0,0,0)
        player1_base=Ships.Base(self.surface,0,0,1)
        self.surface.blit(player0_base.image,(self.x_to_X(player0_base.x),self.y_to_Y(player0_base.y)))
        self.surface.blit(player1_base.image,(self.x_to_X(player1_base.x),self.y_to_Y(player1_base.y)))
        return player0_base,player1_base