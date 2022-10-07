from pygame import Surface, transform


class Background():
    def __init__(self, image: Surface):
        self._original_image = image
        self._scaled_image = self._original_image.copy()
        self._rect = self._scaled_image.get_rect()

    def set_size(self, width, height):
        # Very naiive and will probably look bad
        # TODO Update to scale without stretching the image
        self._scaled_image = transform.scale(
            self._original_image, (width, height))

    def get_surface(self):
        return self._scaled_image.copy()

    def get_rect(self):
        return self._rect.copy()
