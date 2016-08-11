import os
from collections import namedtuple
import constants as cst
import guiutils


"""
The tiles library contains all pairs of (image, rects) available from static/img/tiles.
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
				image, rect = guiutils.load_image(os.path.join(cst.IMG_DIR, *["tiles", cat, f]))
				getattr(tlib, cat+"_tiles")[tile_type] = [image, rect]
	print("OK")

print("-- LOADING FINISHED : Tiles library --")