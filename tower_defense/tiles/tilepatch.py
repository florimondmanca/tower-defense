import os
import constants as CST
from . import utils

class TilePatch:
	"""
	An object representing a tile patch (that we shall stick to the map later on).
	Arguments are category (terrain, building, etc.) and tile_type (grass, roadNorth, wallRock, etc.). All tiles must be .png files.
	"""
	def __init__(self, category, tile_type):
		self.category = category
		self.tile_type = tile_type
		self.image, self.rect = utils.load_image(os.path.join(CST.IMG_DIR, *["tiles", category, tile_type+".png"]))

	def __str__(self):
		return "TilePatch: {}".format(self.tile_type)