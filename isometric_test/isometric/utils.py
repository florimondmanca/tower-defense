import pygame
from . import constants as cst

def load_image(path_to_image):
    """
    Loads the image using the full path to the image.
    Manages alpha conversion (e.g. png's).
    """
    image = pygame.image.load(path_to_image)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image, image.get_rect()

def cart_to_iso(*pos):
    if len(pos) == 1:
        pos = pos[0]
    x, y = pos
    return (x-y), (x+y)/2

def iso_to_cart(*pos):
    if len(pos) == 1:
        pos = pos[0]
    x, y = pos
    return (2*y + x)/2, (2*y - x)/2

def tile_to_cart(*pos):
    if len(pos) == 1:
        pos = pos[0]
    i, j = pos
    return cst.TILE_SIZE*i, cst.TILE_SIZE*j

def tile_to_iso(*pos):
    if len(pos) == 1:
        pos = pos[0]
    i, j = pos
    return cart_to_iso(*tile_to_cart(i, j))