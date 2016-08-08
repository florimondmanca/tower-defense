# encoding=utf-8

# ------ Importation ------

import pygame.font
import os
p = os.getcwd()
from .filefinder import get_path
from .turrets import *

# ------ Nomenclature ------

'''
data codes :
0 = void
1 = obstacle
2 = entry
3 = exit
'''

# tower-defense path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

turret_dict = [BasicSmall(),
				BasicMedium(),
				BasicLarge(),
				MissileSmall(),
				MissileMedium(),
				MissileLarge(),
				LaserSmall(),
				LaserMedium(),
				LaserLarge(),
				BasicMedium(),
				BasicMedium(),
				BasicMedium(),
				BasicMedium(),
				BasicMedium(),
				BasicMedium(),
				BasicMedium()]

# ------ Constants ------

fps = 48


screenSize = (800,600)
caseSize = 100
offset = 50

paper = (255, 245, 168)
turquoise = (37, 154, 141)
white = (255, 255, 255)
grey = (165, 185, 185)
black = (50, 55, 70)
blue = (20, 60, 110)
red = (250,0,0)

pygame.font.init()

drawFont = pygame.font.Font(get_path("speculum.ttf"), 100)

textFont = pygame.font.Font(get_path("speculum.ttf"),  18)
textFont2 = pygame.font.Font(get_path("speculum.ttf"), 15)

creditFont = pygame.font.Font(get_path("speculum.ttf"), 12)

titleFont = pygame.font.Font(get_path("speculum.ttf"), 40)