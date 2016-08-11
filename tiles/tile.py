import os
import constants as cst
from isometric import IsoSprite
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

	def __str__(self):
		return "Tile :\n    pos: {}\n    iso_pos: {}\n    rect: {}".format(self.pos, self.iso_pos, self.rect)