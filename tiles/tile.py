import os
import constants as cst
from isometric import IsoSprite, isoutils
import gui

class Tile(IsoSprite):
    """
    An IsoSprite representing a tile.
    """
    bright_patch, _ = gui.misc.load_image("tiles", "misc", "bright.png")
    def __init__(self, tile_pos=None, category="none", tile_type=cst.NONE_TILE):
        if tile_pos is not None:
            tile_pos = (tile_pos[0] - cst.MAP_WIDTH//2, tile_pos[1] - cst.MAP_WIDTH//2)
        super().__init__(path_to_image=["tiles", category, tile_type+".png"], tile_pos=tile_pos)

    def change(self, category, tile_type):
        """Changes the tile to a new category and tile_type"""
        self.image, self.rect = gui.misc.load_image("tiles", category, tile_type+".png")
        self.rect.center = self.iso_pos

    def _update_positions(self, new_pos=None, new_iso_pos=None):
        """ Keeps pos, iso_pos, rect and iso_rect up-to-date """
        if new_pos is not None:
            new_iso_pos = isoutils.cart_to_iso(new_pos)
        elif new_iso_pos is not None:
            new_pos = isoutils.iso_to_cart(new_iso_pos)
        else:
            raise TypeError("Did not give any position to update !")
        # move the rects with the same amount
        self._rect.center = self._pos = new_pos
        self._iso_rect.center = self._iso_pos = new_iso_pos


class Decoration(IsoSprite):
    """
    An IsoSprite representing a decoration object.
    """
    def __init__(self, tile_pos=None, category="none", deco_type=cst.NONE_TILE):
        if tile_pos is not None:
            tile_pos = (tile_pos[0] - cst.MAP_WIDTH//2, tile_pos[1] - cst.MAP_WIDTH//2)
        super().__init__(path_to_image=["decoration", category, deco_type+".png"], tile_pos=tile_pos)

    def change(self, category, tile_type):
        """Changes the tile to a new category and tile_type"""
        self.image, self.rect = gui.misc.load_image("decoration", category, deco_type+".png")
        self.rect.center = self.iso_pos
