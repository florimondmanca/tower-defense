import os
import pygame
from . import constants as cst
from . import utils


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


class TestGame:
	"""
	Runs a game for testing isometric perspective
	"""
	def __init__(self):
		# init pygame, screen and clock
		pygame.init()
		self.screen = pygame.display.set_mode(cst.SCREEN_SIZE)
		self.clock = pygame.time.Clock()
		self.screen_width = cst.SCREEN_WIDTH
		self.screen_height = cst.SCREEN_HEIGHT
		self.map_width = cst.MAP_WIDTH
		self.map_height = cst.MAP_HEIGHT
		# init the tile library (containing all the tile patches)
		self.tlib = TileLibrary()
		# init the cartesian map (2D array as a dict)
		self.cartmap = [[self.tlib.terrain_tiles["grass"] for x in range(self.map_width)] for y in range(self.map_height)]
		self.init_map()

	def init_map(self):
		self.cartmap[10][10] = self.cartmap[10][11] = self.tlib.terrain_tiles["bridgeNorth"]

	def update(self):
		pass

	def display(self):
		self.screen.fill(pygame.Color("white"))
		for x in range(self.map_width):
			for y in range(self.map_height):
				cart_x = cst.TILE_SIZE*x
				cart_y = cst.TILE_SIZE*y
				iso_x = self.screen_width//2 + (cart_x - cart_y)
				iso_y = self.screen_height//2 + (cart_x + cart_y)/2
				rect = pygame.Rect(iso_x, iso_y, cst.TILE_SIZE/2, cst.TILE_SIZE)
				self.screen.blit(self.cartmap[x][y].image, rect)

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
