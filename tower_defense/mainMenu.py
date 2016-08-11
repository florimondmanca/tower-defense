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
    optionsMessage = Message("Options", (hw, cst.CASE_SIZE), font=cst.TITLE_FONT)
    musicMessage = Message("Music:  ", (hw, int(1.5*cst.CASE_SIZE)))
    musicButton = Button("ON", (musicMessage.rect.right, int(1.5*cst.CASE_SIZE)))
    menuButton = Button("Back to menu", (hw, int(3.5*cst.CASE_SIZE)))
    creditsMessage1 = Message( "Game by Guillaume Coiffier and Florimond Manca",
        (hw, 4*cst.CASE_SIZE-24-2), font=cst.CREDIT_FONT)
    creditsMessage2 = Message( "Music by Florimond Manca",
        (hw, 4*cst.CASE_SIZE-12), font=cst.CREDIT_FONT)

    while True:
        clock.tick(cst.FPS)
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
        screen.fill(cst.TURQUOISE)
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
    hw = cst.SCREEN_WIDTH//2
    instructionsMessage = Message("Instructions", (hw, cst.CASE_SIZE),
        font=cst.TITLE_FONT)
    instructions1 = Message("this is a message",
        (hw, int(1.5*cst.CASE_SIZE)), font=cst.CREDIT_FONT)
    instructions2 = Message("this is an other message",
        (hw, 18+int(1.5*cst.CASE_SIZE)), font=cst.CREDIT_FONT)
    menuButton = Button("Back to menu", (hw, int(3.5*cst.CASE_SIZE)))
    while True:
        clock.tick(cst.FPS)
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
    musicSound = pygame.mixer.Sound(os.path.join(cst.SONG_DIR,"TicTacToe_theme.wav"))
    pygame.display.set_caption("BubbleRush")
    clock = pygame.time.Clock()
    hw = cst.SCREEN_WIDTH//2
    title = Message("BubbleRush", (hw, cst.CASE_SIZE//2),
                    font=cst.TITLE_FONT)
    playButton = Button("Play", (hw, int(1.5*cst.CASE_SIZE)))
    instructionsButton = Button("Instructions", (hw, 2*cst.CASE_SIZE))
    optionsButton = Button("Options", (hw, int(2.5*cst.CASE_SIZE)))
    quitButton = Button("Quit", (hw, int(3.5*cst.CASE_SIZE)))

    musicChannel.play(musicSound, loops=-1, fade_ms=2000)

    while True:
        clock.tick(cst.FPS)
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

        screen.fill(cst.TURQUOISE)
        title.display(screen)
        playButton.update(screen)
        instructionsButton.update(screen)
        optionsButton.update(screen)
        quitButton.update(screen)
        pygame.display.flip()