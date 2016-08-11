# BubbleRush by Guillaume Coiffier
# Main file

import os, sys

if os.getcwd() not in sys.path :
	sys.path.append(os.getcwd())

from mainMenu import run_game

run_game()
