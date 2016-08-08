# encoding=utf-8

# ------ Importations ------

import pygame
import math
from os import getcwd
p = getcwd()
from filefinder import load_image

class Turret:
    '''Classe de base des tourelles posables par le joueur '''

    def __init__(self,img,can, size, price = 50):
        self.base,self.base_rect = load_image(img)
        self.cannon,self.cannon_rect = load_image(can)
        self.size = size
        self.price = price
        self.pos = (-1,-1)

    def init_pos(self,pos):
        self.base_rect.move_ip(pos)
        self.cannon_rect.move_ip(pos)
        self.pos = pos
        
    def update(self,bliton= None):
        if bliton == None :
            bliton = pygame.display.get_surface()
        bliton.blit(self.base, self.base_rect)
        #bliton.blit(self.cannon, self.cannon_rect)


class Mob:
    ''' Classe de base des monstres traversant le niveau '''

    def __init__(self, pos, img, spd = 1):
        ''' __init__(self, pos, img, spd): Initialise un mob'''
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img)
        self.speed = spd
        self.rect.center = pos
        self.movepos = [0,0]    # vitesse de déplacement droite/gauche, haut/bas, valeurs dans {-self.speed,0,self.speed}
        self.angle = math.radians(0)   # angle initial
        self.angle_cons = 0            # angle de consigne initial
        self.pas_rot = math.radians(15)
        
    def pivot(self):
        ''' pivot(self): Gère la rotation. Incrémente ou décrémente son angle suivant la valeur de l'angle de consigne angle_cons, obtenu à partir des touches directionnelles du clavier. '''
        
        alpha , beta = round( math.degrees( self.angle ) ) , self.angle_cons
        delta = beta - alpha
        if delta > 180:       # gère les cas particuliers
            delta = delta - 360
        if delta < -180:
            delta = delta + 360
        if delta > 5:       # on se laisse une marge pour éviter les erreurs numériques
            self.angle += self.pas_rot
        elif delta < -5:
            self.angle -= self.pas_rot

    def rotate(self):
        ''' rotate(self): pivote le sprite du corps d'un angle self.angle '''
        
        centre_rect = self.rect.center
        angle = math.degrees( self.angle )
        self.image = pygame.transform.rotate( self.image , angle )
        self.rect = self.image.get_rect( center=centre_rect )
        
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

    # fonctions de déplacement
    def moveright(self):
        self.movepos[0] = self.speed
    def moveleft(self):
        self.movepos[0] = -self.speed
    def moveup(self):
        self.movepos[1] = -self.speed
    def movedown(self):
        self.movepos[1] = self.speed
    def stophorizontal(self):
        self.movepos[0] = 0
    def stopvertical(self):
        self.movepos[1] = 0
    def stop(self):
        self.movepos = [0,0]

