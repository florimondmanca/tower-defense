import os
import constants as cst
from isometric import IsoSprite, isoutils
import guiutils

class Tile(IsoSprite):
	"""
	An IsoSprite representing a tile.
	"""
	def __init__(self, pos=None, category="none", tile_type=cst.NONE_TILE):
		super(Tile, self).__init__(path_to_image=os.path.join(cst.IMG_DIR, *["tiles", category, tile_type+".png"]), pos=pos)
		self.iso_pos = (self.iso_pos[0] + cst.SCREEN_WIDTH//2, self.iso_pos[1] + cst.SCREEN_HEIGHT//2)

	def change(self, category, tile_type):
		"""Changes the tile to a new category and tile_type"""
		self.image, self.rect = guiutils.load_image(os.path.join(cst.IMG_DIR, *["tiles", category, tile_type+".png"]))
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

	def __str__(self):
		return "Tile :\n    pos: {}\n    iso_pos: {}\n    rect: {}".format(self.pos, self.iso_pos, self.rect)


class Decoration(IsoSprite):
	"""
	An IsoSprite representing a decoration object.
	"""
	def __init__(self, pos=None, category="none", deco_type=cst.NONE_TILE):
		super(Decoration, self).__init__(path_to_image=os.path.join(cst.IMG_DIR, *["decoration", category, deco_type+".png"]), pos=pos)
		self.iso_pos = (self.iso_pos[0] + cst.SCREEN_WIDTH//2, self.iso_pos[1] + cst.SCREEN_HEIGHT//2)

	def change(self, category, tile_type):
		"""Changes the tile to a new category and tile_type"""
		self.image, self.rect = guiutils.load_image(os.path.join(cst.IMG_DIR, *["decoration", category, deco_type+".png"]))
		self.rect.center = self.iso_pos

	def __str__(self):
		return "Deco :\n    pos: {}\n    iso_pos: {}\n    rect: {}".format(self.pos, self.iso_pos, self.rect)