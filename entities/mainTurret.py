# encoding=utf-8

# ------ Importations ------

import pygame
import math
from isometric import IsoSprite
import constants as cst


class MainTurret(IsoSprite):

	def __init__(self):
		IsoSprite.__init__(self)
		self.hp = cst.TOTAL_HP