import os
from . import constants as cst
from . import utils

# class TerrainTile:
# 	"""
# 	An object representing a terrain tile on the map.
# 	Attributes are :
# 		tile_type (string)
# 		pos (Cartesian position (x, y))
# 		iso_pos (Isometric position (iso_x, iso_y))
# 	"""
# 	pos = None  # (float, float)
# 	iso_pos = None  # (float, float)
# 	tile_type = "grass"  # string

# 	def __init__(self, tile_type=None, pos=None, iso_pos=None):
# 		# init positions from args
# 		self.pos = pos
# 		self.iso_pos = iso_pos
# 		# calculate final positions
# 		self._calculate_positions()
# 		# init tile type
# 		if tile_type is not None:
# 			self.tile_type = tile_type
# 		self.image, self.rect = utils.load_image(self.tile_type)

# 	def _calculate_positions(self):
# 		"""
# 		Calculates the final positions (cartesian and isometric). They should not change in the future.
# 		"""
# 		if self.pos is None:
# 			if self.iso_pos is None:
# 				self.pos = (0, 0)
# 				self.iso_pos = self.cart_to_iso(self.pos)
# 			else:
# 				self.pos = self.iso_to_cart(self.iso_pos)
# 		else:
# 			self.iso_pos = self.cart_to_iso(self.pos)

# 	def cart_to_iso(self, pos):
# 		return (pos[0] - pos[1], (pos[0] + pos[1])/2)

# 	def iso_to_cart(self):
# 		return ((2*pos[1] + pos[0]) 2, (2*pos[1] - pos[0])/2)

class TilePatch:
	"""
	An object representing a tile patch (that we shall stick to the map later on)
	"""
	def __init__(self, tile_path, tile_type):
		self.tile_type = tile_type
		self.image, self.rect = utils.load_image(tile_path)


class TileLibrary:
	"""
	An object that loads tiles and stores them.
	"""
	def __init__(self):
		self.terrain_tiles = self.init_tiles()  # dict

	def init_tiles(self):
		"""
		Loads all available tiles in dicts.
		Currently loads :
			terrain_tiles
		"""
		# load terrain tiles
		terrain_tiles = dict()
		for root, dirs, files in os.walk(os.path.join(cst.BASE_DIR, *["static", "img", "terrain_tiles"])):
			for f in files:
				if f.endswith(".png"):
					tile_type = f.replace(".png", "")
					terrain_tiles[tile_type] = TilePatch(tile_path=os.path.join(root, f), tile_type=tile_type)
		# (extend to load more categories of tile types)
		return terrain_tiles


class TestGame(object):
	"""
	Runs a game for testing isometric perspective
	"""
	def __init__(self):
		super(Viewer, self).__init__()
		# init pygame, screen and clock
		pygame.init()
		self.screen = pygame.display.set_mode(cst.SCREEN_SIZE)
		self.clock = pygame.time.Clock()
		self.map_width = cst.MAP_WIDTH
		self.map_height = cst.MAP_HEIGHT
		# init the tile library (containing all the tile patches)
		self.tlib = TileLibrary()
		# init the cartesian map (2D array as a dict)
		self.cartmap = [[self.tlib.terrain_tiles["grass"]) for x in range(self.map_width)] for y in range(self.map_height)]
		self.init_map()

	def init_map(self):
		self.cartmap[10][10] = self.cartmap[10][11] = self.tlib.terrain_tiles["bridgeNorth"]

	def update(self):
		pass

	def display(self):
		for x in range(self.map_width):
			for y in range(self.map_height):
				self.screen.blit(self.cartmap[x][y].image, pygame.Rect(cst.TILE_SIZE*x, cst.TILE_SIZE*y, TILE_SIZE, TILE_SIZE))

	def run(self):
		while True:
			self.clock.tick(cst.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return
			self.update()
			self.display()
			pygame.display.flip()

if __name__ == '__main__':
	v = Viewer()
	v.run()
