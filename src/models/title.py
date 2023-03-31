from pygame import image, transform

from models.entity import Entity

TITLE_SIZE = (562, 135)

#TODO: Does this need to be an entity? Maybe there could be a seperate class for purely visual components like this (and the background)
class Title(Entity):
    """Represents the title (Flappy Duck) itself"""
    def __init__(self, window_width: int, window_height: int):
        self._title_image = transform.scale(
            image.load("assets/title.png"), TITLE_SIZE
        )
        self._title_rect = self._title_image.get_rect()
        #Centers title horizontally and 1/4ths down vertically
        self._title_rect = self._title_rect.move(int(window_width/2 - TITLE_SIZE[0]/2), int(window_height/4))

    def move(self, delta_time=1):
        """Moves the title button, not needed since it shouldn't move"""
        pass

    def get_left(self):
        """Returns the title's left-most position."""
        return self._title_rect.left

    def get_right(self):
        """Returns the title's right-most position."""
        return self._title_rect.right

    def get_bottom(self):
        """Returns the title's bottom-most position."""
        return self._title_rect.bottom

    def get_top(self):
        """Returns the title's top-most position."""
        return self._title_rect.top

    def handle_window_border_x(self):
        """Handles the behavior of the title's image if it reaches the x-borders of the window."""
        pass

    def handle_window_border_y(self):
        """Handles the behavior of the title's image if it reaches the y-borders of the window."""
        pass

    # def __init__(self, image: Surface):
    #     self._original_image = image
    #     self._scaled_image = self._original_image.copy()
    #     self._rect = self._scaled_image.get_rect()
    #     self._window_surface = None

    # def set_size(self, width, height):
    #     old_ratio = self._original_image.get_width() / self._original_image.get_height()
    #     new_ratio = width / height
    #     if old_ratio < new_ratio:
    #         new_width = width
    #         new_height = width / old_ratio
    #     else:
    #         new_width = height * old_ratio
    #         new_height = height
    #     self._scaled_image = transform.scale(
    #         self._original_image, (int(new_width), int(new_height)))
    #     self._rect = self._scaled_image.get_rect()

    # def set_window_surface(self, surface):
    #     self._window_surface = surface

    # def draw(self):
    #     self._window_surface.blit(self._scaled_image, self._rect)

    def get_surface(self):
        """Returns the internal Surface for the title."""
        return self._title_image.copy()

    def get_rect(self):
        """Returns the internal Rect for the title."""
        return self._title_rect.copy()
