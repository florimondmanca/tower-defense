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

# Screen and clock
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 1280,720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# Map constants
MAP_WIDTH = 17  # tiles
TILE_PIXEL_SIZE = 32  # pixels
MAP_OFFSET = 50  # pixels, offset due to GUI

# Map-system-related constants
NONE_TILE = "none"  # the name of the blank tile (must be in terrain folder)
NONE_TILE_PATH = os.path.join(IMG_DIR, *["tiles", "none", "none.png"])

# Colors
PAPER = (244, 234, 200)  #(255, 245, 168)
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
GUI_TITLE_FONT = pygame.font.Font(FONT_PATH, 25)
GUI_DESCR_FONT = pygame.font.Font(FONT_PATH, 16)
SCORE_FONT = pygame.font.Font(FONT_PATH,25)

# GUI Constants
CASE_SIZE = 150  # base size for buttons, messages, etc.
ST_Y = 20 # Small Turret y coordinate
LT_Y = 55 # Large Turret 
