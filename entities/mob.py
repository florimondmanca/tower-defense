'''
mob :
	Contains every sort of mobs in the game.
	All classes inherits from the Mob class.
'''

import os
import pygame
import math
import constants as cst
from isometric import IsoSprite, isoutils
import math


class ChaserMob(IsoSprite):
	"""
	A mob animated through a spritesheet that chases a target IsoSprite object.
	If target is None, the Chaser stands in place.
	ChaserMob(pos=(0, 0), target=None) -> ChaserMob
	"""
	def __init__(self, pos=None, target=None):
		super(ChaserMob, self).__init__(path_to_image=os.path.join(cst.IMG_DIR, *["spritesheets", "chaser.png"]), pos=pos)
		self.target = target
		self.speed = 3  # chasing speed
		self.anim_key = 0  # 0, 1 or 2 (x on spritesheet)
		self.state = 0  # 0 front, 1 left, 2 right, 3 back (y on spritesheet)
		self.anim_speed = 5  # sprite anims every anim_speed frames
		self.anim_counter = 0  # increments every frame
		self.size = 32  # pixels
		# v force rect to be of size self.size, not spritesheet's size !
		new_iso_rect = pygame.Rect((0, 0), (self.size, self.size))
		new_iso_rect.center = self.iso_pos
		self.iso_rect = new_iso_rect
		new_rect = pygame.Rect((0, 0), isoutils.iso_to_cart(self.size, self.size))
		new_rect.center = self.pos
		self.rect = new_rect
		# ^
		self.anim_image = None
		self.update_anim_image()

	def update_anim_image(self):
		mask_rect = pygame.Rect(self.anim_key*self.size, self.state*self.size, self.size, self.size)
		self.anim_image = self.image.subsurface(mask_rect)

	def update(self):
		# update the animation
		self.anim_counter += 1
		if self.anim_counter == self.anim_speed:
			self.anim_counter = 0
			self.anim_key = (self.anim_key + 1) % 3
			self.update_anim_image()
		# update the position and orientation according to the target
		if self.target is not None:
			# get the direction to the target
			dir_x = self.target.pos[0] - self.pos[0]
			dir_y = self.target.pos[1] - self.pos[1]
			n = math.sqrt(dir_x*dir_x + dir_y*dir_y)
			dx = self.speed*dir_x/n
			dy = self.speed*dir_y/n
			if not self.rect.move(dx, dy).colliderect(self.target.rect):
				self.pos = (self.pos[0] + dx, self.pos[1] + dy)
				# define the new orientation
				angle = math.atan2(-dy, dx)
				if 0 < angle < math.pi/2:
					self.state = 2
				elif math.pi/2 <= angle < math.pi:
					self.state = 3
				elif -math.pi <= angle < -math.pi/2:
					self.state = 1
				else:
					self.state = 0

	def display(self, screen):
		screen.blit(self.anim_image, self.iso_rect)
		pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 2)
		pygame.draw.rect(screen, pygame.Color("blue"), self.target.rect, 2)
		pygame.draw.rect(screen, pygame.Color("red"), self.iso_rect, 2)
		pygame.draw.rect(screen, pygame.Color("red"), self.target.iso_rect, 2)