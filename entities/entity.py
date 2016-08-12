'''
Entities class.
Generic classes representing every entities (mobs and turrets) of the game.
Classes Turret and Mob inherits from class IsoSprite (juste like the Tile class)
'''

# ------ Importations ------

import pygame
import math
from isometric import IsoSprite, isoutils

# ------ Entities ------

class Turret(IsoSprite):
    '''Classe de base des tourelles posables par le joueur '''

    def __init__(self):
        pass
        
    def update(self,bliton= None):
        if bliton == None :
            bliton = pygame.display.get_surface()
        bliton.blit(self.base, self.base_rect)
        #bliton.blit(self.cannon, self.cannon_rect)


class Mob(IsoSprite):
    ''' Classe de base des monstres traversant le niveau '''

    def __init__(self, pos, img, spd = 1):
        self.image, self.rect = load_image(img)
        self.speed = spd
        self.rect.center = pos
        self.movepos = [0,0]    # vitesse de déplacement droite/gauche, haut/bas, valeurs dans {-self.speed,0,self.speed}
        self.angle = math.radians(0)   # angle initial
        self.angle_cons = 0            # angle de consigne initial
        self.pas_rot = math.radians(15)
        
    def update(self):
        ''' update(self): met à jour la position du mob'''
        
        self.pivot()
        self.rotate()
        dx = self.movepos[0]
        dy = self.movepos[1]
        oldpos = self.rect
        self.rect = self.rect.move(dx, dy)
        screen = pygame.display.get_surface()
        screen.blit(self.image , self.rect)

    def display(self, screen = pygame.display.get_surface()):
        screen.blit(self.anim_image, self.iso_rect)
        pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 2)
        pygame.draw.rect(screen, pygame.Color("blue"), self.target.rect, 2)
        pygame.draw.rect(screen, pygame.Color("red"), self.iso_rect, 2)
        pygame.draw.rect(screen, pygame.Color("red"), self.target.iso_rect, 2)


