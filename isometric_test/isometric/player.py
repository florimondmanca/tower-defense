import os
import pygame
from . import constants as cst
from . import utils
from .isosprite import IsoSprite

sqrt2 = 1.41421

# class Mob(pygame.sprite.Sprite):
# 	"""
# 	A mob that can move on the map.
# 	Initial position must be given in terms of pixels.
# 	"""
# 	def __init__(self, pos=None):
# 		super(Mob, self).__init__()
# 		if pos is None:
# 			self.pos = [0, 0]
# 		else:
# 			self.pos = pos
# 		self.image, self.rect = utils.load_image(os.path.join(cst.IMG_DIR, *["characters", "mob_test.png"]))
# 		self.speed = 5
	
# 	def update(self):
# 		"""
# 		Moves the mob according to the keys being pressed.
# 		"""
# 		# find keys
# 		keys = pygame.key.get_pressed()
# 		right = keys[pygame.K_RIGHT]
# 		left = keys[pygame.K_LEFT]
# 		up = keys[pygame.K_UP]
# 		down = keys[pygame.K_DOWN]
# 		# build velocity
# 		velocity = [0, 0]
# 		if right:
# 			velocity[0] += self.speed
# 		if left:
# 			velocity[0] += -self.speed
# 		if up:
# 			velocity[1] += -self.speed
# 		if down:
# 			velocity[1] += self.speed
# 		# diagonal speeding effects
# 		if up and right or up and left or down and right or down and left:
# 			velocity[0] /= 1.2
# 			velocity[1] /= 1.2
# 		if up and right or down and left:
# 			velocity[0] /= sqrt2
# 			velocity[1] /= sqrt2
# 		# move pos and rect
# 		self.pos[0] += velocity[0]
# 		self.pos[1] += velocity[1]
# 		self.rect.center = self.pos

# 	def display(self, screen):
# 		iso_x, iso_y = utils.cart_to_iso(self.pos)
# 		rect = self.rect
# 		rect.centerx = iso_x + screen.get_width()//2
# 		rect.centery = iso_y + screen.get_height()//2
# 		screen.blit(self.image, rect)

class Mob(IsoSprite):
	"""
	A mob that can move on the map.
	Initial position must be given in terms of pixels.
	"""
	def __init__(self, pos=None):
		path_to_image = os.path.join(cst.IMG_DIR, *["characters", "mob_test.png"])
		super(Mob, self).__init__(path_to_image=path_to_image, pos=pos)
		self.speed = 5
	
	def update(self):
		"""
		Moves the mob according to the keys being pressed.
		"""
		# find keys
		keys = pygame.key.get_pressed()
		right = keys[pygame.K_RIGHT]
		left = keys[pygame.K_LEFT]
		up = keys[pygame.K_UP]
		down = keys[pygame.K_DOWN]
		# build velocity
		velocity = [0, 0]
		if right:
			velocity[0] += self.speed
		if left:
			velocity[0] += -self.speed
		if up:
			velocity[1] += -self.speed
		if down:
			velocity[1] += self.speed
		# diagonal speeding effects
		if up and right or up and left or down and right or down and left:
			velocity[0] /= 1.2
			velocity[1] /= 1.2
		if up and right or down and left:
			velocity[0] /= sqrt2
			velocity[1] /= sqrt2
		# update position accordingly
		self.pos = [self.pos[0] + velocity[0], self.pos[1] + velocity[1]]
