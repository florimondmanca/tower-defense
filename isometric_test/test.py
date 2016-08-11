import sys
from isometric.main import main

if len(sys.argv) > 1:
	map_name = sys.argv[1]
else:
	map_name = "docmap.map"

main(map_name)