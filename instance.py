# encoding=utf-8

# ------ Importations ------

import pygame

import constants as cst
from guiutils import load_image, Message, Button, GraphicButton, Cursor, Score
from tiles.map import *
from entities import mob

# ------ Classe Principale ------

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
		self.mobs = pygame.sprite.Group()
		self.mobs.add(mob.ChaserMob(pos=(300, 400), target=self.map[1, 0]))

	def update(self):
		self.mobs.update()

	def display(self):
		self.screen.fill(pygame.Color("white"))
		for tile in self.map:
			tile.display(self.screen)

		# mid-screen lines (optional, just for landmark)
		pygame.draw.line(self.screen, pygame.Color("red"), (self.screen_width//2, 0), (self.screen_width//2, self.screen_height))
		pygame.draw.line(self.screen, pygame.Color("blue"), (0, self.screen_height//2), (self.screen_width, self.screen_height//2))

		# display mobs
		for mob in self.mobs:
			mob.display(self.screen)



	def run(self):
		while True:
			self.clock.tick(cst.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return "PYGAME_QUIT"
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