import os
from collections import namedtuple
import constants as CST
import utils


"""
The Mob library contains all Mob Patches available from static/img/mobs.
Usage:
from .mobLibrary import tlib
"""
TLib = namedtuple("tlib", [cat+"_tiles" for cat in CST.TILE_CATEGORIES])
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

print("-- LOADING FINISHED : Mob library --")
