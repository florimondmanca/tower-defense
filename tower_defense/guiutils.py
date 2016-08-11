# encoding=utf-8


# ------ Imports ------

import pygame
from os import getcwd
p = getcwd()

from copy import copy
import constants as cst

def load_image(path_to_image):
    """
    Loads the image using the full path to the image.
    Manages alpha conversion (e.g. png's).
    """
    image = pygame.image.load(path_to_image)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image, image.get_rect()


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

	def changeMessage(self, newMsg, font=cst.TEXT_FONT, color=cst.WHITE):
		self.text = newMsg
		self.image = font.render(newMsg, True, color)
		self.rect = self.image.get_rect(center=self.rect.center)

	def display(self, bliton=None):
		"""
		Brings the message on screen
		"""
		if bliton == None :
			bliton = pygame.display.get_surface()
		bliton.blit(self.image, self.rect)

class Score:
	def __init__(self, msg, pos, value = 0):
		self.msg = Message(msg, pos)
		self.l = self.msg.rect.right+5

		self.val = value
		self.val_msg = Message(str(value), pos)
		self.val_msg.rect.left = self.l

		self.pos = pos

	def update(self, bliton, val= None):
		if val != None and val != self.val :
			self.val_msg.changeMessage(str(val))

		self.val_msg.display(bliton)
		self.msg.display(bliton)


class Button:
	"""
	A clickable button which highlights itself when mouse flies over it.
	:param text: the actual text to display.
	:param center: the center point of the button.
	:param font=TEXT_FONT: font of the button.
	:param color=white: color of the button.
	"""
	def __init__(self, text, center, font=cst.TEXT_FONT, color=cst.WHITE):
		self.text = text
		self.font = font
		self.rect = font.render(text, True, color).get_rect()
		self.rect.center = center
		self.lit = False
		self.color = color #color du type (r,g,b) avec 0<= r,g,b <= 255

	def update(self, bliton=None):
		"""
		Updates the button's state, especially deals with highlighting.
		"""
		if bliton == None :
			bliton = pygame.display.get_surface()	
		mousePos = pygame.mouse.get_pos()
		if not self.lit:
			if self.rect.collidepoint(mousePos):
				self.lit = True
		else:
			if not self.rect.collidepoint(mousePos):
				self.lit = False
		color = self.getColor()
		text = self.font.render(self.text, True, color)
		bliton.blit(text , self.rect)

	def getColor(self):
		"""
		Returns a color based on whether the button is highlit.
		"""
		r, g, b = self.color
		if self.lit:
			r = max(r-90, 0)
			g = max(g-70, 0)
			b = max(b-70, 0)
		return (r, g, b)

	def changeText(self, newText, color=cst.WHITE):
		self.text = newText
		self.image = self.font.render(newText, True, color)
		self.rect = self.image.get_rect(center=self.rect.center)

class GraphicButton:
	'''Bouton de selection d'une tourelle dans la GUI '''

	def __init__(self,topleft, data_number, font=cst.TEXT_FONT_2):

		self.data = turret_dict[data_number]  #La tourelle associée au bouton
		self.preview = self.data.preview  # Image réelle de la tourelle

		self.text = "  "+self.data.name
		self.price = str(self.data.price) + "$"

		self.font = font
		textRect = font.render(self.text, True, white).get_rect()
		textRect.topleft = (topleft[0]+12, topleft[1])
		
		self.priceRect = font.render(self.price, True, paper).get_rect()
		self.priceRect.topleft = (topleft[0]+100, topleft[1]+12)

		self.lit = False

		self.img, self.rect = load_image(self.data.mini) #Miniature de la tourelle
		self.rect.topleft = topleft
		self.rect.union_ip(textRect)

	def getColor(self,color):
		"""
		Returns a color based on whether the button is highlit.
		"""
		r, g, b = color
		if self.lit:
			r = max(r-90, 0)
			g = max(g-70, 0)
			b = max(b-70, 0)
		return (r, g, b)

	def update(self,bliton = None):
		if bliton == None :
			bliton = pygame.display.get_surface()	
		mousePos = pygame.mouse.get_pos()
		if not self.lit:
			if self.rect.collidepoint(mousePos):
				self.lit = True
		else:
			if not self.rect.collidepoint(mousePos):
				self.lit = False
		text = self.font.render(self.text, True, self.getColor(white))
		price = self.font.render(self.price,True, self.getColor(paper))
		bliton.blit(text , self.rect)
		bliton.blit(price, self.priceRect)
		bliton.blit(self.img,self.rect)

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

	def select(self,obj= None):
		if obj == None :
			self.selected = None
			self.image, self.rect = self.cursor_image, self.cursor_rect
		else :
			self.selected = obj
			self.image, self.rect = load_image(self.selected.preview)

	def update(self, mousePos, bliton = None):
		"""
		Updates the cursor's state, especially brings it to the position of the
		mouse.
		"""
		if bliton == None :
			bliton = pygame.display.get_surface()
		x,y = mousePos
		self.rect.topleft = ((x//10)*10, (y//10)*10)
		if x+self.rect.width < 601 and x>self.rect.width//2:
			self.parent.blit(self.image, self.rect)
