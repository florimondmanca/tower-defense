# encoding=utf-8


# ------ Imports ------

import pygame

from copy import copy
import constants as cst
from isometric import isoutils

map_center = isoutils.iso_to_cart((cst.SCREEN_WIDTH//2, cst.SCREEN_HEIGHT//2))


class Message(pygame.sprite.Sprite):
	'''
	A class for manipulating text messages and bring them on screen easily.
	:param parent: the Surface on which the text is plotted.
	:param msg: the actual text to display.
	:param font=TEXT_FONT: font of the message.
	:param color: color of the message.
	'''
	def __init__(self, msg, center, font=cst.TEXT_FONT, color=cst.WHITE):
		self.text = msg
		self.font = font
		self.image = font.render(msg, True, color)
		self.rect = self.image.get_rect()
		self.rect.center = center

	def change_message(self, new_msg, font=cst.TEXT_FONT, color=cst.WHITE):
		self.text = new_msg
		self.image = font.render(new_msg, True, color)
		self.rect = self.image.get_rect(center=self.rect.center)

	def display(self, bliton=None):
		"""
		Brings the message on screen
		"""
		if bliton is None :
			bliton = pygame.display.get_surface()
		bliton.blit(self.image, self.rect)


class Button(pygame.sprite.Sprite):
	"""
	A clickable button which underlines itself when mouse hovers it
	:param text: the actual text to display.
	:param center: the center point of the button.
	:param font=TEXT_FONT: font of the button.
	:param color=WHITE: color of the button.
	"""
	def __init__(self, text, center, font=cst.TEXT_FONT, color=cst.WHITE):
		pygame.sprite.Sprite.__init__(self)
		self.text = text
		self.font = font
		self.image = font.render(text, True, color) 
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.hover = False  # True when mouse hovers the button
		self.color = color #color du type (r,g,b) avec 0<= r,g,b <= 255

	def update(self, bliton=None):
		"""
		Updates the button's state, especially deals with highlighting.
		"""
		if bliton is None :
			bliton = pygame.display.get_surface()	
		mouse_pos = pygame.mouse.get_pos()
		if not self.hover:
			if self.rect.collidepoint(mouse_pos):
				self.hover = True
		else:
			if not self.rect.collidepoint(mouse_pos):
				self.hover = False
		if self.hover:
			pygame.draw.line(bliton, self.color, self.rect.bottomright, self.rect.bottomleft)
		bliton.blit(self.image, self.rect)

	def get_color(self):
		"""
		Returns a color based on whether the button is highlit.
		"""
		color = self.color
		if self.hover:
			color += pygame.Color(70, 70, 70)
		return color

	def change_text(self, new_text, color=cst.WHITE):
		self.text = new_text
		self.image = self.font.render(new_text, True, color)
		self.rect = self.image.get_rect(center=self.rect.center)