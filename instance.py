# encoding=utf-8

# ------ Importations ------

import pygame
from time import time
import constants as cst
from gui import miscgui, gamegui
from tiles.map import Map
from entities import moblist,turretlist,mainTurret
from isometric import isoutils
from gui import *

# ------ Classe Principale ------

# key_to_function : simple mapping from keys to Instance's functions
key_to_function = {
	pygame.K_LEFT: lambda self: self.rotate_all("left"),
	pygame.K_RIGHT: lambda self: self.rotate_all("right"),
	pygame.K_ESCAPE : lambda self: self.quit()
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

		# init the GUI
		self.gui = gamegui.GUI()

		# init the map
		self.map = Map.import_map(map_name)
		self.matrix = [[None for j in range(2*cst.MAP_WIDTH)] for i in range(2*cst.MAP_WIDTH)]

		self.player = mainTurret.MainTurret()
		self.turrets = [self.player]
		
		# init the mobs
		self.mobs = pygame.sprite.Group()
		self.mobs.add(moblist.ChaserMob(tile_pos=(9, 12), target=self.map.tiles[1, 0]))

		self.RUNNING = True

	def update(self, mouse_pos, mouse_click):
		self.mobs.update()
		self.gui.update(mouse_pos, mouse_click)

	def rotate_all(self, direction):
		""" Rotates the map by 90 degrees (clockwise if direction is 'left', counter-clockwise if direction is 'right') """
		func = "rotate_{}".format(direction)
		for tile in self.map.tiles.values():
			getattr(tile, func)()
		for mob in self.mobs:
			getattr(mob, func)()
		for deco in self.map.deco:
			getattr(deco, func)()
		for turret in self.turrets:
			getattr(turret, func)()

	def display(self):
		self.screen.fill(cst.PAPER)
		for tile in self.map.get_tiles():
			tile.display(self.screen)
		for deco in self.map.deco:
			deco.display(self.screen)
		for mob in self.mobs:
			mob.display(self.screen)
		for turret in self.turrets:
			turret.display(self.screen)
		self.gui.display(self.screen)

		# DEBUG
		if cst.DEBUG :
			# mid-screen lines
			pygame.draw.line(self.screen, pygame.Color("red"), (self.screen_width//2, 0), (self.screen_width//2, self.screen_height))
			pygame.draw.line(self.screen, pygame.Color("blue"), (0, self.screen_height//2), (self.screen_width, self.screen_height//2))

	def run(self):
		while self.RUNNING:
			mouse_click = False
			mouse_pos = pygame.mouse.get_pos()
			self.clock.tick(cst.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return "PYGAME_QUIT"
				elif event.type == pygame.KEYDOWN:
					if event.key in key_to_function:
						key_to_function[event.key](self)
				elif event.type == pygame.MOUSEBUTTONDOWN :
					mouse_click = True

			self.update(mouse_pos, mouse_click)
			self.display()
			pygame.display.flip()

	def quit(self):
		self.RUNNING = False

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
