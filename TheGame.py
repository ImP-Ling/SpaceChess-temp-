import pygame

    #resolution is 1024x1024
    #64x64
    #x and y means 64x64
    #need to x16
    #weapon type 0 means kinetic energy weapon, 1 means lazer
pygame.init()
surface=pygame.display.set_mode([1024,1024])

class Ships:
    def __init__ (self,surface,x,y,player):
        self.surface=surface
        self.player=player
        self.x=x
        self.y=y
        self.player=player
        self.cost=None
        self.weapon_cost=None
        self.move_cost=None
        self.image=None
        self.damage=None
        self.health=None
        self.weapon_type=0
        self.armour_type=0
        self.image.blit(self.surface,(16*x,16*y))

    def move(self,x,y):
        cost=self.move_cost*(abs(self.x-x)+abs(self.y-y))
        rect=pygame.draw.rect(self.surface,(255,255,255),self.image.get_rect())
        rect.blit(self.surface,(16*self.x,16*self.y))
        self.x=x
        self.y=y
        self.image.blit(self.surface,(16*self.x,16*self.y))
        return cost

    def attack(self,target):
        target.damage(self.damage,self.weapon_type)
        clock=pygame.time.Clock()
        if self.weapon_type == 1:
            i=0
            while(i<60):
                clock.tick(60)
                pygame.draw.line(self.surface,(255,0,0),(16*self.x,16*self.y),(16*target.x,16*target.y),int(i/6))
                i=i+1

        return self.weapon_cost

    def damage(self,damage,weapon_type):
        if(abs(weapon_type-self.armour_type)==0):
            self.health=self.health-int(damage/2)
        else:
            self.health=self.health-damage
    