import pygame
import constants as cst

def heuristic(a, b):
    '''
    The heuristic function of the A*
    '''
    x = b[0]-a[0]
    y = b[1]-a[1]
    return (x*x + y*y)

def get_neighbors(case,obstacles) :
    '''
    Returns the list of each cell which is adjacent to the (i, j) cell
    '''
    i, j = case
    neighbors = []
    if j > 0 and obstacles[i, j-1]:
        neighbors.append((i, j-1))
    if j < 20 and obstacles[i, j+1]:
        neighbors.append((i, j+1))
    if i > 0 and obstacles[i-1, j]:
        neighbors.append((i-1, j))
    if i < 31 and obstacles[i+1, j]:
        neighbors.append((i+1, j))
    return neighbors


class HealthBar:
    """
    HealthBar(max_val, pos) -> HealthBar
    max_val = the value (integer) for which the bar is full
    pos = the bottomleft corner (as an health bar always stands on top of an entity with length 32 pxl)
    """
    def __init__(self, max_val, pos):
        self.max_val = max_val
        self.cur_val = max_val

        self.rect = pygame.Rect(0,0,32,5)

    def get_color(self):
        ratio = self.cur_val/self.max_val
        if ratio > 0.5 :
            return cst.HP_GREEN
        elif ratio > 0.25 :
            return cst.HP_ORANGE
        else :
            return cst.HP_RED

    def display(self, screen = pygame.display.get_surface()):
        ratio = self.cur_val/self.max_val
        pygame.draw.rect(screen, self.get_color(), self.rect)

    def update(self, new_val) :
        if new_val != self.cur_val :
            self.cur_val = new_val
            self.rect.width = (32*self.cur_val)//self.max_val