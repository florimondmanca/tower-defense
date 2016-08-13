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
	Methods:
		display(screen): Displays the sprite on the screen with isometric perspective.
		rotate_left(map_center): Rotates the sprite by 90° clockwise around the map_center.
		rotate_right(map_center): Rotates the sprite by 90° anti-clockwise around the map_center.
	IMPORTANT : You can only access the IsoSprite's rect and iso_rect, not modify them directly. To modify, use set_rect and set_iso_rect methods.
	"""

	def __init__(self, path_to_image=cst.NONE_TILE_PATH, pos=None):
		# initialize from Sprite
		pygame.sprite.Sprite.__init__(self)
		# initialize position (in cartesian space) and iso-position (in screen space)
		if pos is None:
			self._pos = [0, 0]  # in pixels on cartesian map
		else:
			self._pos = pos
		self._iso_pos = None  # in pixels on isometric (screen) map
		# get the image, iso_rect and rect
		self.image, self._iso_rect = guiutils.load_image(path_to_image)
		self._rect = pygame.Rect((0, 0), isoutils.iso_to_cart(self.iso_rect.size))  # rect on cartesian map, used for collisions
		self._update_positions(new_pos=True)

	# protect the pos attribute to help updating iso_pos, rect and iso_rect
	def get_pos(self):
		return self._pos

	def set_pos(self, new_pos):
		self._pos = new_pos
		self._update_positions(new_pos=True)

	pos = property(get_pos, set_pos)

	# protect the iso_pos attribute to help updating pos, rect and iso_rect
	def get_iso_pos(self):
		return self._iso_pos

	def set_iso_pos(self, new_iso_pos):
		self._iso_pos = new_iso_pos
		self._update_positions(new_iso_pos=True)

	iso_pos = property(get_iso_pos, set_iso_pos)

	# don't allow direct modifying of rect
	@property
	def rect(self):
		return self._rect

	def set_rect(self, new_rect):
		self._rect = new_rect

	# don't allow direct modifying of iso_rect
	@property
	def iso_rect(self):
		return self._iso_rect

	def set_iso_rect(self, new_iso_rect):
		self._iso_rect = new_iso_rect

	def _update_positions(self, new_pos=False, new_iso_pos=False):
		""" Keeps pos, iso_pos, rect and iso_rect up-to-date """
		if new_pos:  # self.pos just changed
			self._iso_pos = isoutils.cart_to_iso(self._pos)
			self._rect.center = self._pos
			self._iso_rect.center = self._iso_pos
		elif new_iso_pos:  # self.iso_pos just changed
			self._pos = isoutils.iso_to_cart(self._iso_pos)
			self._rect.center = self._pos
			self._iso_rect.center = self._iso_pos

	def display(self, screen = pygame.display.get_surface()):
		"""Displays the sprite on the screen in isometric perspective"""
		screen.blit(self.image, self._iso_rect)

	def rotate_left(self, map_center):
		"""
		Rotates the sprite by 90° clockwise around the map center.
		"""
		self.pos = guiutils.rotate_left(self.pos, map_center)

	def rotate_right(self, map_center):
		"""
		Rotates the sprite by 90° anti-clockwise around the map center.
		"""
		self.pos = guiutils.rotate_right(self.pos, map_center)

	def __str__(self):
		return "IsoSprite(pos={}, rect={}".format(self._pos, self._rect)

	def __repr__(self):
		return self.__str__()