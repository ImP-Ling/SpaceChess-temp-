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
		print(position)
		x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
		y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

		if x_match and y_match:

			return True
		else:
			return False


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
