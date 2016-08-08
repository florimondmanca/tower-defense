# encoding=utf-8

# ------ Importations ------

import pygame

from .filefinder import load_image
from .constants import *
from .classes_utilities import Message, Button, GraphicButton, Cursor
from .importation import import_level, import_mob , import_turrets

# ------ Classe Principale ------

class Instance:
	'''
	The main class of the game
	'''
	def __init__(self,n=1):
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((800,600))

		self.cursor = Cursor(self.screen)

		# Données de la zone de jeu
		self.bg, self.bg_rect = load_image("bggz.png")
		
		self.data = import_level(n)
		wall = load_image("wall.png")

		self.walls = []
		for i in range(60) :
			for j in range(60) :
				if self.data[i][j]== 1 : # un mur
					self.walls.append((wall[0], wall[1].move((10*i,10*j))))

		self.turrets = []

		# Données du GUI
		self.gui, self.gui_rect = load_image("gui.png")
		self.gui_rect.move_ip((600,0))

		self.startButton = Button("Next Wave", (700,580))

		self.money = 1000
		self.wave = 0
		self.lives = 10

		self.livesMsg = Score("lives: ", (670,15))
		self.moneyMsg = Score("money: ", (670,35))
		self.waveMsg = Score("wave: ", (662,55))

		self.turret_buttons = import_turrets()

		self.level = n

	def update(self, left_click=False):
		'''
		Updates the game's state
		'''
		bliton = pygame.display.get_surface()
		(x, y) = pygame.mouse.get_pos()
		xc,yc = 10*(x//10), 10*(y//10)
		# Update de la zone de jeu

		bliton.blit(self.bg,self.bg_rect)
		if left_click and x<601 : #on a cliqué sur la zone de jeu : on pose la tourelle selectionnée
			if self.cursor.selected != None :
				if self.money > self.cursor.selected.data.price :
					self.money -= self.cursor.selected.data.price
					new_turret = self.cursor.selected.data
					new_turret.init_pos((xc,yc))
					self.turrets.append(new_turret)

					# prise en compte de la hitbox de la tourelle dans les chemins
					self.data[yc][xc] = 1
					if new_turret.size > 1 :
						self.data[yc][xc+1] = 1
						self.data[yc+1][xc+1] = 1
						self.data[yc+1][xc] = 1
					if new_turret.size > 2 :
						self.data[yc][xc+2] = 1
						self.data[yc+1][xc+2] = 1
						self.data[yc+2][xc+2] = 1
						self.data[yc+2][xc] = 1
						self.data[yc+2][xc+1] = 1


		for w in self.walls :
			bliton.blit(w[0],w[1])

		for t in self.turrets :
			t.update(bliton)

		# Update du GUI
		bliton.blit(self.gui,self.gui_rect)

		self.startButton.update(bliton)

		self.livesMsg.update(bliton, self.lives)
		self.moneyMsg.update(bliton, self.money)
		self.waveMsg.update(bliton, self.wave)

		for b in self.turret_buttons :
			b.update(bliton)

		# Update du curseur
		self.cursor.update((x,y),bliton)

	def run_wave(self,n):
		'''
		Boucle de jeu du mode "wave" 
		'''
		mob_list = import_mob(self.level,n)
		done = False
		while not done :
			# boucle principale de jeu
			self.clock.tick(fps)

			self.update()

			#3 flip
			pygame.display.flip()
			return

	def run(self):
		'''
		Boucle de jeu du mode "édition"
		'''
		done = False
		while not done:

			# Remise à zéro des variables de boucle
			self.clock.tick(fps)
			left_click = False

			# Gestion des événements
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					left_click = True
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					self.cursor.select()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
					test = self.pause()
					if test == 0 :
						return
					elif test == 1 :
						pygame.quit()

			# Gestion des actions
			if left_click :
				if self.startButton.lit :
					self.wave += 1
					self.run_wave(self.wave)
				for x in self.turret_buttons :
					if x.lit :
						self.cursor.select(x)
			
			# Mise à jour des données et affichage
			self.update(left_click)

			# Flip
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


