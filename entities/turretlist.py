# encoding=utf-8

# ------ Importations ------
import os
import pygame
import constants as cst
from . import turret

# ------ Tourelles ------

'''
Définir ICI une fonction plussify
CAUTION : define classes strictly as :
{Type of turret}{Small/Large}
'''

class BasicSmall(turret.Turret):
	def __init__(self):
		turret.Turret.__init__(self, os.path.join(cst.IMG_DIR, *["turrets", "test.png"]), tile_pos=(0, 0))


class BasicLarge(turret.Turret):
	def __init__(self):
		turret.Turret.__init__(self, os.path.join(cst.IMG_DIR, *["turrets", "test_large.png"]), tile_pos=(0, 0))


class MissileSmall(turret.Turret):
	def __init__(self):
		turret.Turret.__init__(self, os.path.join(cst.IMG_DIR, *["turrets", "test.png"]), tile_pos=(0, 0))


class MissileLarge(turret.Turret):
	def __init__(self):
		turret.Turret.__init__(self, os.path.join(cst.IMG_DIR, *["turrets", "test_large.png"]), tile_pos=(0, 0))


class LaserSmall(turret.Turret):
	def __init__(self):
		turret.Turret.__init__(self, os.path.join(cst.IMG_DIR, *["turrets", "test.png"]), tile_pos=(0, 0))


class LaserLarge(turret.Turret):
	def __init__(self):
		turret.Turret.__init__(self, os.path.join(cst.IMG_DIR, *["turrets", "test_large.png"]), tile_pos=(0, 0))
