import os
from . import constants as cst
from . import utils

class TilePatch:
	"""
	An object representing a tile patch (that we shall stick to the map later on)
	"""
	def __init__(self, category, tile_type):
		self.tile_type = tile_type
		self.image, self.rect = utils.load_image(os.path.join(BASE_DIR, *[category, tile_type]))

	def __str__(self):
		return "TilePatch: {}".format(self.tile_type)


class TilesLibrary:
	"""
	Tiles library that contains all Tile Patches available from staitc/img/***tiles (eg: terrain_tiles)
	"""
	def __init__(self):
		print("\n-- LOADING : Tiles library --")
		categories = ["terrain",]  # add more categories later on
		for cat in categories:
			print("Loading {} tiles...".format(cat))
			setattr(self, "{}_tiles".format(cat), dict())
			for root, dirs, files in os.walk(os.path.join(cst.BASE_DIR, *["static", "img", cat])):
				for f in files:
					if f.endswith(".png"):
						tile_type = f.replace(".png", "")
						self.terrain_tiles[tile_type] = TilePatch(category=cat, tile_type=tile_type)
			print("OK")

		print("-- LOADING FINISHED : Tiles library --")