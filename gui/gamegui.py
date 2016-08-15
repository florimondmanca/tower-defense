# encoding=utf-8


# ------ Imports ------

import pygame
import os

from copy import copy
import constants as cst
from isometric import isoutils
from . import miscgui,menugui

map_center = isoutils.iso_to_cart((cst.SCREEN_WIDTH//2, cst.SCREEN_HEIGHT//2))

class Score:
	def __init__(self, msg, pos, value=0):
		self.msg = Message(msg, pos)
		self.l = self.msg.rect.right + 5

		self.val = value
		self.val_msg = Message(str(value), pos)
		self.val_msg.rect.left = self.l

		self.pos = pos

	def update(self, bliton, val=None):
		if val != None and val != self.val :
			self.val_msg.changeMessage(str(val))
		self.val_msg.display(bliton)
		self.msg.display(bliton)


class TurretBar:
	''' La barre de selection des tourelles en haut de l'écran'''

	def __init__(self):
		self.bgimg,self.bgrect = miscgui.load_image(os.path.join(cst.IMG_DIR, *["gui","bar.png"]))
		self.bgrect.topleft = (0,0)
		self.turrets = pygame.sprite.Group()
		self.turrets.add(GraphicButton((30,20), None))
		self.turrets.add(GraphicButton((102,20), None))
		self.turrets.add(GraphicButton((174,20), None))

	def update(self, mouse_pos, mouse_click):
		if mouse_click :
			for tur in self.turrets :
				tur.selected = False
		self.turrets.update(mouse_pos, mouse_click)

	def display(self,screen = pygame.display.get_surface()):
		screen.blit(self.bgimg,self.bgrect)
		for t in self.turrets :
			t.display(screen)



class GraphicButton(pygame.sprite.Sprite):
	'''Bouton de selection d'une tourelle dans la GUI '''

	def __init__(self, topleft, data_number, font=cst.GUI_TURRET_FONT):
		pygame.sprite.Sprite.__init__(self)

		self.data = None #La tourelle associée au bouton
		self.preview, self.preview_rect =  miscgui.load_image(os.path.join(cst.IMG_DIR, *["turrets", "test.png"])) # Image réelle de la tourelle

		self.preview_rect.topleft = topleft

		self.font = cst.GUI_TURRET_FONT
		
		self.text = "Test"
		self.text_rect = font.render(self.text, True, cst.WHITE).get_rect()
		self.text_rect.midtop = (self.preview_rect.midbottom[0], self.preview_rect.midbottom[1]+5)
		
		self.price = "100"
		self.price_rect = font.render(self.price, True, cst.PAPER).get_rect()
		self.price_rect.midtop = (self.text_rect.midbottom[0], self.text_rect.midbottom[1]+5)

		self.hover = False
		self.selected = False

		self.rect = self.preview_rect.union(self.text_rect).union(self.price_rect)


	def get_color(self, color):
		"""
		Returns a color based on whether the button is highlit.
		"""
		r, g, b = color
		if self.hover:
			r = max(r-90, 0)
			g = max(g-70, 0)
			b = max(b-70, 0)
		return (r, g, b)


	def update(self, mouse_pos, mouse_click):
		if not self.hover:
			if self.rect.collidepoint(mouse_pos):
				self.hover = True
		else:
			if not self.rect.collidepoint(mouse_pos):
				self.hover = False
		if mouse_click :
			if not self.selected :
				if self.rect.collidepoint(mouse_pos) :
					self.selected = True
			else :
				if self.rect.collidepoint(mouse_pos) :
					self.selected = False


	def display(self, screen = pygame.display.get_surface()):
		screen.blit(self.preview, self.preview_rect)
		
		text = self.font.render(self.text, True, self.get_color(cst.PAPER))
		screen.blit(text,self.text_rect)

		price = self.font.render(self.price, True, self.get_color(cst.PAPER))
		screen.blit(price,self.price_rect)

		if self.selected :
			miscgui.draw_frame(screen, self.rect, cst.YELLOW)

class GUI:
	"""
	The class that deals with the GUI of the game.
	Handles the top turret selector, the score, and various buttons
	"""

	def __init__(self):
		self.turret_bar = TurretBar()
		self.score = None
		self.money = None
		self.next_wave = menugui.Button("Next Wave", (1100,30), font=cst.TEXT_FONT, color=cst.WHITE)

	def update(self, mouse_pos, mouse_click):
		self.turret_bar.update(mouse_pos, mouse_click)
		self.next_wave.update(mouse_pos)

	def display(self,screen = pygame.display.get_surface()):
		self.turret_bar.display(screen)
		self.next_wave.display(screen)


class Cursor(pygame.sprite.Sprite):
	"""
	A textual cursor which will follow the mouse's moves.
	:param parent: the Surface which the cursor belongs to.
	:param font=TEXT_FONT: the text font.
	:param color=blue: the text color.
	"""
	def __init__(self, parent):
		self.pos = (0, 0)
		self.parent = parent
		self.cursor_image, self.cursor_rect = load_image("cursor.png")
		self.selected = None
		self.image, self.rect = self.cursor_image, self.cursor_rect

	def select(self, obj=None):
		if obj is None:
			self.selected = None
			self.image, self.rect = self.cursor_image, self.cursor_rect
		else :
			self.selected = obj
			self.image, self.rect = load_image(self.selected.preview)

	def update(self, mouse_pos, bliton=None):
		"""
		Updates the cursor's state, especially brings it to the position of the
		mouse.
		"""
		if bliton == None :
			bliton = pygame.display.get_surface()
		x,y = mouse_pos
		self.rect.topleft = ((x//10)*10, (y//10)*10)
		if x+self.rect.width < 601 and x>self.rect.width//2:
			self.parent.blit(self.image, self.rect)
