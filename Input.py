'''
this file should include all the controlling bit of the program
'''
import pygame
import Graphics

BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
GREY=(200,200,200)

class Button(object):
	def __init__(self, text, color, x=None, y=None,displays=None, **kwargs):
		font=pygame.font.SysFont('arial',20)
		self.surface = font.render(text, True, color)
		self.displays=displays
		self.WIDTH = self.surface.get_width()
		self.HEIGHT = self.surface.get_height()
		self.label=text

		if 'centered_x' in kwargs and kwargs['centered_x']:
			self.x = display_width // 2 - self.WIDTH // 2
		else:
			self.x = x

		if 'centered_y' in kwargs and kwargs['cenntered_y']:
			self.y = display_height // 2 - self.HEIGHT // 2
		else:
			self.y = y

	def display(self):
		self.displays.blit(self.surface, (self.x, self.y))

	def check_click(self, position):
		
		x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
		y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

		if x_match and y_match:

			return True
		else:
			return False


class Image(Button):
	def __init__(self,image,x=None,y=None,displays=None,**kwargs):
		
		self.surface = pygame.image.load(image)
		self.displays=displays
		self.WIDTH = self.surface.get_width()
		self.HEIGHT = self.surface.get_height()
		self.label=image


		if 'centered_x' in kwargs and kwargs['centered_x']:
			self.x = display_width // 2 - self.WIDTH // 2
		else:
			self.x = x

		if 'centered_y' in kwargs and kwargs['cenntered_y']:
			self.y = display_height // 2 - self.HEIGHT // 2
		else:
			self.y = y






def get_L_mouse_click():	
	if pygame.mouse.get_pressed(3)[0]:
		print("pressed")
		x,y=pygame.mouse.get_pos()
		return x,y
	else:
		return 0,0
	


def get_R_mouse_click():
	if pygame.mouse.get_pressed()[1]:
		x,y=pygame.mouse.get_pos()
		return x,y
	else:
		return 0,0


def listen1(grid,menu):
	while True:
		pygame.event.wait()
		if pygame.mouse.get_pressed(3)[0]:
			print("pressed")
			x,y=pygame.mouse.get_pos()
			if x<=1024 and y<=1024:
				for item in grid.all_ships:
					if item.check_click((x,y)):
						print("{0}  {1} {2}".format(item,x,y))
						return "ship",item
			else:
				#print(menu.buttons)
				for item in menu.buttons:
					#print(item)
					if item.check_click((x,y)):
						print("{0}{1} {2}".format(item,x,y))
						print(item.label[0:4])
						if item.label[0:4]=="ship":
							
							#here
							return "button",item
						if item.label=="--Finish Round--":
							return "finish",item

def undo_deploy(menu):
	menu.laser_color=BLACK
	menu.railgun_color=BLACK
	menu.energy_color=BLACK
	menu.hard_color=BLACK
	menu.deploy_color=BLACK
	menu.torpedo_color=BLACK
	menu.destroyer_color=BLACK
	menu.cruiser_color=BLACK
	menu.carrier_color=BLACK
	menu.eship_color=BLACK

def undo_menu(menu):
	menu.attack_color=BLACK
	menu.move_color=BLACK
	menu.undo_color=BLACK
	menu.special_color=BLACK

def unclickable_deploy(menu):
	menu.laser_color=GREY
	menu.railgun_color=GREY
	menu.energy_color=GREY
	menu.hard_color=GREY
	menu.deploy_color=GREY

def unclickable_menu(menu):
	menu.attack_color=GREY
	menu.move_color=GREY
	menu.undo_color=BLACK
	menu.special_color=GREY

def listen2(grid,menu,p0,p1,this_round,ship_to_display,label1,round):
	weapon=0
	armour=0
	while True:
		pygame.event.wait()
		if pygame.mouse.get_pressed(3)[0]:
			print("pressed")
			x,y=pygame.mouse.get_pos()
			if x<=1024 and y<=1024:
				return "change",0


			if label1=="ship":
				if menu.undo.check_click((x,y)):
					print("undo")
					menu.move_color=BLACK
					menu.attack_color=BLACK
					undo_deploy(menu)
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
					return "undo",0
				elif menu.move.check_click((x,y)):
					print("move")
					menu.move_color=RED
					menu.attack_color=BLACK
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
					return "move",0
				elif menu.attack.check_click((x,y)):
					print("attack")
					menu.move_color=BLACK
					menu.attack_color=BLACK
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
					return "attack",0
				elif menu.special.check_click((x,y)):
					print("special")
					return "special",0
				elif menu.finish.check_click((x,y)):
					print("finish")
					menu.move_color=BLACK
					menu.attack_color=BLACK
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
					return "finish",0
			elif label1=="button":
				
				
				if menu.undo.check_click((x,y)):
					print("undo")
					menu.move_color=BLACK
					menu.attack_color=BLACK
					undo_deploy(menu)
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
					return "undo",0
				if menu.laser.check_click((x,y)):
					print("laser")
					weapon=1
					menu.laser_color=RED
					menu.railgun_color=BLACK
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
				if menu.railgun.check_click((x,y)):
					print("railgun")
					weapon=0
					menu.railgun_color=RED
					menu.laser_color=BLACK
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
				if menu.energy.check_click((x,y)):
					print("energy")
					armour=1
					menu.energy_color=RED
					menu.hard_color=BLACK
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
				if menu.hard.check_click((x,y)):
					print("hard")
					armour=0
					menu.hard_color=RED
					menu.energy_color=BLACK
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
				if menu.deploy.check_click((x,y)):
					print("deploy")
					
					menu.deploy_color=RED
					menu.in_game_multi_player(p0,p1,this_round,ship_to_display,round)
					return weapon,armour

def listen3():
	while True:
		pygame.event.wait()
		if pygame.mouse.get_pressed(3)[0]:
			print("pressed0")
			x,y=pygame.mouse.get_pos()
			return x,y,0
		elif pygame.mouse.get_pressed(3)[2]:
			print("pressed2")
			x,y=pygame.mouse.get_pos()
			return x,y,1
	