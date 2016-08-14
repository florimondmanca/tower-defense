'''
Entities class.
Generic classes representing every entities (mobs and turrets) of the game.
Classes Turret and Mob inherits from class IsoSprite (juste like the Tile class)
'''

# ------ Importations ------

import pygame
import math
from isometric import IsoSprite, isoutils
import constants as cst

# ------ Turret Class ------

class Turret(IsoSprite):
    '''Classe de base des tourelles posables par le joueur '''

    def __init__(self, path_to_image, pos):

        # game settings
        self.hp = 0
        self.hit_ground = True
        self.hit_fly = True
        self.price = 100
        
    def update(self):
        pass

    def display(self, screen = pygame.display.get_surface()):
        super().display(screen)
        if cst.DEBUG:
            pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 2)
            pygame.draw.rect(screen, pygame.Color("blue"), self.target.rect, 2)
            pygame.draw.rect(screen, pygame.Color("red"), self.iso_rect, 2)
            pygame.draw.rect(screen, pygame.Color("red"), self.target.iso_rect, 2)
