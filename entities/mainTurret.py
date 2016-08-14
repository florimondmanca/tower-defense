# encoding=utf-8

# ------ Importations ------

import pygame
import math
import os
from isometric import IsoSprite
import constants as cst
from . import turret


class MainTurret(turret.Turret):
	"""
	The Main tower in the middle of the terrain.
	This class also contains every datas related to the player, like money or score.
	"""
	def __init__(self):
		super(MainTurret, self).__init__(path_to_image=os.path.join(cst.IMG_DIR, *["spritesheets", "maintower.png"]), pos=(400,300))
		self.hp = 1000

		self.money = 400
		self.score = 0