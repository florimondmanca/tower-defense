import os
from . import constants as cst

class TilePatch:
	"""
	An object representing a tile patch (that we shall stick to the map later on)
	"""
	def __init__(self, tile_path, tile_type):
		self.tile_type = tile_type
		self.image, self.rect = utils.load_image(tile_path)

	def __str__(self):
		return "TilePatch: {}".format(self.tile_type)


print("\n-- LOADING : Tiles library --")

# load terrain tiles
print("Loading terrain tiles...")
terrain_tiles = dict()
for root, dirs, files in os.walk(os.path.join(cst.BASE_DIR, *["static", "img", "terrain_tiles"])):
	for f in files:
		if f.endswith(".png"):
			_tile_type = f.replace(".png", "")
			terrain_tiles[tile_type] = TilePatch(tile_path=os.path.join(root, f), tile_type=tile_type)
print("OK")

print("-- LOADING FINISHED : Tiles library --")