import os
import pygame

# Filesystem-related constants
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, *["static", "img"])
MAPS_DIR = os.path.join(BASE_DIR, *["static", "maps"])
MAP_EXT = ".map"
TILE_CATEGORIES = list(filter(lambda f: not f.startswith("."), os.listdir(os.path.join(IMG_DIR, "tiles"))))

# General game constants
FPS = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
TILE_SIZE = 50  # pixels
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set a screen now (needed for the TilesLibrary)

# Map system-related constants
cst.NONE_TILE = "none"  # the name of the blank tile (must be in terrain folder)