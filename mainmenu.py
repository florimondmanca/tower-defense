# ------ Imports ------

import pygame
import os, sys
from time import sleep
import constants as cst
from gui import menu
from instance import Instance

if sys.platform == "win32": #si sous windows,
    # on a besoin de ce module pour le standalone
    import pygame._view

pygame.init()
screen = cst.SCREEN

# ------ Functions ------

pygame.mixer.pre_init(frequency=44100)

def options(screen,clock):
    """
    Runs the loop for the OPTIONS screen.
    """

    hw = cst.SCREEN_WIDTH//2
    options_message = menu.Message("Options", (hw, cst.CASE_SIZE), font=cst.TITLE_FONT)
    music_message = menu.Message("Music:  ", (hw, int(1.5*cst.CASE_SIZE)))
    music_button = menu.Button("ON", (music_message.rect.right, int(1.5*cst.CASE_SIZE)))
    menu_button = menu.Button("Back to menu", (hw, int(3.5*cst.CASE_SIZE)))
    credits_message1 = menu.Message( "Game by Guillaume Coiffier and Florimond Manca",
        (hw, 4*cst.CASE_SIZE), font=cst.CREDIT_FONT)
    credits_message2 = menu.Message( "Music by Florimond Manca",
        (hw, 4.5*cst.CASE_SIZE), font=cst.CREDIT_FONT)

    while True:
        clock.tick(cst.FPS)
        mouse_event = None
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_event = event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu_button.hover:
                    return
                elif music_button.hover:
                    if music_button.text == "ON":
                        music_button.change_text("OFF")
                        pygame.mixer.pause()
                    elif music_button.text == "OFF":
                        music_button.change_text("ON")
                        pygame.mixer.unpause()
        screen.fill(cst.GRASS)
        options_message.display(screen)
        menu_button.update(mouse_event)
        menu_button.display(screen)

        music_message.display(screen)
        music_button.update(mouse_event)
        music_button.display(screen)

        credits_message1.display(screen)
        credits_message2.display(screen)
        pygame.display.flip()


def instructions(screen, clock):
    """
    Runs the loop for the INSTRUCTIONS screen.
    """
    hw = cst.SCREEN_WIDTH//2
    instructions_message = menu.Message("Instructions", (hw, cst.CASE_SIZE),
        font=cst.TITLE_FONT)
    instructions1 = menu.Message("this is a message",
        (hw, int(1.5*cst.CASE_SIZE)), font=cst.CREDIT_FONT)
    instructions2 = menu.Message("this is an other message",
        (hw, 18+int(1.5*cst.CASE_SIZE)), font=cst.CREDIT_FONT)
    menu_button = menu.Button("Back to menu", (hw, int(3.5*cst.CASE_SIZE)))
    while True:
        clock.tick(cst.FPS)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu_button.hover:
                    return
        screen.fill(cst.GRASS)

        instructions_message.display(screen)
        instructions1.display(screen)
        instructions2.display(screen)

        menu_button.update(mouse_pos)
        menu_button.display(screen)

        pygame.display.flip()


def run_game():
    """
    Runs the main loop.
    """
    pygame.mixer.init()
    music_channel = pygame.mixer.Channel(0)
    music_sound = pygame.mixer.Sound(os.path.join(cst.SONG_DIR,"TowerDefense-elec1.wav"))
    pygame.display.set_caption("BubbleRush")
    clock = pygame.time.Clock()
    hw = cst.SCREEN_WIDTH//2
    title = menu.Message("BubbleRush", (hw, cst.CASE_SIZE//2),
                    font=cst.TITLE_FONT)
    buttons = pygame.sprite.Group()
    play_button = menu.Button("Play", (hw, int(1.5*cst.CASE_SIZE)))
    tuto_button = menu.Button("Tutorial", (hw, int(2*cst.CASE_SIZE)))
    instructions_button = menu.Button("Instructions", (hw, 2.5*cst.CASE_SIZE))
    options_button = menu.Button("Options", (hw, int(3*cst.CASE_SIZE)))
    quit_button = menu.Button("Quit", (hw, int(3.5*cst.CASE_SIZE)))
    
    buttons.add([play_button, tuto_button, instructions_button, options_button, quit_button])

    music_channel.play(music_sound, loops=-1, fade_ms=2000)

    while True:
        clock.tick(cst.FPS)
        mouse_event = None
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_event = event
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.hover:
                    print("-- Instance started --")
                    output = Instance().run()
                    print("-- Instance finished --")
                    if output == "PYGAME_QUIT":
                        pygame.quit()
                        return
                elif tuto_button.hover:
                    pass
                elif instructions_button.hover:
                    instructions(screen, clock)
                elif options_button.hover:
                    options(screen, clock)
                elif quit_button.hover:
                    pygame.mixer.music.fadeout(200)
                    sleep(.2)
                    pygame.quit()
                    return

        screen.fill(cst.GRASS)
        title.display(screen)
        buttons.update(mouse_event)
        for but in buttons :
            but.display(screen)
        pygame.display.flip()