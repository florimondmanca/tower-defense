import os
import pygame
from . import constants as cst
from . import utils
from .tileslibrary import tlib
from .tilepatch import TilePatch
from .map import Map
from .player import Mob


class TestGame:
	"""
	Runs a game for testing isometric perspective
	"""
	def __init__(self, map_name):
		# init pygame, screen and clock
		pygame.init()
		self.screen = cst.SCREEN
		self.clock = pygame.time.Clock()
		self.screen_width = cst.SCREEN_WIDTH
		self.screen_height = cst.SCREEN_HEIGHT
		self.mobs = pygame.sprite.Group()
		# init the map
		self.map = Map.import_map(map_name)
		#self.map = Map.create_plain("grass", 10, 10); self.init_map()
		self.init_mobs()

	def init_map(self):
		# only used for testing
		self.map[0, 0] = "roadCornerNW"
		self.map[0, 1] = cst.NONE_TILE

	def init_mobs(self):
		self.mobs.add(Mob())

	def update(self):
		self.mobs.update()

	def display(self):
		self.screen.fill(pygame.Color("white"))
		# display the map
		for y in range(self.map.height):
			for x in range(self.map.width):
				iso_x, iso_y = utils.tile_to_iso(x, y)
				rect = pygame.Rect(0, 0, self.map[x, y].rect.width, self.map[x, y].rect.height)
				rect.centerx = iso_x + self.screen_width//2
				rect.centery = iso_y + self.screen_height//2
				self.screen.blit(self.map[x, y].image, rect)

		# display the mobs
		for mob in self.mobs:
			mob.display(self.screen)

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
