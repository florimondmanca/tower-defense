import pygame
from . import constants as cst
from . import utils

class IsoSprite(pygame.sprite.Sprite):
	"""
	A very basic class which implements isometric perspective to the pygame.sprite.Sprite baseclass.
	IsoSprite has a pos and rect in Cartesian space, and an iso_pos and iso_rect in Isometric space.
	Modifying any of those (eg s.pos = (4, 0)) changes the other position or rect if necessary, in a cycle :
	pos -> iso_pos -> iso_rect -> rect -> pos ...
	"""

	def __init__(self, path_to_image, pos=None):
		super(IsoSprite, self).__init__()
		self.image, self.iso_rect = utils.load_image(path_to_image)
		if pos is None:
			self._pos = [0, 0]  # in pixels on cartesian map
		else:
			self._pos = pos

	def get_pos(self):
		return self._pos

	def set_pos(self, new_pos):
		self._pos = new_pos
		self.update_positions(pos=True)

	def update_positions(self, pos=False, iso_pos=False):
		if pos:  # self.pos just changed
			self._iso_pos = utils.cart_to_iso(self._pos)
			self.rect.center = self._iso_pos
		if iso_pos:  # self.iso_pos just changed
			self._pos = utils.iso_to_cart(self._iso_pos)
			self.rect.center = self._iso_pos

	def display(self, screen):
		"""Displays the sprite on the screen in isometric perspective"""
		iso_x, iso_y = utils.cart_to_iso(self.pos)
		iso_x, iso_y = utils.cart_to_iso(self.pos)
		rect = self.rect
		rect.centerx = iso_x + screen.get_width()//2
		rect.centery = iso_y + screen.get_height()//2
		screen.blit(self.image, rect)