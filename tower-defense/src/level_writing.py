# encoding=utf-8

# ------ Importations ------

from os import getcwd
p = getcwd()

from .filefinder import get_path

# ------ Nomenclature ------

'''
data codes :
0 = void
1 = wall
2 = entry
3 = exit
'''

# ------ Fonctions ------

def func(j):
	if j>27 and j<33 :
		return 2
	return 1

def func2(j):
	if j>27 and j<33 :
		return 3
	return 1

def convert(liste):
	string = ""
	for x in liste :
		string+= str(x)+" "
	return string

def write():
	data = [[0 for i in range(60)] for j in range(60)]
	data[0] = [func(j) for j in range(60)]
	data[-1] = [func2(j) for j in range(60)]
	for i in range(60) :
		data[i][0] = 1
		data[i][-1] = 1
	texte = open("level.txt",mode='w')
	for x in data:
		texte.write(convert(x)+"\n")

write()