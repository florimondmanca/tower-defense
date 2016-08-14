# encoding=utf-8

# ------ Importations ------

import pygame
import math
from . import turret

# ------ Tourelles ------

'''
Définir ICI une fonction plussify
'''

class BasicSmall(turret.Turret):

	def __init__(self):
		turret.Turret.__init__(self,"turret.Turret_base1.png","cannon.png", 1, 50)
		self.preview = "turret.Turret_base1.png"
		self.mini = "mini.png"
		self.name = "Basic S"

class BasicLarge(turret.Turret):
	
	def __init__(self):
		turret.Turret.__init__(self,"turret.Turret_base3.png","cannon.png", 3, 150)
		self.preview = "turret.Turret_base3.png"
		self.mini = "mini.png"
		self.name = "Basic L"



class MissileSmall(turret.Turret):

	def __init__(self):
		turret.Turret.__init__(self,"turret.Turret_base1.png","cannon.png", 1, 80)
		self.preview = "turret.Turret_base1.png"
		self.mini = "mini.png"
		self.name = "Missile S"


class MissileLarge(turret.Turret):

	def __init__(self):
		turret.Turret.__init__(self,"turret.Turret_base3.png","cannon.png", 3, 200)
		self.preview = "turret.Turret_base3.png"
		self.mini = "mini.png"
		self.name = "Missile L"



class LaserSmall(turret.Turret):

	def __init__(self):
		turret.Turret.__init__(self,"turret.Turret_base1.png","cannon.png", 1, 250)
		self.preview = "turret.Turret_base1.png"
		self.mini = "mini.png"
		self.name = "Laser S"


class LaserLarge(turret.Turret):

	def __init__(self):
		turret.Turret.__init__(self,"turret.Turret_base3.png","cannon.png", 3, 500)
		self.preview = "turret.Turret_base3.png"
		self.mini = "mini.png"
		self.name = "Laser L"
