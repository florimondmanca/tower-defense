# encoding=utf-8

# ------ Importations ------

import pygame

import constants as cst
from guiutils import load_image, Message, Button, GraphicButton, Cursor, Score
from tiles.map import Map
from entities import mob
from isometric import isoutils
import guiutils

# ------ Classe Principale ------

# key_to_function : simple mapping from keys to Instance's functions
key_to_function = {
	pygame.K_LEFT: lambda self: self.rotate_all_left(),
	pygame.K_RIGHT: lambda self: self.rotate_all_right(),
}

class Instance:
	"""
	Runs a game for testing isometric perspective
	"""
	def __init__(self, map_name="basic.map"):
		# init pygame, screen and clock
		pygame.init()
		self.screen = cst.SCREEN
		self.clock = pygame.time.Clock()
		self.screen_width = cst.SCREEN_WIDTH
		self.screen_height = cst.SCREEN_HEIGHT

		# init the map
		self.map = Map.import_map(map_name)
		self.matrix = [[None for j in range(2*cst.MAP_WIDTH)] for i in range(2*cst.MAP_HEIGHT)]

		# init the mobs
		self.mobs = pygame.sprite.Group()
		self.mobs.add(mob.ChaserMob(pos=(300, 400), target=self.map.tiles[1, 0]))

	def update(self):
		self.mobs.update()

	def rotate_all_left(self):
		"""
		Rotates the map, the mobs, etc 90° clockwise around the screen's center
		"""
		map_center_cart = isoutils.iso_to_cart((cst.SCREEN_WIDTH//2, cst.SCREEN_HEIGHT//2))
		for tile in self.map.tiles.values():
			tile.rotate_left(map_center_cart)
		for mob in self.mobs:
			mob.rotate_left(map_center_cart)
		for deco in self.map.deco:
			deco.rotate_left(map_center_cart)

	def rotate_all_right(self):
		"""
		Rotates the map, the mobs, etc 90° anti-clockwise around the screen's center
		"""
		map_center_cart = isoutils.iso_to_cart((cst.SCREEN_WIDTH//2, cst.SCREEN_HEIGHT//2))
		for tile in self.map.tiles.values():
			tile.rotate_right(map_center_cart)
		for mob in self.mobs:
			mob.rotate_right(map_center_cart)
		for deco in self.map.deco:
			deco.rotate_right(map_center_cart)

	def display(self):
		self.screen.fill(pygame.Color("white"))
		for tile in self.map.get_tiles():
			tile.display(self.screen)
		for deco in self.map.deco:
			deco.display(self.screen)
		for mob in self.mobs:
			mob.display(self.screen)
		# display turret

		if cst.DEBUG :
			# mid-screen lines
			pygame.draw.line(self.screen, pygame.Color("red"), (self.screen_width//2, 0), (self.screen_width//2, self.screen_height))
			pygame.draw.line(self.screen, pygame.Color("blue"), (0, self.screen_height//2), (self.screen_width, self.screen_height//2))

	def run(self):
		while True:
			self.clock.tick(cst.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return "PYGAME_QUIT"
				elif event.type == pygame.KEYDOWN:
					if event.key in key_to_function:
						key_to_function[event.key](self)

			self.update()
			self.display()
			pygame.display.flip()

	def pause(self):
		'''Runs the pause menu '''
		bg, bg_rect = load_image("bgpause.png")
		bg_rect.move_ip((100,100))
		resumeButton = Button("Resume Game", (400,150))
		menuButton = Button("Back to menu", (400,200))
		exitButton = Button("Quit Game", (400,250))

		done = False
		while not done :
			self.clock.tick(48)
			screen = pygame.display.get_surface()
			
			screen.blit(bg,bg_rect)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if menuButton.lit:
						return 0
					elif exitButton.lit :
						return 1
					elif resumeButton.lit :
						return 2
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
					return 2
			menuButton.update(screen)
			exitButton.update(screen)
			resumeButton.update(screen)

			pygame.display.flip()
