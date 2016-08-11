# encoding=utf-8

# ------ Importations ------

import pygame
import math
from entity import Turret

# ------ Tourelles ------

'''
Définir ICI une fonction plussify
'''

class BasicSmall(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base1.png","cannon.png", 1, 50)
		self.preview = "turret_base1.png"
		self.mini = "mini.png"
		self.name = "Basic S"



class BasicMedium(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base2.png","cannon.png", 2, 100)
		self.preview = "turret_base2.png"
		self.mini = "mini.png"
		self.name = "Basic M"		



class BasicLarge(Turret):
	
	def __init__(self):
		Turret.__init__(self,"turret_base3.png","cannon.png", 3, 150)
		self.preview = "turret_base3.png"
		self.mini = "mini.png"
		self.name = "Basic L"



class MissileSmall(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base1.png","cannon.png", 1, 80)
		self.preview = "turret_base1.png"
		self.mini = "mini.png"
		self.name = "Missile S"



class MissileMedium(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base2.png","cannon.png", 2, 150)
		self.preview = "turret_base2.png"
		self.mini = "mini.png"
		self.name = "Missile M"



class MissileLarge(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base3.png","cannon.png", 3, 200)
		self.preview = "turret_base3.png"
		self.mini = "mini.png"
		self.name = "Missile L"



class LaserSmall(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base1.png","cannon.png", 1, 250)
		self.preview = "turret_base1.png"
		self.mini = "mini.png"
		self.name = "Laser S"



class LaserMedium(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base2.png","cannon.png", 2, 350)
		self.preview = "turret_base2.png"
		self.mini = "mini.png"
		self.name = "Laser M"



class LaserLarge(Turret):

	def __init__(self):
		Turret.__init__(self,"turret_base3.png","cannon.png", 3, 500)
		self.preview = "turret_base3.png"
		self.mini = "mini.png"
		self.name = "Laser L"
