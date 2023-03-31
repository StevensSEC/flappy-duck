import sys

import pygame

from pygame import event, mouse

from models.player import Player
from models.window import Window
from models.title import Title
from models.button import Button

from enum import Enum

class GameState(Enum):
    START = 0
    RUNNING = 1
    GAMEOVER = 2

def event_loop() -> None:
    """The main GUI event loop. Handles events then draws the screen. Loops until the user exits."""
    print("Entering main game loop")
    pygame.init()

    window = Window()

    #Entities
    player = Player(0, window.width / 2 * .75)
    title = Title(window.width, window.height)
    start = Button(window.width, window.height, "start.png")
    restart = Button(window.width, window.height, "restart.png")\

    #First registrations (things that appear on the title screen)
    window.register_entity(title)
    window.register_entity(start)

    #Game State Variable
    game_state = GameState.START

    #Game Control Variables
    has_clicked = False

    #Events that correspond to different game states. After each series of events, return the state the game should be in afterwards
    def start_events(event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            nonlocal has_clicked #TODO: Keep this as nonlocal, or pass the variable?
            if not has_clicked:
                window.clear()
                window.update()
                if start.check_if_clicked(mouse.get_pos()):
                    #If the start button is clicked, start managing the player, stop managing the title screen objects, and "kick off" the game by setting their gravity
                    #TODO: Make the game state a class, so that registering/unregistering can be abstracted?
                    window.unregister_entity(title)
                    window.unregister_entity(start)
                    window.register_entity(player)
                    player.gravity = 1500
                    return GameState.RUNNING
        return GameState.START

    def running_events(event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            nonlocal has_clicked #TODO: Keep this as nonlocal, or pass the variable?
            if not has_clicked:
                window.clear()
                window.update()
                player.gravity = 1500
                has_clicked = True
            else:
                player.jump(window._frame_counter)
        return GameState.RUNNING

    def game_over_events(event) -> None:
        pass


    # Event loop: a loop that checks if new events have occurred and responds to them if they have
    while True:
        # check all the events sent from pygame
        for _event in event.get():
            # if a quit event was sent, end the process
            if _event.type == pygame.QUIT:
                print("Found QUIT event")
                sys.exit()
            else:
                match game_state:
                    case GameState.START:
                        game_state = start_events(_event)
                    case GameState.RUNNING:
                        game_state = running_events(_event)
                    case GameState.GAMEOVER:
                        game_state = game_over_events(_event)
                    case _:
                        #If the game somehow enters a state not covered above, just quit
                        print("Invalid game state entered. Game will now QUIT.")
                        sys.exit()

        # handle the window
        window.clear()
        window.update()