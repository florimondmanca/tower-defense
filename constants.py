#BubbleRush constants file

# ------ Importation ------

import pygame
import os

# ------ Constants ------

# DEBUG VARIABLE
DEBUG = True

# Filesystem-related constants
BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
IMG_DIR = os.path.join(BASE_DIR, *["static", "img"])
SONG_DIR = os.path.join(BASE_DIR, *["static", "sounds"])
MAPS_DIR = os.path.join(BASE_DIR, *["static", "maps"])
FONT_DIR = os.path.join(BASE_DIR, *["static","fonts"])
MAP_EXT = ".map"

# General game constants
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 1280,720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

MAP_WIDTH = 17
TILE_PIXEL_SIZE = 32  # pixels


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set a screen now (needed for the TilesLibrary)

CASE_SIZE = 150  # base size for buttons, messages, etc.

# Map-system-related constants
NONE_TILE = "none"  # the name of the blank tile (must be in terrain folder)
NONE_TILE_PATH = os.path.join(IMG_DIR, *["tiles", "none", "none.png"])

# Colors
PAPER = (255, 245, 168)
TURQUOISE = pygame.Color("dark turquoise")
WHITE = pygame.Color("white")
YELLOW = pygame.Color("yellow")
GREY = (165, 185, 185)
BLACK = pygame.Color("black")
BLUE = (20, 60, 110)
RED = (250,0,0)
GRASS = (139,181,74)

# Fonts
pygame.font.init()

FONT_PATH = os.path.join(FONT_DIR,"speculum.ttf")

DRAW_FONT = pygame.font.Font(FONT_PATH, 100)

TEXT_FONT = pygame.font.Font(FONT_PATH,  28)

CREDIT_FONT = pygame.font.Font(FONT_PATH, 22)

TITLE_FONT = pygame.font.Font(FONT_PATH, 50)

GUI_TURRET_FONT = pygame.font.Font(FONT_PATH, 18)

# GUI Constants

ST_Y = 20 # Small Turret y coordinate
LT_Y = 55 # Large Turret 
