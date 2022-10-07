from pygame import image

from models.entity import Entity


class Player(Entity):
    """Represents the player."""

    def __init__(self, gravity: int, x_pos: int):
        """Create a new Player."""
        self._player_image = image.load("assets/ball.gif")
        self._player_rect = self._player_image.get_rect()
        self._player_rect = self._player_rect.move(x_pos, 0)

        self.gravity = gravity
        self.y_velo = 0

        # only updated every click to determine number of frames between the last jump and this jump.
        self.local_frame_count = 0
        # counts down from (n) frames to 0
        self.jump_timer = 0

    def jump(self, frameCounter):
        frame_diff = frameCounter - self.local_frame_count
        self.local_frame_count = frameCounter
        # set the jump timer to 0 if negative so number doesn't underflow after a long time
        self.jump_timer = max(self.jump_timer - frame_diff, 0)
        if self.jump_timer > 0:
            # print(self.jump_timer)
            self.jump_timer -= 1
            return
        else:
            # print(self.jump_timer)
            # (n = 20) frames
            self.jump_timer = 20
            self.y_velo = -650
            return

    def move(self, delta_time=1):
        """Moves the player according to their current speed."""
        self.y_velo += self.gravity * delta_time

        self._player_rect = self._player_rect.move(0, self.y_velo * delta_time)

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
        pass

    def handle_window_border_y(self):
        """Handles the behavior of the player's image if they reach the y-borders of the window."""
        pass

    def get_surface(self):
        """Returns the internal Surface for the player."""
        # return a copy here because `self._player_image` is a private field
        # private field means that another part of the program should not be able to modify it
        return self._player_image.copy()

    def get_rect(self):
        """Returns the internal Rect for the player."""
        return self._player_rect.copy()
