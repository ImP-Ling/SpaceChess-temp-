'''
this file should include all the controlling bit of the program
'''
import pygame

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
							return "button",item
						if item.label=="--Finish Round--":
							return "finish",item
