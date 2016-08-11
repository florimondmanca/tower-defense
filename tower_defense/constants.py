#BubbleRush constants file

# ------ Importation ------

import pygame
import os

# ------ Constants ------

# Filesystem-related constants
BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
IMG_DIR = os.path.join(BASE_DIR, *["static", "img"])
SONG_DIR = os.path.join(BASE_DIR, *["static", "sounds"])
MAPS_DIR = os.path.join(BASE_DIR, *["static", "maps"])
FONT_DIR = os.path.join(BASE_DIR, *["static","fonts"])
MAP_EXT = ".map"
TILE_CATEGORIES = list(filter(lambda f: not f.startswith("."), os.listdir(os.path.join(IMG_DIR, "tiles"))))


# General game constants
FPS = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
TILE_SIZE = 50  # pixels
MAP_WIDTH, MAP_HEIGHT = 20, 20
MAP_SIZE = (MAP_WIDTH, MAP_HEIGHT)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set a screen now (needed for the TilesLibrary)

CASE_SIZE = 120


# Colors
PAPER = (255, 245, 168)
TURQUOISE = (37, 154, 141)
WHITE = (255, 255, 255)
GREY = (165, 185, 185)
BLACK = (50, 55, 70)
BLUE = (20, 60, 110)
RED = (250,0,0)

# Fonts
pygame.font.init()

font_path = os.path.join(FONT_DIR,"speculum.ttf")

drawFont = pygame.font.Font(font_path, 100)

textFont = pygame.font.Font(font_path,  18)
textFont2 = pygame.font.Font(font_path, 15)

creditFont = pygame.font.Font(font_path, 12)

titleFont = pygame.font.Font(font_path, 40)
