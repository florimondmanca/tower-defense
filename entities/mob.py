'''
Mob class.
Classes Turret and Mob inherits from class Entity
'''

# ------ Importations ------

import pygame
import math
from isometric import IsoSprite, isoutils
import constants as cst
from . import misc,entity

# ------ Mob Class ------

class Mob(entity.Entity):
    ''' Classe de base des monstres traversant le niveau '''

    def __init__(self, path_to_image, tile_pos=None):
        entity.Entity.__init__(self, path_to_image, tile_pos)
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

    ## ------ Graphical functions ------

    def update_image(self):
        mask_rect = pygame.Rect(self.anim_key*self.size, self.state*self.size, self.size, self.size)
        self.image = self.spritesheet.subsurface(mask_rect)
        
    def update(self):
        super().update()
        # update the animation
        self.anim_counter += 1
        if self.anim_counter == self.anim_speed:
            self.anim_counter = 0
            self.anim_key = (self.anim_key + 1) % 3
            self.update_image()

    def display(self, screen):
        '''
        display(self, screen) :
            displays the Sprite onto the screen.
        '''
        super().display(screen)
        if cst.DEBUG:
            pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 2)
            pygame.draw.rect(screen, pygame.Color("red"), self.iso_rect, 2)

    ## ------ Behavior and AI functions ------

    def find_path(self, obstacles, target):
        '''
        find_path(self,obstacles) -> path list
            implementation of the A* algorithm. The heuristic used is the euclidean distance.
            return a list of tiles to walk on in order to get to the target avoiding obstacles. The path is the shortest possible path
            if no path is available, returns None.

            obstacles = dict where dict[(i,j)] is True if and only if there is an obstacle on case (i,j)
            target = the coordinate tupple of the case to reach
        '''

        # Data structures
        get_default_dict = lambda default_value: dict(((i, j), default_value) for i in range(cst.MAP_WIDTH) for j in range(cst.MAP_WIDTH))
        passage = get_default_dict(None)
        distance = get_default_dict(float('inf'))
        seen = get_default_dict(False)
        pq = PriorityQueue()

        # Initialisation
        seen[self.case] = True
        distance[self.case] = 0
        pq.put((0,self.case))

        # Processing
        try :
            while not seen[target] :
                prio, case = pq.get()
                if not seen[case] :
                    for vois in get_neightbors(case,obstacles):
                        new_distance = distance[case] + heuristic(target, vois)
                        if not seen[vois] and new_distance < distance[vois]:
                            pq.put((new_distance, vois))
                            distance[vois] = new_distance
                            passage[vois] = case
                seen[case] = True
        except Empty:
            return None
        else:
            # Post-Processing. Extracting path from datas
            shortest_path = []
            pos = target
            while pos != self.case :
                shortest_path.append(pos)
                pos = passage[pos]
            shortest_path.reverse()  # shortest_path was (goal -> init) and we want (init -> goal)
            return shortest_path
