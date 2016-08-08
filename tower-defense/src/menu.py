# encoding=utf-8


# ------ Imports ------

import pygame
import os, sys
from time import sleep

if sys.platform == "win32": #si sous windows,
    # on a besoin de ce module pour le standalone
    import pygame._view

pygame.init()
screen = pygame.display.set_mode((800,600))

from .constants import *
from .classes_utilities import Message, Button, Cursor, Score
from .boucle_level import Instance
from .filefinder import get_path

# ------ Functions ------

pygame.mixer.pre_init(frequency=44100)

def options(screen,clock):
    """
    Runs the loop for the OPTIONS screen.
    """

    hw = screenSize[0]//2
    optionsMessage = Message("Options", (hw, caseSize), font=titleFont)
    musicMessage = Message("Music:  ", (hw, int(1.5*caseSize)))
    musicButton = Button("ON", (musicMessage.rect.right, int(1.5*caseSize)))
    menuButton = Button("Back to menu", (hw, int(3.5*caseSize)))
    creditsMessage1 = Message( "Game by Guillaume Coiffier",
        (hw, 4*caseSize-24-2), font=creditFont)
    creditsMessage2 = Message( "Music by Florimond Manca",
        (hw, 4*caseSize-12), font=creditFont)

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menuButton.lit:
                    return
                elif musicButton.lit:
                    if musicButton.text == "ON":
                        musicButton.changeText("OFF")
                        pygame.mixer.pause()
                    elif musicButton.text == "OFF":
                        musicButton.changeText("ON")
                        pygame.mixer.unpause()
        screen.fill(turquoise)
        optionsMessage.display(screen)
        menuButton.update(screen)
        musicMessage.display(screen)
        musicButton.update(screen)
        creditsMessage1.display(screen)
        creditsMessage2.display(screen)
        pygame.display.flip()


def instructions(screen, clock):
    """
    Runs the loop for the INSTRUCTIONS screen.
    """
    hw = screenSize[0]//2
    instructionsMessage = Message("Instructions", (hw, caseSize),
        font=titleFont)
    instructions1 = Message("this is a message",
        (hw, int(1.5*caseSize)), font=creditFont)
    instructions2 = Message("this is an other message",
        (hw, 18+int(1.5*caseSize)), font=creditFont)
    menuButton = Button("Back to menu", (hw, int(3.5*caseSize)))
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menuButton.lit:
                    return
        screen.fill(turquoise)
        instructionsMessage.display(screen)
        instructions1.display(screen)
        instructions2.display(screen)
        menuButton.update(screen)
        pygame.display.flip()


def run_game():
    """
    Runs the main loop.
    """
    pygame.mixer.init()
    musicChannel = pygame.mixer.Channel(0)
    musicSound = pygame.mixer.Sound(get_path("TicTacToe_theme.wav"))
    pygame.display.set_caption("BubbleRush")
    clock = pygame.time.Clock()
    hw = screenSize[0]//2
    title = Message("BubbleRush", (hw, caseSize//2),
                    font=titleFont)
    playButton = Button("Play", (hw, int(1.5*caseSize)))
    instructionsButton = Button("Instructions", (hw, 2*caseSize))
    optionsButton = Button("Options", (hw, int(2.5*caseSize)))
    quitButton = Button("Quit", (hw, int(3.5*caseSize)))

    musicChannel.play(musicSound, loops=-1, fade_ms=2000)

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if playButton.lit:
                    game = Instance()
                    game.run()
                elif instructionsButton.lit:
                    instructions(screen, clock)
                elif optionsButton.lit:
                    options(screen, clock)
                elif quitButton.lit:
                    pygame.mixer.music.fadeout(200)
                    sleep(.2)
                    pygame.quit()
                    return
        screen.fill(turquoise)
        title.display(screen)
        playButton.update(screen)
        instructionsButton.update(screen)
        optionsButton.update(screen)
        quitButton.update(screen)
        pygame.display.flip()


# ------ Execution ------

if __name__ == "__main__":
    run_game()
