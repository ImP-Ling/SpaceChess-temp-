'''
a series of ships classes
'''
import pygame
import math
import Graphics
class Ships:
    def __init__ (self,grid,x,y,player,weapon=0,armour=0):
        '''
        initialize Ship class
        '''
        self.grid=grid
        self.player=player
        self.x=x
        self.y=y
        self.range=None
        self.player=player
        self.cost=None
        self.weapon_cost=None
        self.move_cost=None
        self.image=None
        self.damage=None
        self.health=None
        self.weapon_type=0
        self.armour_type=0
        self.freeze=False
        self.type=None
        grid.new_ship(self)
        # deleted blit: self.image.blit(self.surface,(16*x,16*y))
    def __str__(self):
        '''
        returns a description of the ship object
        '''
        return("{0} at {1},{2}; player is {3}".format(self.type,self.x,self.y,self.player))

    def move(self,x,y):
        '''
        move the ship,return a cost
        '''
        if not self.freeze:
            cost=self.move_cost*(abs(self.x-x)+abs(self.y-y))
            #rect=pygame.draw.rect(self.surface,(255,255,255),self.image.get_rect())
            #rect.blit(self.surface,(16*self.x,16*self.y))

            self.x=x
            self.y=y
            #self.image.blit(self.surface,(16*self.x,16*self.y))
            return cost
        else:
            print("this {0} is frozen at the moment".format(self))
            #should include more ways to inform the player, unfinished
            return 0

    def attack(self,target):
        '''
        attack the target, containing  animations
        '''
        if self.get_distance(target)<=range:
            target.damage(self.damage,self.weapon_type)
            clock=pygame.time.Clock()
            grid.attack(self,target)
            # unfinished railgun animation
            return self.weapon_cost
        else:
            #unfinished alert
            print("attack of {0} to {1} out of range".format(self,target))

    def damage(self,damage,weapon_type):
        if(abs(weapon_type-self.armour_type)==0):
            self.health=self.health-int(damage/2)
        else:
            self.health=self.health-damage

    def get_distance(self,ship):
        d=math.sqrt((abs(self.x-ship.x))^2+abs(self.y-ship.y)^2)
        return d

    def rotate(self):
        #rotate the image if on the opponent side
        if self.player==1:
            pygame.transform.rotate(self.image,180)

class Torpedos(Ships):
    '''
    class Torpedos, as an basic example in ships; they have no special power
    small ship at a size of 1x1, or 16x16

    '''
    def __init__(self,grid,x,y,player,weapon=0,armour=0):
        super().__init__(grid,x,y,player)
        self.range=1
        self.cost=100
        self.weapon_cost=10
        self.move_cost=5
        self.image=pygame.image.load('ships/Torpedo.png')
        self.damage=10
        self.health=15
        self.weapon=0
        self.armour=0
        self.type="Torpedo"
        self.rotate()

class Destroyers(Ships):
    '''
    class Destroyers, a larger ship that cannot fire lasers, no special power
    small ship at 1x2, or 16x32
    '''
    def __init__(self,grid,x,y,player,weapon=0,armour=0):
        super().__init__(grid,x,y,player)
        self.range=3
        self.cost=500
        self.weapon_cost=50
        self.move_cost=20
        self.image=pygame.image.load('ships/Destroyer.png')
        self.damage=25
        self.health=40
        self.weapon=0
        self.armour=0
        self.type="Destroyer"
        self.rotate()

class Cruisers(Ships):

    '''
    class Cruisers, a larger ship that can fire lasers and railgun, no special power
    bigger ship at 2x4, or 32x64
    '''
    def __init__(self,grid,x,y,player,weapon=0,armour=0):
        super().__init__(grid,x,y,player)
        self.range=5
        self.cost=1000
        self.weapon_cost=100
        self.move_cost=50
        self.image=pygame.image.load('ships/Cruiser.png')
        self.damage=50
        self.health=100
        self.weapon=weapon
        self.armour=armour
        self.type="Cruiser"
        self.rotate()

class Carriers(Ships):
    '''
    class Carriers, same grade as the cruisers, and have the same weapons like the cruisers, special power is to deploy torpedo ships
    same grade at 2x4 or 32x64
    '''
    def __init__(self,grid,x,y,player,weapon=0,armour=0):
        super().__init__(grid,x,y,player)
        self.range=5
        self.cost=5000
        self.weapon_cost=100
        self.move_cost=100
        self.image=pygame.image.load('ships/Carrier.png')
        self.damage=50
        self.health=150
        self.weapon=weapon
        self.armour=armour
        self.type="Carrier"
        self.ships=True
        self.rotate()

    def launch(self):
        if self.ships:
            ships=[]
            if x==1:
                x=2
            if x==64:
                x=63
            ships.append(Torpedos(self.surface,x-1,y,player))
            ships.append(Torpedos(self.surface,x-1,y-1,player))
            ships.append(Torpedos(self.surface,x-1,y-2,player))
            ships.append(Torpedos(self.surface,x-1,y-3,player))
            ships.append(Torpedos(self.surface,x+2,y,player))
            ships.append(Torpedos(self.surface,x+2,y-1,player))
            ships.append(Torpedos(self.surface,x+2,y-2,player))
            ships.append(Torpedos(self.surface,x+2,y-3,player))
            return ships
        else:
            #a way to tell players deployed already
            print('already deployed')

class E_ships(Ships):
    '''
    class E-ships, same grade as Cruisers, can fire lasers and railgun, but can also fire up emp
    ship at 2x4,or 32x64
    '''
    def __init__(self,grid,x,y,player,weapon=0,armour=0):
        super().__init__(grid,x,y,player)
        self.range=5
        self.cost=5000
        self.move_cost=50
        self.weapon_cost=100
        self.image='/ships/E-ship.png'
        self.damage=50
        self.health=80
        self.armour=armour
        self.weapon=weapon
        self.type="E-ship"
        self.ships=[]
        self.rotate()

    def EMP(self,ships):
         #have to enter a list of ships, but cannot detect(needs further programming)
         self.ships.clear()
         for item in ships:
             item.freeze=True
             self.ships.append(item)
         return cost
    def unfreeze(self):
         #this should be used after one round
         for item in self.ships:
             self.ships.freeze=False

class Base(Ships):
    '''
    a basic Base class as the home base, cannot move
    Base at 8x4, or 128*64
    '''
    def __init__(self,grid,x,y,player,weapon=0,armour=0):
        super().__init__(grid,x,y,player)
        self.range=8
        self.weapon_cost=150
        self.damage=80
        self.health=500
        self.image=pygame.image.load('ships/HomeBase.png')
        self.type="Base"
        if player==0:
            self.x=29
            self.y=6
        if player==1:
            self.x=29
            self.y=62

    def move(self,x,y):
        '''
        having shome fun
        '''
        print("why are u trying to move the home base???")
        
        
