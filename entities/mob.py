'''
mob :
	Contains every sort of mobs in the game.
	All classes inherits from the Mob class.
'''

import os
import pygame
import math
import constants as cst
import math
from . import entity


class ChaserMob(entity.Mob):
	"""
	A mob animated through a spritesheet that chases a target IsoSprite object.
	If target is None, the Chaser stands in place.
	ChaserMob(pos=(0, 0), target=None) -> ChaserMob
	"""
	def __init__(self, pos=None, target=None):
		super(ChaserMob, self).__init__(path_to_image=os.path.join(cst.IMG_DIR, *["spritesheets", "chaser.png"]), pos=pos)
		self.target = target


	def update(self):
		# generic Mob update
		entity.Mob.update(self)
		
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

