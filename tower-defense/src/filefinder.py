# -*- coding: utf-8 -*-

# ------ Importations ------

import os
import pygame

# tower-defense path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ------ Fonctions ------

def main_path():
    """
    Retourne le chemin du dossier racine du jeu
    """
    return os.path.dirname(os.path.dirname(__file__))

def get_path(path):
    """
    Fonction qui retourne le chemin d'un fichier ou dossier
    à partir d'un path
    path est un string du type "static/sounds/some_sound.wav"
    """
    allowed = ("static, levels")  # keep up to date as more file types are added
    # 1. Variables
    splitted = path.split("/")
    if splitted[0] in allowed:
        # for sounds, images, fonts, etc.
        return os.path.join(BASE_DIR, *splitted)
    else:
        raise ValueError("Could not load file with path {}. Must begin with one of these : {}".format(fullname, allowed))

def load_image(name):
    """
    Charge l'image du fichier désigné par "name.extension",
    et renvoie sa surface ainsi que le rect associé.
    Attention : le name donné doit exister dans ~/static/img
    """
    image = pygame.image.load(get_path("static/img/{}".format(name)))
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    return (image, image.get_rect())
