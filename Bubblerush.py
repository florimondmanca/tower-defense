# BubbleRush by Guillaume Coiffier
# Main file

import os, sys

if os.getcwd() not in sys.path :
	sys.path.append(os.getcwd())

from mainmenu import run_game

run_game()
