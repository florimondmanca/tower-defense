'''
Entities class.
Generic classes representing every entities (mobs and turrets) of the game.
'''

# ------ Importations ------

import pygame
import math
from isometric import IsoSprite, isoutils
import constants as cst
from . import misc
from gui import menu

# ------ Entity Class ------

class Entity(IsoSprite):
    """

    """

    def __init__(self, path_to_image, tile_pos=None):
        IsoSprite.__init__(self, path_to_image, tile_pos)
        pos = self.iso_rect.topleft

        # name parameters
        self.name = "null"
        self.nameb = menu.Message(self.name, (pos[0], pos[1]-7), font=cst.NAME_FONT, color=cst.BLACK, center = False)

        # health parameters
        self._max_hp = 100
        self._hp = self._max_hp
        self.dead = False

        # health bar parameters
        self.hb = misc.HealthBar(self._max_hp, pos)

    ## ------ Graphical functions ------

    def update(self):

        # health bar and name placement
        # those objects should always lie on top of the entity sprite
        (x,y) = self.iso_rect.midtop
        self.hb.rect.midbottom = (x,y)
        self.nameb.rect.midbottom = (x,y-7)

        # update value to display on the health bar
        self.hb.update(self._hp)

        # check if dead
        if self._hp == 0 :
            self.dead = True

    def display(self, screen):
        '''
        display(self, screen) :
            displays the Sprite onto the screen.
        '''
        super().display(screen)
        if cst.SHOW_HEALTH or cst.DEBUG :
            self.hb.display(screen)
        if cst.SHOW_NAME or cst.DEBUG :
            self.nameb.display(screen)

   ## ------ Health-Bar functions ------
    
    def damage(self,value):
        self._hp = max(0, self._hp - value)
