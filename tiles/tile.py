import os
import constants as cst
from .tileslibrary import tlib
from isometric.isosprite import IsoSprite

class Tile(IsoSprite):
	"""
	An IsoSprite representing a tile.
	"""
	def __init__(self, pos=None, category="none", tile_type=cst.NONE_TILE):
		super(Tile, self).__init__(pos=pos)
		self.image, self.rect = getattr(tlib, "{}_tiles".format(category))[tile_type]
		self.rect.center = self.iso_pos

	def change(self, category, tile_type):
		"""Changes the tile to a new category and tile_type"""
		self.image, self.rect = getattr(tlib, "{}_tiles".format(category))[tile_type]