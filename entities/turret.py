'''
Turret class.
Classes Turret and Mob inherits from class Entity
'''

# ------ Importations ------

import pygame
import math
from isometric import IsoSprite, isoutils
import constants as cst
from . import entity

# ------ Turret Class ------

class Turret(entity.Entity):
    '''Classe de base des tourelles posables par le joueur '''

    def __init__(self, path_to_image, tile_pos):
        entity.Entity.__init__(self, path_to_image, tile_pos)
        # game settings
        self.hp = 0
        self.hit_ground = True
        self.hit_fly = True
        self.price = 100
        
    def update(self):
        super().update()

    def display(self, screen):
        super().display(screen)
        if cst.DEBUG:
            pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 2)
            pygame.draw.rect(screen, pygame.Color("red"), self.iso_rect, 2)
