'''
this file should include the choosing UI and the grid（playing UI)

'''
import pygame
import Ships
import Input

BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
GREY=(200,200,200)
class Grid:
    '''
    a grid class that automaticaly creates a grid with a surface
    '''
    def __init__(self):
        self.display=pygame.display.set_mode((1500,1024))
        pygame.display.set_caption("Space Chess")
        icon=pygame.image.load("ships/E-ship.png")
        pygame.display.set_icon(icon)
        self.surface=pygame.Surface((1024,1024))
        self.welcome()
        self.display.blit(self.surface,(0,0))
        self.all_ships=[]
    
    def x_to_X(self,x):
        X=16*x-1
        return X
    def y_to_Y(self,y):
        Y=16*(64-y)-1
        return Y

    def X_to_x(self,x):
        X=int((x+1)/16)
        return X
    def Y_to_y(self,y):
        Y=64-int((y+1)/16)
        return Y
    def welcome(self):
        image=pygame.image.load("welcome.png")
        self.surface.blit(image,(0,0))


    def draw_grid(self):
        self.surface.fill((255,255,255))
        for i in range(0,64):
            pygame.draw.line(self.surface,(200,200,200),(16*i,0),(16*i,1023))
            pygame.draw.line(self.surface,(200,200,200),(0,16*i),(1023,16*i))
            
        font1=pygame.font.SysFont('arial',30)
        text1=font1.render('Player 0',True,(0,0,0))
        self.surface.blit(text1,(924,970))
        text2=font1.render('Player 1',True,(0,0,0))
        self.surface.blit(text2,(924,20))


        pygame.draw.line(self.surface,(0,0,0),(1023,0),(1023,1023))
        pygame.draw.line(self.surface,(0,0,0),(0,1023),(1023,1023))

        pygame.draw.line(self.surface,(255,0,0),(0,16*11),(1023,16*11))
        pygame.draw.line(self.surface,(255,0,0),(0,16*53),(1023,16*53))

    def draw_and_create_base(self):
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

    def del_ship(self,ship2,player):
        i=0
        clock=pygame.time.Clock()
        while(i<60):
                    clock.tick(60)
                    pygame.draw.circle(self.display,(255,0,0),(self.x_to_X(ship2.center_x),self.y_to_Y(ship2.center_y)),i)
                    pygame.display.update()
                    i=i+1
        self.all_ships.remove(ship2)
        if ship2.val!=6:           
            player.ships.remove(ship2)
        self.refresh()

    def EMP(self,ship):
        i=0
        clock=pygame.time.Clock()
        while(i<60):
                    clock.tick(60)
                    self.refresh()
                    pygame.draw.circle(self.display,(100,100,255),(self.x_to_X(ship.center_x),self.y_to_Y(ship.center_y)),int(160/60*i),5)
                    pygame.display.update()
                    i=i+1

    def make_list(self):
        list1=[[0 for i in range(65)]for j in range(65)]
        for item in self.all_ships:
            list1[item.x][item.y]=item.val
        list2=[[0 for i in range(65)]for j in range(65)]
        for item in self.all_ships:
            list2[item.x][item.y]=item.player
        list3=[[0 for i in range(65)]for j in range(65)]
        for item in self.all_ships:
            list3[item.x][item.y]=item.health
        list4=[[0 for i in range(65)]for j in range(65)]
        for item in self.all_ships:
            list4[item.x][item.y]=item.damage
        list5=[[0 for i in range(65)]for j in range(65)]
        for item in self.all_ships:
            list5[item.x][item.y]=item.range
        list6=[[0 for i in range(65)]for j in range(65)]
        for item in self.all_ships:
            list6[item.x][item.y]=item.weapon_type
        list7=[[0 for i in range(65)]for j in range(65)]
        for item in self.all_ships:
            list7[item.x][item.y]=item.armour_type        
        return list1,list2,list3,list4,list5,list6,list7


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
       self.undo=None
       self.attack=None
       self.attack_color=BLACK
       self.deploy=None
       self.move=None
       self.move_color=BLACK
       self.torpedo=None
       self.torpedo_color=BLACK
       self.destroyer=None
       self.destroyer_color=BLACK
       self.cruiser=None
       self.cruiser_color=BLACK
       self.carrier=None
       self.carrier_color=BLACK
       self.eship=None
       self.eship_color=BLACK
       self.laser=None
       self.laser_color=BLACK
       self.railgun=None
       self.railgun_color=BLACK
       self.energy=None
       self.energy_color=BLACK
       self.hard=None
       self.hard_color=BLACK
       self.deploy=None
       self.deploy_color=BLACK
       self.special=None
       self.special_color=BLACK
       self.finish=None
       self.buttons=[self.undo,self.attack,self.deploy,self.move,self.torpedo,self.destroyer,self.cruiser,self.carrier,self.eship,self.laser,self.railgun,self.energy,self.hard,self.deploy,self.special,self.finish]
       #self.chosen=None

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

    def in_game_multi_player(self,player0,player1,this_round,chosen=None,count=0):
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
        pygame.display.update()

        #displaying RP
        text3=self.font3.render('Resource Points',True,(255,0,0))
        self.display.blit(text3,(1050,160))
        text3=self.font3.render('  Player 0: {0}'.format(player0.RP),True,(0,0,0))
        self.display.blit(text3,(1050,185))
        text3=self.font3.render('  Player 1: {0}'.format(player1.RP),True,(0,0,0))
        self.display.blit(text3,(1050,210))
        text3=self.font3.render('  Count:{}'.format(count),True,(0,0,0))
        self.display.blit(text3,(1300,250))
        pygame.display.update()


        #buttons
        self.undo=Input.Button("--Undo--",(0,0,0),1050,245,self.display)
        self.undo.display()
        self.attack=Input.Button("--Attack--",self.attack_color,1050,280,self.display)
        self.attack.display()
        self.move=Input.Button("--Move--",self.move_color,1050,315,self.display)
        self.move.display()

        #Deploy
        text4=self.font2.render('Deploy Ships: ( click the icon to choose )',True,(255,0,0))
        self.display.blit(text4,(1050,350))
        text4=self.font2.render('Torpedos: D:100,M:5,W:10, 10/15',True,self.torpedo_color)
        self.display.blit(text4,(1050,370))
        self.torpedo=Input.Image('ships/Torpedo.png',1300,370,self.display)
        self.torpedo.display()
        text4=self.font2.render('Destroyers: D:500,M:20,W:50, 25/40',True,self.destroyer_color)
        self.display.blit(text4,(1050,410))
        self.destroyer=Input.Image('ships/Destroyer.png',1300,410,self.display)
        self.destroyer.display()
        text4=self.font2.render('Cruisers: D:1000,M:50,W:100, 50/100',True,self.cruiser_color)
        self.display.blit(text4,(1050,450))
        self.cruiser=Input.Image('ships/Cruiser.png',1300,450,self.display)
        self.cruiser.display()
        text4=self.font2.render('Carriers: D:5000,M:100,W:100, 50/150',True,self.carrier_color)
        self.display.blit(text4,(1050,520))
        self.carrier=Input.Image('ships/Carrier.png',1300,520,self.display)
        self.carrier.display()
        text4=self.font2.render('E-ships: D:5000,M:50,W:100, 50/80',True,self.eship_color)
        self.display.blit(text4,(1050,590))
        self.eship=Input.Image('ships/E-ship.png',1300,590,self.display)
        self.eship.display()

        #choose armour and weapon
        text4=self.font2.render('Choose Armour and Weapon:',True,(255,0,0))
        self.display.blit(text4,(1050,630))
        self.laser=Input.Button("--Laser--",self.laser_color,1050,650,self.display)
        self.laser.display()
        self.railgun=Input.Button("--Railgun--",self.railgun_color,1200,650,self.display)
        self.railgun.display()
        self.energy=Input.Button("--Energy--",self.energy_color,1050,690,self.display)
        self.energy.display()
        self.hard=Input.Button("--Hard--",self.hard_color,1200,690,self.display)
        self.hard.display()
        self.deploy=Input.Button("--Deploy!--",self.deploy_color,1125,730,self.display)
        self.deploy.display()

        #extras
        self.special=Input.Button("--Special--",self.special_color,1200,245,self.display)
        self.special.display()
        self.finish=Input.Button("--Finish Round--",(255,0,0),1200,280,self.display)
        self.finish.display()
        text1=self.font1.render('Player {0}'.format(this_round),True,(0,0,0))
        self.display.blit(text1,(1300,190))

        #displays ships
        if chosen!=None:
            text4=self.font2.render('Chosen Ship:   {0}'.format(chosen),True,(255,0,0))
            self.display.blit(text4,(1050,780))
            text4=self.font2.render('  Damage: {0}'.format(chosen.damage),True,(0,0,0))
            self.display.blit(text4,(1050,810))
            text4=self.font2.render('  Health: {0}'.format(chosen.health),True,(0,0,0))
            self.display.blit(text4,(1050,840))
            text4=self.font2.render('  Armour: {0}'.format(chosen.armour_type),True,(0,0,0))
            self.display.blit(text4,(1050,870))
            text4=self.font2.render('  Weapon: {0}'.format(chosen.weapon_type),True,(0,0,0))
            self.display.blit(text4,(1050,900))
            pygame.display.update()
            #input()
        pygame.display.update()
        self.buttons=[self.undo,self.attack,self.deploy,self.move,self.torpedo,self.destroyer,self.cruiser,self.carrier,self.eship,self.laser,self.railgun,self.energy,self.hard,self.deploy,self.special,self.finish]

        
        return self.buttons 

    def in_game_single_player(self,player0,player1,this_round,chosen=None,count=0):
        self.display.blit(self.surface,(1024,0))
        text1=self.font1.render('Space Chess -- Single Player',True,(0,0,0))
        self.display.blit(text1,(1050,30))
        text2=self.font2.render(" How to play? .",True,(255,0,0))
        self.display.blit(text2,(1050,70))
        text2=self.font2.render( '   First, click one of your ships or a ship you want to deploy.',True,(0,0,0))
        self.display.blit(text2,(1050,90))
        text2=self.font2.render('   Secondly, choose a function like moving or attack',True,(0,0,0))
        self.display.blit(text2,(1050,110))
        text2=self.font2.render('   Thirdly, choose a target.',True,(0,0,0))
        self.display.blit(text2,(1050,130))
        pygame.display.update()

        #displaying RP
        text3=self.font3.render('Resource Points',True,(255,0,0))
        self.display.blit(text3,(1050,160))
        text3=self.font3.render('  Player 0: {0}'.format(player0.RP),True,(0,0,0))
        self.display.blit(text3,(1050,185))
        text3=self.font3.render('  Player 1: {0}'.format(player1.RP),True,(0,0,0))
        self.display.blit(text3,(1050,210))
        text3=self.font3.render('  Count:{}'.format(count),True,(0,0,0))
        self.display.blit(text3,(1300,250))
        pygame.display.update()


        #buttons
        self.undo=Input.Button("--Undo--",(0,0,0),1050,245,self.display)
        self.undo.display()
        self.attack=Input.Button("--Attack--",self.attack_color,1050,280,self.display)
        self.attack.display()
        self.move=Input.Button("--Move--",self.move_color,1050,315,self.display)
        self.move.display()

        #Deploy
        text4=self.font2.render('Deploy Ships: ( click the icon to choose )',True,(255,0,0))
        self.display.blit(text4,(1050,350))
        text4=self.font2.render('Torpedos: D:100,M:5,W:10, 10/15',True,self.torpedo_color)
        self.display.blit(text4,(1050,370))
        self.torpedo=Input.Image('ships/Torpedo.png',1300,370,self.display)
        self.torpedo.display()
        text4=self.font2.render('Destroyers: D:500,M:20,W:50, 25/40',True,self.destroyer_color)
        self.display.blit(text4,(1050,410))
        self.destroyer=Input.Image('ships/Destroyer.png',1300,410,self.display)
        self.destroyer.display()
        text4=self.font2.render('Cruisers: D:1000,M:50,W:100, 50/100',True,self.cruiser_color)
        self.display.blit(text4,(1050,450))
        self.cruiser=Input.Image('ships/Cruiser.png',1300,450,self.display)
        self.cruiser.display()
        text4=self.font2.render('Carriers: D:5000,M:100,W:100, 50/150',True,self.carrier_color)
        self.display.blit(text4,(1050,520))
        self.carrier=Input.Image('ships/Carrier.png',1300,520,self.display)
        self.carrier.display()
        text4=self.font2.render('E-ships: D:5000,M:50,W:100, 50/80',True,self.eship_color)
        self.display.blit(text4,(1050,590))
        self.eship=Input.Image('ships/E-ship.png',1300,590,self.display)
        self.eship.display()

        #choose armour and weapon
        text4=self.font2.render('Choose Armour and Weapon:',True,(255,0,0))
        self.display.blit(text4,(1050,630))
        self.laser=Input.Button("--Laser--",self.laser_color,1050,650,self.display)
        self.laser.display()
        self.railgun=Input.Button("--Railgun--",self.railgun_color,1200,650,self.display)
        self.railgun.display()
        self.energy=Input.Button("--Energy--",self.energy_color,1050,690,self.display)
        self.energy.display()
        self.hard=Input.Button("--Hard--",self.hard_color,1200,690,self.display)
        self.hard.display()
        self.deploy=Input.Button("--Deploy!--",self.deploy_color,1125,730,self.display)
        self.deploy.display()

        #extras
        self.special=Input.Button("--Special--",self.special_color,1200,245,self.display)
        self.special.display()
        self.finish=Input.Button("--Finish Round--",(255,0,0),1200,280,self.display)
        self.finish.display()
        text1=self.font1.render('Player {0}'.format(this_round),True,(0,0,0))
        self.display.blit(text1,(1300,190))

        #displays ships
        if chosen!=None:
            text4=self.font2.render('Chosen Ship:   {0}'.format(chosen),True,(255,0,0))
            self.display.blit(text4,(1050,780))
            text4=self.font2.render('  Damage: {0}'.format(chosen.damage),True,(0,0,0))
            self.display.blit(text4,(1050,810))
            text4=self.font2.render('  Health: {0}'.format(chosen.health),True,(0,0,0))
            self.display.blit(text4,(1050,840))
            text4=self.font2.render('  Armour: {0}'.format(chosen.armour_type),True,(0,0,0))
            self.display.blit(text4,(1050,870))
            text4=self.font2.render('  Weapon: {0}'.format(chosen.weapon_type),True,(0,0,0))
            self.display.blit(text4,(1050,900))
            pygame.display.update()
            #input()
        pygame.display.update()
        self.buttons=[self.undo,self.attack,self.deploy,self.move,self.torpedo,self.destroyer,self.cruiser,self.carrier,self.eship,self.laser,self.railgun,self.energy,self.hard,self.deploy,self.special,self.finish]

        
        return self.buttons 

    def game_ends(self,p,r):
        self.display.blit(self.surface,(1024,0))
        text1=self.font1.render('Space Chess -- Game Ends',True,(0,0,0))
        self.display.blit(text1,(1050,30))
        text1=self.font1.render('Player {0} wins'.format(p),True,(0,0,0))
        self.display.blit(text1,(1050,70))
        text1=self.font1.render('Rounds {0}'.format(r),True,(0,0,0))
        self.display.blit(text1,(1050,210))
        pygame.display.update()