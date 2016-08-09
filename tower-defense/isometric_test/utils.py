import pygame

def load_image(path_to_image):
    """
    Loads the image using the full path to the image.
    Manages alpha conversion (e.g. png's).
    """
    image = pygame.image.load(path_to_image)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image, image.get_rect()
