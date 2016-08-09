class Point:
	def __init__(self, tile_type=None, pos=None, iso_pos=None):
		if pos is None:
			if iso_pos is None:
				self.pos = (0, 0)
			else:
				self.iso_pos = iso_pos
		else:
			self.pos = pos
		self.calculate_positions()
		if tile_type is None:
			self.tile_type = 0
		else:
			self.tile_type = tile_type

	def calculate_positions(self):
		pass

	def cart_to_iso(self):
		pass

	def iso_to_cart(self):
		pass