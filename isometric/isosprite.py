import pygame
import constants as cst
from . import isoutils
import guiutils

class IsoSprite(pygame.sprite.Sprite):
	"""
	A very basic class which implements isometric perspective to the pygame.sprite.Sprite baseclass.
	pos is the sprite's position in the cartesian space
	iso_pos is the sprite's position in the isometric (screen) space
	rect is the sprite's rect **in isometric (screen) space**
	"""

	def __init__(self, path_to_image=cst.NONE_TILE_PATH, pos=None):
		super(IsoSprite, self).__init__()
		self.image, self.rect = guiutils.load_image(path_to_image)
		if pos is None:
			self._pos = [0, 0]  # in pixels on cartesian map
		else:
			self._pos = pos
		self._iso_pos = None  # in pixels on isometric (screen) map
		self.update_positions(pos=True)

	def get_pos(self):
		return self._pos

	def set_pos(self, pos):
		self._pos = pos
		self.update_positions(pos=True)

	pos = property(get_pos, set_pos)

	def get_iso_pos(self):
		return self._iso_pos

	def set_iso_pos(self, iso_pos):
		self._iso_pos = iso_pos
		self.update_positions(iso_pos=True)

	iso_pos = property(get_pos, set_pos)

	def update_positions(self, pos=False, iso_pos=False):
		if pos:  # self.pos just changed
			self._iso_pos = isoutils.cart_to_iso(self._pos)
			self.rect.center = self._iso_pos
		elif iso_pos:  # self.iso_pos just changed
			self._pos = isoutils.iso_to_cart(self._iso_pos)
			self.rect.center = self._iso_pos

	def display(self, screen):
		"""Displays the sprite on the screen in isometric perspective"""
		rect = self.rect
		rect.centerx += screen.get_width()//2
		rect.centery += screen.get_height()//2
		screen.blit(self.image, rect)