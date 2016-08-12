import pygame
import constants as cst

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

def cart_to_tile(*pos):
    if len(pos) == 1:
        pos = pos[0]
    x, y = pos
    return x//cst.TILE_SIZE, y//cst.TILE_SIZE

def iso_to_tile(*pos):
    return cart_to_tile(iso_to_cart(pos))

def tile_to_iso(*pos):
    if len(pos) == 1:
        pos = pos[0]
    i, j = pos
    return cart_to_iso(*tile_to_cart(i, j))