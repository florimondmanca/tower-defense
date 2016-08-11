import os
import constants as cst
from .tileslibrary import tlib
from .tilepatch import TilePatch


class Map:
	"""
	Represents a 2D map made out of tiles.
	Ascending X : South
	Ascending Y : West
	"""
	def __init__(self, width=5, height=5, tiles=None):
		self.width = width
		self.height = height
		if tiles is None:
			self.tiles = [[tlib.terrain_tiles["none"] for y in range(height)] for x in range(width)]
		else:
			self.tiles = tiles

	@staticmethod
	def create_plain(tile_type, width, height):
		""" Creates a 'width'*'height' map with only one tile type. """
		new_map = Map(width=width, height=height)
		for x in range(width):
			for y in range(height):
				new_map.tiles[x][y] = tlib.terrain_tiles[tile_type]
		return new_map

	@staticmethod
	def import_map(map_name):
		""" Imports a map 'map_name' from the static/maps folder. map_name must end with {} """.format(cst.MAP_EXT)
		if not map_name.endswith(cst.MAP_EXT):
			raise TypeError("Cannot import map with name {}. Map names must end with '{}'.".format(map_name, cst.MAP_EXT))
		# used to check later on that all values are present in map file
		found = {"WIDTH": False, "HEIGHT": False, "TILE_TYPES": False, "TILES_ARRAY": False}
		# fetch values from the .map file
		with open(os.path.join(cst.MAPS_DIR, map_name), 'r') as mapfile:
			l = mapfile.readline().strip()
			while l != "END_OF_FILE":
				# if empty line, just skip it
				if l == "":
					l = mapfile.readline().strip()
					continue
				# fetch width
				elif l == "WIDTH":
					width = int(mapfile.readline().strip())
					found["WIDTH"] = True
				# fetch height
				elif l == "HEIGHT":
					height = int(mapfile.readline().strip())
					found["HEIGHT"] = True
				# fetch the tile_types dictionnary
				elif l == "TILE_TYPES":
					tile_types = {}
					l = mapfile.readline().strip()
					while l != "END":
						symbol, category, tile_type = l.split()
						tile_types[symbol] = (category, tile_type)
						l = mapfile.readline().strip()
					found["TILE_TYPES"] = True
				# fetch the symbolic tiles array
				elif l == "TILES_ARRAY":
					tiles_symb = []
					l = mapfile.readline().strip()
					while l != "END":
						tiles_symb.append(list(l))
						l = mapfile.readline().strip()
					# must transpose columns and rows
					tiles_symb = list(map(list, zip(*tiles_symb)))
					# check dimensions are OK with the ones declared
					assert len(tiles_symb) == width, "Widths do not correspond !"
					if height > 0:
						assert len(tiles_symb[0]) == height, "Heights do not correspond !"
					found["TILES_ARRAY"] = True
				l = mapfile.readline().strip()

		# check that all values were successfully fetched
		for to_find, val in found.items():
			not_found = []
			if not val:
				not_found.append(to_find)
			if not_found:
				raise NameError("Could not import map {} as the following is missing :\n{}".format(map_name, not_found))

		# assign TilePatch tiles to a 2D array from symbolic tiles
		tiles = []
		for x in range(width):
			row = []
			for y in range(height):
				row.append(TilePatch(*tile_types[tiles_symb[x][y]]))
			tiles.append(row)

		return Map(width=width, height=height, tiles=tiles)

	def __getitem__(self, pos):
		""" Allows direct access to the tiles, e.g. some_map[x, y] instead of some_map.tiles[x][y]. If y is not passed (some_map[x]), returns the complete row some_map.tiles[x]. """
		if isinstance(pos, tuple):
			x, y = pos
			return self.tiles[x][y]
		else:
			return self.tiles[pos]

	def __setitem__(self, pos, tile_type, tile_category="terrain_tiles"):
		""" Allows direct replacement of a tile using its tile_type, i.e. a string value. Looks for tile_type in the tlib.<tile_category> dictionnary.
		If pos is a (x, y) tuple, changes the tile at (x, y).
		If only x is passed, changes the whole row to the given tile. """
		if isinstance(pos, tuple):
			x, y = pos
			self.tiles[x][y] = getattr(tlib, tile_category)[tile_type]
		else:
			x = pos
			for y in range(self.height):
				self.tiles[x][y] = getattr(tlib, tile_category)[tile_type]

	def __iter__(self):
		""" Iterates over the map tiles, in descending depth (y) order. """
		for y in range(self.height):
			for x in range(self.width):
				yield self.tiles[x][y]