# -*- coding: utf-8 -*-

# ------ Importations ------

import os
import pygame

# ------ Fonctions ------

# 1. Obtenir le main_path

def main_path():
    """
    Retourne le chemin du dossier racine du jeu
    """
    return os.path.dirname(os.path.dirname(__file__))


# 2. Le pathfinder
def get_path(fullname):
    """
    Fonction qui retourne le chemin d'un fichier ou dossier
    à partir d'un fullname
    fullname est un string du type "image_num.format"
    """
    # 1. Variables
    main = main_path()
    formats = ["png", "txt", "ttf", "wav", "py"]
    places = ["graphics", "sounds", "src", "levels"]
    name = fullname.partition(".")[0]
    end = fullname.partition(".")[2]
    labels = name.partition("_")
    num = labels[1]
    path = ""

    # 2. Vérification de la conformité de fullname
    if end not in formats and end != "":
        raise UserWarning("Le format de {0} n'est pas supporté".format(fullname))

    # 3. Recherche
    for place in places:
        p = os.path.join(main, place)
        for root, dirs, files in os.walk(p):
            if fullname in dirs:
                path = os.path.join(root, fullname)
                break
            elif fullname in files:
                path = os.path.join(root, fullname)
                break

    # 4. Sortie
    if path == "":
        raise UserWarning("{0} n'a pas été trouvé.".format(fullname))
    else:
        return path


# 3. Chargeur de surface Pygame

def load_image(name):
    """
    Charge l'image du fichier désigné par "name.extension",
    et renvoie sa surface ainsi que le rect associé.
    """
    screen = pygame.display.get_surface()
    path = get_path(name)
    image = pygame.image.load(path)

    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    return (image, image.get_rect())
