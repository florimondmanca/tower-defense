import os
from collections import namedtuple
from . import constants as cst
from . import utils
from .tilepatch import TilePatch


"""
The tiles library contains all Tile Patches available from static/img/tiles.
Usage:
from .tileslibrary import tlib
"""
TLib = namedtuple("tlib", [cat+"_tiles" for cat in cst.TILE_CATEGORIES])
TLib.__new__.__defaults__ = (dict(),) * len(TLib._fields)
tlib = TLib()
print("\n-- LOADING : Tiles library --")
for cat in cst.TILE_CATEGORIES:
	print("Loading {} tiles...".format(cat))
	# walk through the each category folder to add files
	for root, dirs, files in os.walk(os.path.join(cst.IMG_DIR, *["tiles", cat])):
		for f in files:
			if f.endswith(".png"):
				tile_type = f.replace(".png", "")
				getattr(tlib, cat+"_tiles")[tile_type] = TilePatch(category=cat, tile_type=tile_type)
	print("OK")

print("-- LOADING FINISHED : Tiles library --")