from pygame import image, transform

from models.entity import Entity

BUTTON_SIZE = (187, 65)

class Button(Entity):
    """Represents the button."""
    def __init__(self, window_width: int, window_height: int, button_img: str):
        self._button_image = transform.scale(
            image.load("assets/" + button_img), BUTTON_SIZE
        )
        self._button_rect = self._button_image.get_rect()
        #Centers button horizontally and 3/4ths down vertically
        self._button_rect = self._button_rect.move(int(window_width/2 - BUTTON_SIZE[0]/2), int(3*window_height/4))

    def check_if_clicked(self, mouse_pos):
        return self._button_rect.collidepoint(mouse_pos)

    def move(self, delta_time=1):
        """Moves the button, not needed since it's a static button"""
        pass

    def get_left(self):
        """Returns the button's left-most position."""
        return self._button_rect.left

    def get_right(self):
        """Returns the button's right-most position."""
        return self._button_rect.right

    def get_bottom(self):
        """Returns the button's bottom-most position."""
        return self._button_rect.bottom

    def get_top(self):
        """Returns the button's top-most position."""
        return self._button_rect.top

    def handle_window_border_x(self):
        """Handles the behavior of the button's image if they reach the x-borders of the window."""
        pass

    def handle_window_border_y(self):
        """Handles the behavior of the button's image if they reach the y-borders of the window."""
        pass

    def get_surface(self):
        """Returns the internal Surface for the button."""
        # return a copy here because `self._player_image` is a private field
        # private field means that another part of the program should not be able to modify it
        return self._button_image.copy()

    def get_rect(self):
        """Returns the internal Rect for the button."""
        return self._button_rect.copy()

