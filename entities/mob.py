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

# ------ Mob Class ------

class Mob(IsoSprite):
    ''' Classe de base des monstres traversant le niveau '''

    def __init__(self, path_to_image, pos = None):
        IsoSprite.__init__(self, path_to_image, pos)
        self.spritesheet = self.image
        self.anim_key = 0  # 0, 1 or 2 (x on spritesheet)
        self.state = 0  # 0 front, 1 left, 2 right, 3 back (y on spritesheet)
        self.anim_speed = 5  # sprite anims every anim_speed frames
        self.anim_counter = 0  # increments every frame
        self.size = 32  # pixels

        # v force rect to be of size self.size, not spritesheet's size !
        new_iso_rect = pygame.Rect((0, 0), (self.size, self.size))
        new_iso_rect.center = self.iso_pos
        self.set_iso_rect(new_iso_rect)
        new_rect = pygame.Rect((0, 0), isoutils.iso_to_cart(self.size, self.size))
        new_rect.center = self.pos
        self.set_rect(new_rect)

        # ^
        self.image = None
        self.update_image()

        # game settings
        self.speed = 3  # chasing speed
        self.is_flying = False
        self.hp = 0


    def update_image(self):
        mask_rect = pygame.Rect(self.anim_key*self.size, self.state*self.size, self.size, self.size)
        self.image = self.spritesheet.subsurface(mask_rect)
        
    def update(self):
        ''' 
        update(self):
        '''
        # update the animation
        self.anim_counter += 1
        if self.anim_counter == self.anim_speed:
            self.anim_counter = 0
            self.anim_key = (self.anim_key + 1) % 3
            self.update_image()

    def display(self, screen = pygame.display.get_surface()):
        '''
        display(self, screen = pygame.display.get_surface()) :
            displays the Sprite onto the screen.
        '''
        super().display(screen)
        if cst.DEBUG:
            pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 2)
            pygame.draw.rect(screen, pygame.Color("blue"), self.target.rect, 2)
            pygame.draw.rect(screen, pygame.Color("red"), self.iso_rect, 2)
            pygame.draw.rect(screen, pygame.Color("red"), self.target.iso_rect, 2)
