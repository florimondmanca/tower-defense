import pygame

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
