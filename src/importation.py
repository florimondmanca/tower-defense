# encoding=utf-8

# ------ Importations ------

from os import getcwd
p = getcwd()

from filefinder import get_path
from classes_utilities import GraphicButton

# ------ Fonctions ------
	
def convert(string):
	return [int(x) for x in string.strip().split(" ")]

def import_level(n):
	texte = open(get_path("level{0}.txt".format(n)), mode='r')
	data = []
	for i in range(60):
		string = texte.readline()
		data.append(convert(string))
	return data

def import_mob(level,wave):
	texte = open(get_path("level{0}.txt".format(level)), mode='r')
	for i in range(60+wave-1):
		texte.readline()
	data = texte.readline().strip().split(" ")
	return None

def import_turrets():
	l = []
	for i in range(12):
		l.append(GraphicButton((620,90+40*i),i))
	return l