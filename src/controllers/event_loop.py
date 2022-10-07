import sys

import pygame
from pygame import event

from models.player import Player
from models.window import Window


def event_loop() -> None:
    """The main GUI event loop. Handles events then draws the screen. Loops until the user exits."""
    print("Entering main game loop")
    pygame.init()

    window = Window()

    player = Player(0, window.width / 2 * .75)
    window.register_entity(player)
    
    has_clicked = False

    # Event loop: a loop that checks if new events have occurred and responds to them if they have
    while True:
        # check all the events sent from pygame
        for _event in event.get():
            # if a quit event was sent, end the process
            if _event.type == pygame.QUIT:
                print("Found QUIT event")
                sys.exit()
            elif _event.type == pygame.MOUSEBUTTONDOWN:
                if not has_clicked:
                    # TODO: Add a start menu, don't just leave gravity at 0 until the first click.
                    window.clear()
                    window.update()
                    player.gravity = 1500
                    has_clicked = True
                else:
                    player.jump(window._frame_counter)

        # handle the window
        window.clear()
        window.update()
