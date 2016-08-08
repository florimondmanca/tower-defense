# encoding=utf-8

# ------ Importations ------

import pygame
import math
from os import getcwd
p = getcwd()
from .filefinder import load_image
from .entity import Mob

# ------ Tourelles ------

class Cell(Mob):
	def __init__(self):
		Mob.__init__(self,(0,0),"cell.png",1)
		self.path = []
