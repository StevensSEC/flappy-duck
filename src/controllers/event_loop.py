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

    player = Player(1000, window.width/2 * .75)
    window.register_entity(player)

    # Event loop: a loop that checks if new events have occurred and responds to them if they have
    while True:
        # check all the events sent from pygame
        for _event in event.get():
            # if a quit event was sent, end the process
            if _event.type == pygame.QUIT:
                print("Found QUIT event")
                sys.exit()

        # handle the window
        window.clear()
        window.update()
