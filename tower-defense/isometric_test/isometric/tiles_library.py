import os
from . import constants as cst
from . import utils

class TilePatch:
	"""
	An object representing a tile patch (that we shall stick to the map later on)
	"""
	def __init__(self, tile_path, tile_type):
		self.tile_type = tile_type
		self.image, self.rect = utils.load_image(tile_path)

	def __str__(self):
		return "TilePatch: {}".format(self.tile_type)


class TilesLibrary:
	"""
	Tiles library that contains all Tile Patches available from staitc/img/***tiles (eg: terrain_tiles)
	"""
	def __init__(self):
		print("\n-- LOADING : Tiles library --")

		# load terrain tiles
		print("Loading terrain tiles...")
		self.terrain_tiles = dict()
		for root, dirs, files in os.walk(os.path.join(cst.BASE_DIR, *["static", "img", "terrain_tiles"])):
			for f in files:
				if f.endswith(".png"):
					tile_type = f.replace(".png", "")
					self.terrain_tiles[tile_type] = TilePatch(tile_path=os.path.join(root, f), tile_type=tile_type)
		print("OK")

		print("-- LOADING FINISHED : Tiles library --")