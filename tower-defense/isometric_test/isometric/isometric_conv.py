import os
import pygame
from . import constants as cst
from . import utils
from . import tiles_library as tlib


class Map:
	"""
	Represents a 2D map made out of tiles.
	"""
	def __init__(self, width=5, height=5):
		self.width = 5
		self.height = 5
		self.tiles = [[tlib.terrain_tiles["none"] for y in range(height)] for x in range(width)]

	@classmethod
	def create_plain(tile_type, width, height):
		new_map = Map(width=width, height=height)
		for x in range(width):
			for y in range(height):
				new_map.tiles[x][y] = tlib.terrain_tiles[tile_type]
		return new_map

	@classmethod
	def import_map(map_name):
		""" Imports a map 'map_name' from the static/maps folder. """
		pass
		#with open(os.path.join(cst.MAPS_DIR, map_name), 'r') as mapfile:

	def __getitem__(self, pos):
		""" Allows direct access to the tiles, e.g. some_map[x, y] instead of some_map.tiles[x][y]. If y is not passed (some_map[x]), returns the complete row some_map.tiles[x]. """
		if isinstance(pos, tuple):
			x, y = pos
			return self.tiles[x][y]
		else:
			return self.tiles[pos]

	def __setitem__(self, pos, tile_type, tile_category="terrain_tiles"):
		""" Allows direct replacement of a tile using its tile_type, i.e. a string value. Looks for tile_type in the tlib.<tile_category> dictionnary.
		If pos is a (x, y) tuple, changes the tile at (x, y).
		If only x is passed, changes the whole row to the given tile. """
		if isinstance(pos, tuple):
			x, y = pos
			self.tiles[x][y] = getattr(tlib, tile_category)[tile_type]
		else:
			x = pos
			for y in range(self.height):
				self.tiles[x][y] = getattr(tlib, tile_category)[tile_type]

	def __iter__(self):
		""" Iterates over the map tiles, in descending depth (y) order. """
		for y in range(self.height):
			for x in range(self.width):
				yield self.tiles[x][y]


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
		# init the cartesian map (2D array as a dict)
		self.map = Map.create_plain("grass", cst.MAP_WIDTH, cst.MAP_HEIGHT)
		self.init_map()

	def init_map(self):
		self.map[0, 0] = "bridgeNorth"
		self.map[0, 1] = "water"

	def update(self):
		pass

	def display(self):
		self.screen.fill(pygame.Color("white"))

		for y in range(self.map.height):
			for x in range(self.map.width):
				cart_x = cst.TILE_SIZE * x
				cart_y = cst.TILE_SIZE * y
				iso_x = (cart_x - cart_y)
				iso_y = (cart_x + cart_y)/2
				rect = pygame.Rect(0, 0, self.map[x, y].rect.width, self.map[x, y].rect.height)
				rect.centerx = iso_x + self.screen_width//2
				rect.centerx = iso_y + self.screen_height//2
				self.screen.blit(self.map[x, y].image, rect)

		# mid-screen lines (optional, just for landmark)
		pygame.draw.line(self.screen, pygame.Color("red"), (self.screen_width//2, 0), (self.screen_width//2, self.screen_height))
		pygame.draw.line(self.screen, pygame.Color("blue"), (0, self.screen_height//2), (self.screen_width, self.screen_height//2))

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
