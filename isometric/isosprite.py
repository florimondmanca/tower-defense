import pygame
import constants as cst
from . import isoutils
import guiutils

class IsoSprite(pygame.sprite.Sprite):
	"""
	A basic class which implements isometric perspective into the pygame.sprite.Sprite class.
	IsoSprite(path_to_image, pos) -> IsoSprite
	Attributes :
		pos : sprite's position in cartesian space
		iso_pos : sprite's position in isometric (screen) space
		rect : sprite's image rect in isometric (screen) space
	Methods:
		display(screen) : Displays the sprite on the screen with isometric perspective.
	IMPORTANT : Only change IsoSprite's pos or iso_pos when trying to move the sprite (NOT THE ISOSPRITE'S RECT) as the rect attribute is not linked to pos or iso_pos. The rect is automatically moved when pos and iso_pos are modified.
	"""

	def __init__(self, path_to_image=cst.NONE_TILE_PATH, pos=None):
		super(IsoSprite, self).__init__()
		self.image, self.rect = guiutils.load_image(path_to_image)
		if pos is None:
			self._pos = [0, 0]  # in pixels on cartesian map
		else:
			self._pos = pos
		self._iso_pos = None  # in pixels on isometric (screen) map
		self._update_positions(pos=True)

	def get_pos(self):
		return self._pos

	def set_pos(self, new_pos):
		self._pos = new_pos
		self._update_positions(pos=True)

	pos = property(get_pos, set_pos)

	def get_iso_pos(self):
		return self._iso_pos

	def set_iso_pos(self, new_iso_pos):
		self._iso_pos = new_iso_pos
		self._update_positions(iso_pos=True)

	iso_pos = property(get_iso_pos, set_iso_pos)

	def _update_positions(self, pos=False, iso_pos=False):
		""" Keeps pos, iso_pos and rect up-to-date """
		if pos:  # self.pos just changed
			self._iso_pos = isoutils.cart_to_iso(self._pos)
			self.rect.center = self._iso_pos
		elif iso_pos:  # self.iso_pos just changed
			self._pos = isoutils.iso_to_cart(self._iso_pos)
			self.rect.center = self._iso_pos

	def display(self, screen):
		"""Displays the sprite on the screen in isometric perspective"""
		screen.blit(self.image, self.rect)