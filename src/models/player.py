from typing import List

from pygame import image

from models.entity import Entity


class Player(Entity):
    """Represents the player."""

    def __init__(self, speed: List[int]):
        """Create a new Player."""
        self._player_image = image.load("assets/ball.gif")
        self._player_rect = self._player_image.get_rect()

        # ensure that the speed is a 2D vector before setting it
        if len(speed) != 2:
            raise RuntimeError(f"Invalid speed. Expected list of length 2, got length {len(speed)}")
        self.speed = speed

    def move(self):
        """Moves the player according to their current speed."""
        self._player_rect = self._player_rect.move(self.speed)

    def get_left(self):
        """Returns the player's left-most position."""
        return self._player_rect.left

    def get_right(self):
        """Returns the player's right-most position."""
        return self._player_rect.right

    def get_bottom(self):
        """Returns the player's bottom-most position."""
        return self._player_rect.bottom

    def get_top(self):
        """Returns the player's top-most position."""
        return self._player_rect.top

    def handle_window_border_x(self):
        """Handles the behavior of the player's image if they reach the x-borders of the window."""
        self.speed[0] = -self.speed[0]

    def handle_window_border_y(self):
        """Handles the behavior of the player's image if they reach the y-borders of the window."""
        self.speed[1] = -self.speed[1]

    def get_surface(self):
        """Returns the internal Surface for the player."""
        # return a copy here because `self._player_image` is a private field
        # private field means that another part of the program should not be able to modify it
        return self._player_image.copy()

    def get_rect(self):
        """Returns the internal Rect for the player."""
        return self._player_rect.copy()
