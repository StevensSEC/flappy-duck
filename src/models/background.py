from pygame import Surface, transform


class Background():
    def __init__(self, image: Surface):
        self._original_image = image
        self._scaled_image = self._original_image.copy()
        self._rect = self._scaled_image.get_rect()
        self._window_surface = None

    def set_size(self, width, height):
        old_ratio = self._original_image.get_width() / self._original_image.get_height()
        new_ratio = width / height
        if old_ratio < new_ratio:
            new_width = width
            new_height = width / old_ratio
        else:
            new_width = height * old_ratio
            new_height = height
        self._scaled_image = transform.scale(
            self._original_image, (int(new_width), int(new_height)))
        self._rect = self._scaled_image.get_rect()

    def set_window_surface(self, surface):
        self._window_surface = surface

    def draw(self):
        self._window_surface.blit(self._scaled_image, self._rect)

    def get_surface(self):
        return self._scaled_image.copy()

    def get_rect(self):
        return self._rect.copy()
