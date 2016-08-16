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
		self.msg = menugui.Message(msg, pos)
		self.l = self.msg.rect.right + 5

		self.val = value
		self.val_msg = Message(str(value), pos)
		self.val_msg.rect.left = self.l

		self.pos = pos

	def update(self, val=None):
		if val is not None and val != self.val :
			self.val_msg.changeMessage(str(val))


	def display(self, screen = pygame.display.get_surface()):
		self.val_msg.display(screen)
		self.msg.display(screen)


class TurretBar:
	''' La barre de selection des tourelles en haut de l'écran'''

	def __init__(self):
		self.bgimg,self.bgrect = miscgui.load_image(os.path.join(cst.IMG_DIR, *["gui","bar.png"]))
		self.bgrect.topleft = (0,0)
		self.turrets = pygame.sprite.Group()
		self.turrets.add(GraphicButton((30,cst.ST_Y), None))
		self.turrets.add(GraphicButton((30,cst.LT_Y), None, large = True))

		self.turrets.add(GraphicButton((102,cst.ST_Y), None))
		self.turrets.add(GraphicButton((102,cst.LT_Y), None, large = True))

		self.turrets.add(GraphicButton((174,cst.ST_Y), None))
		self.turrets.add(GraphicButton((174,cst.LT_Y), None, large = True))

	def update(self, mouse_pos, mouse_click):
		if mouse_click :
			for tur in self.turrets :
				tur.selected = False
		self.turrets.update(mouse_pos, mouse_click)

	def display(self,screen = pygame.display.get_surface()):
		screen.blit(self.bgimg,self.bgrect)
		for t in self.turrets :
			t.display(screen)


class DescriptionWindow:
	"""
	A small window that displays every information about a turret. Linked to a GraphicButton class.
	DescriptionWindow(self, datas) -> DescriptionWindow
		datas = a dict containing entries "preview","title","descr","price", "large"
	"""
	def __init__(self, datas):
		self.bg, self.bg_rect = miscgui.load_image(os.path.join(cst.IMG_DIR, *["gui","desc.png"]))
		self.bg_rect.topleft = (2,102)
		self.dict = datas
		self.font = cst.GUI_TURRET_FONT

	def display(self,screen = pygame.display.get_surface()):
		screen.blit(self.bg, self.bg_rect)

		prev,prev_rect = self.dict["preview"]
		prev_rect.topleft = (8,108)
		screen.blit(prev,prev_rect)

		title = self.font.render(self.dict["title"], True, cst.PAPER)
		title_rect = title.get_rect()
		title_rect.topleft = (50,108)
		screen.blit(title,title_rect)


class GraphicButton(pygame.sprite.Sprite):
	'''Bouton de selection d'une tourelle dans la GUI '''

	def __init__(self, topleft, data_number, large = False):
		pygame.sprite.Sprite.__init__(self)

		self.data = None #La tourelle associée au bouton

		# Image réelle de la tourelle
		if large :
			self.preview, self.rect =  miscgui.load_image(os.path.join(cst.IMG_DIR, *["turrets", "test_large.png"])) 
		else :
			self.preview, self.rect =  miscgui.load_image(os.path.join(cst.IMG_DIR, *["turrets", "test.png"])) 
		self.rect.topleft = topleft
		
		self.title = "Test"
		self.price = "100"
		self.descr = "This is a test to prove that penguins actually don't exist anymore"

		d = dict([("title",self.title), ("price",self.price),("descr",self.descr),("preview",(copy(self.preview),copy(self.rect)))])
		self.description_window = DescriptionWindow(d)

		self.hover = False
		self.selected = False

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
		screen.blit(self.preview, self.rect)
		if self.hover :
			self.description_window.display(screen)
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
		self.next_wave = menugui.Button("Next Wave", (0,0), font=cst.TEXT_FONT, color=cst.RED)
		self.next_wave.rect.bottomright = (1270,710)

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
