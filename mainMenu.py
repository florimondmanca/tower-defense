# ------ Imports ------

import pygame
import os, sys
from time import sleep

if sys.platform == "win32": #si sous windows,
    # on a besoin de ce module pour le standalone
    import pygame._view

pygame.init()
screen = pygame.display.set_mode((800,600))

import constants as cst
from guiutils import Message, Button, Cursor, Score
from instance import Instance

# ------ Functions ------

pygame.mixer.pre_init(frequency=44100)

def options(screen,clock):
    """
    Runs the loop for the OPTIONS screen.
    """

    hw = cst.SCREEN_WIDTH//2
    options_message = Message("Options", (hw, cst.CASE_SIZE), font=cst.TITLE_FONT)
    music_message = Message("Music:  ", (hw, int(1.5*cst.CASE_SIZE)))
    music_button = Button("ON", (music_message.rect.right, int(1.5*cst.CASE_SIZE)))
    menu_button = Button("Back to menu", (hw, int(3.5*cst.CASE_SIZE)))
    credits_message1 = Message( "Game by Guillaume Coiffier and Florimond Manca",
        (hw, 4*cst.CASE_SIZE-24-2), font=cst.CREDIT_FONT)
    credits_message2 = Message( "Music by Florimond Manca",
        (hw, 4*cst.CASE_SIZE-12), font=cst.CREDIT_FONT)

    while True:
        clock.tick(cst.FPS)
        for event in pygame.event.get():
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
        screen.fill(cst.TURQUOISE)
        options_message.display(screen)
        menu_button.update(screen)
        music_message.display(screen)
        music_button.update(screen)
        credits_message1.display(screen)
        credits_message2.display(screen)
        pygame.display.flip()


def instructions(screen, clock):
    """
    Runs the loop for the INSTRUCTIONS screen.
    """
    hw = cst.SCREEN_WIDTH//2
    instructions_message = Message("Instructions", (hw, cst.CASE_SIZE),
        font=cst.TITLE_FONT)
    instructions1 = Message("this is a message",
        (hw, int(1.5*cst.CASE_SIZE)), font=cst.CREDIT_FONT)
    instructions2 = Message("this is an other message",
        (hw, 18+int(1.5*cst.CASE_SIZE)), font=cst.CREDIT_FONT)
    menu_button = Button("Back to menu", (hw, int(3.5*cst.CASE_SIZE)))
    while True:
        clock.tick(cst.FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu_button.hover:
                    return
        screen.fill(cst.TURQUOISE)
        instructions_message.display(screen)
        instructions1.display(screen)
        instructions2.display(screen)
        menu_button.update(screen)
        pygame.display.flip()


def run_game():
    """
    Runs the main loop.
    """
    pygame.mixer.init()
    music_channel = pygame.mixer.Channel(0)
    music_sound = pygame.mixer.Sound(os.path.join(cst.SONG_DIR,"TicTacToe_theme.wav"))
    pygame.display.set_caption("BubbleRush")
    clock = pygame.time.Clock()
    hw = cst.SCREEN_WIDTH//2
    title = Message("BubbleRush", (hw, cst.CASE_SIZE//2),
                    font=cst.TITLE_FONT)
    play_button = Button("Play", (hw, int(1.5*cst.CASE_SIZE)))
    tuto_button = Button("Tutorial", (hw, int(2*cst.CASE_SIZE)))
    instructions_button = Button("Instructions", (hw, 2.5*cst.CASE_SIZE))
    options_button = Button("Options", (hw, int(3*cst.CASE_SIZE)))
    quit_button = Button("Quit", (hw, int(3.5*cst.CASE_SIZE)))

    music_channel.play(music_sound, loops=-1, fade_ms=2000)

    while True:
        clock.tick(cst.FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.hover:
                    game = Instance()
                    if game.run() == "PYGAME_QUIT":
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

        screen.fill(cst.TURQUOISE)
        title.display(screen)
        play_button.update(screen)
        instructions_button.update(screen)
        options_button.update(screen)
        quit_button.update(screen)
        pygame.display.flip()