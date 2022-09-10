import abc

from pygame import Rect, Surface


class Entity(metaclass=abc.ABCMeta):
    """Interface for any entity that can be managed by the window (i.e. a projectile, the player, etc."""

    @abc.abstractmethod
    def move(self, delta_time=1) -> None:
        """Move the entity across the window."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_left(self) -> int:
        """Return's the entity's left-most position."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_right(self) -> int:
        """Return's the entity's right-most position."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_top(self) -> int:
        """Return's the entity's top-most position."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_bottom(self) -> int:
        """Return's the entity's bottom-most position."""
        raise NotImplementedError

    @abc.abstractmethod
    def handle_window_border_x(self) -> None:
        """Define's the entity's behavior when it reaches the x-border of the window."""
        raise NotImplementedError

    @abc.abstractmethod
    def handle_window_border_y(self) -> None:
        """Define's the entity's behavior when it reaches the y-border of the window."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_surface(self) -> Surface:
        """Return the entity's internal Surface."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_rect(self) -> Rect:
        """Return the entity's internal Rect."""
