'''
this file should include the choosing UI and the grid（playing UI)

'''
import pygame
import Ships
import Input

class Grid:
    '''
    a grid class that automaticaly creates a grid with a surface
    '''
    def __init__(self):
        self.display=pygame.display.set_mode((1500,1024))
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
            #print("refreshed{0}".format(item))
        pygame.display.update()

    def attack(self,ship1,ship2):
        clock=pygame.time.Clock()
        if ship1.weapon_type == 1:
                i=0
                while(i<60):
                    clock.tick(60)
                    pygame.draw.line(self.display,(255,0,0),(self.x_to_X(ship1.center_x),self.y_to_Y(ship1.center_y)),(self.x_to_X(ship2.center_x),self.y_to_Y(ship2.center_y)),int(i/6))
                    i=i+1
                    pygame.display.update()
                self.refresh()
                i=0
                while(i<30):
                    clock.tick(60)
                    pygame.draw.circle(self.display,(255,0,0),(self.x_to_X(ship2.center_x),self.y_to_Y(ship2.center_y)),i)
                    pygame.display.update()
                    i=i+1
                self.refresh()
        if ship1.weapon_type==0:
            i=0
            x_distance=(self.x_to_X(ship1.center_x)-self.x_to_X(ship2.center_x))/60
            y_distance=(self.y_to_Y(ship1.center_y)-self.y_to_Y(ship2.center_y))/60
            while(i<60):
                clock.tick(60)
                x=self.x_to_X(ship1.center_x)-i*x_distance
                y=self.y_to_Y(ship1.center_y)-i*y_distance
                pygame.draw.circle(self.display,(255,0,0),(x,y),3)
                pygame.display.update()
                pygame.draw.circle(self.display,(255,255,255),(x,y),3)
                i=i+1
            self.refresh()
            i=0
            while(i<30):
                    clock.tick(60)
                    pygame.draw.circle(self.display,(255,0,0),(self.x_to_X(ship2.center_x),self.y_to_Y(ship2.center_y)),i)
                    pygame.display.update()
                    i=i+1
            self.refresh()
                
class Menu:
    def __init__(self,grid):
       self.display=grid.display
       self.surface=pygame.Surface((476,1024))
       self.surface.fill((255,255,255))
       pygame.font.init()
       #print(pygame.font.get_fonts())
       self.font1=pygame.font.SysFont('arial',30)
       self.font2=pygame.font.SysFont('arial',15)
       self.font3=pygame.font.SysFont('comicsans',25)
    def start_menu(self):
        self.display.blit(self.surface,(1024,0))
        text1=self.font1.render('Space Chess -- Welcome!',True,(0,0,0))
        self.display.blit(text1,(1050,20))
        pygame.display.update()

        single_player_button=Input.Button("Single Player",(0,0,0),1080,80,self.display)
        multi_player_button=Input.Button("Multi Player",(0,0,0),1080,120,self.display)
        single_player_button.display()
        multi_player_button.display()
        pygame.display.update()
        clock=pygame.time.Clock()

        next=None
        while next==None:
            pygame.event.wait()
            x,y=Input.get_L_mouse_click()
            if single_player_button.check_click((x,y)):
                single_player_button=Input.Button("Single Player",(255,0,0),1080,80,self.display)
                single_player_button.display()
                pygame.display.update()
                next="S"
            if multi_player_button.check_click((x,y)):
                multi_player_button=Input.Button("Multi Player",(255,0,0),1080,120,self.display)
                multi_player_button.display()
                pygame.display.update()
                next="M"
        return next

    def in_game_multi_player(self,player0,player1):
        self.display.blit(self.surface,(1024,0))
        text1=self.font1.render('Space Chess -- Multi Player',True,(0,0,0))
        self.display.blit(text1,(1050,30))
        text2=self.font2.render(" How to play? .",True,(255,0,0))
        self.display.blit(text2,(1050,70))
        text2=self.font2.render( '   First, click one of your ships or a ship you want to deploy.',True,(0,0,0))
        self.display.blit(text2,(1050,90))
        text2=self.font2.render('   Secondly, choose a function like moving or attack',True,(0,0,0))
        self.display.blit(text2,(1050,110))
        text2=self.font2.render('   Thirdly, choose a target.',True,(0,0,0))
        self.display.blit(text2,(1050,130))
        text3=self.font3.render('Resource Points',True,(255,0,0))
        self.display.blit(text3,(1050,160))
        text3=self.font3.render('  Player 0: ',True,(0,0,0))
        self.display.blit(text3,(1050,185))
        text3=self.font3.render('  Player 1: ',True,(0,0,0))
        self.display.blit(text3,(1050,210))
        #123

        pygame.display.update()
