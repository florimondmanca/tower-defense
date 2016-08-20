# encoding=utf-8


# ------ Imports ------

import pygame

from copy import copy
import constants as cst
from isometric import isoutils

map_center = isoutils.iso_to_cart((cst.SCREEN_WIDTH//2, cst.SCREEN_HEIGHT//2 + cst.MAP_OFFSET))

def load_image_only(*path_to_image):
    image = pygame.image.load(os.path.join(cst.IMG_DIR, *path_to_image))
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image

def load_image(*path_to_image):
    """
    Loads the image using the full path to the image.
    Manages alpha conversion (e.g. png's).
    """
    image = load_image_only(*path_to_image)
    return image, image.get_rect()

def rotate_left(pos, center=map_center):
    """
    Rotates a given position around a given center by 90° clockwise
    """
    return [(pos[1] - center[1]) + center[0],
            -(pos[0] - center[0]) + center[1]]

def rotate_right(pos, center=map_center):
    """
    Rotates a given position around a given center by 90° anti-clockwise
    """
    return [-(pos[1] - center[1]) + center[0],
            (pos[0] - center[0]) + center[1]]


def draw_frame(screen, rect, color):
    pygame.draw.line(screen, color, rect.topleft, rect.topright)
    pygame.draw.line(screen, color, rect.topright, rect.bottomright)
    pygame.draw.line(screen, color, rect.bottomright, rect.bottomleft)
    pygame.draw.line(screen, color, rect.bottomleft, rect.topleft)


class FpsCounter:
    """ A small object to display fps (in console or could be extended to print on screen) every few frames """
    def __init__(self, nframes=50):
        self.time = 0
        self.count = 0
        self.nframes = nframes

    def update(self, t):
        self.time += t
        self.count += 1
        if self.count == self.nframes:
            print("FPS: {}".format(round(self.nframes/self.time, 3)))
            self.time = self.count = 0
