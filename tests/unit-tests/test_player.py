import unittest

from models.player import Player


class PlayerTestCase(unittest.TestCase):
    def test_border_x_right(self):
        # player with x speed of 2 and no y speed
        player = Player([2, 0])
        mock_window_width = 400

        # move the player until they have reached the edge of the window
        while player.get_right() <= mock_window_width:
            player.move()

        # since they have reached the edge of the window, invoke the handler for the border
        player.handle_window_border_x()

        # the player continues to move after the handler has been invoked
        player.move()

        # check to make sure that the player is not out of bounds
        self.assertLess(player.get_right(), mock_window_width)

    def test_border_x_left(self):
        player = Player([-2, 0])

        while player.get_left() > 0:
            player.move()

        player.handle_window_border_x()

        player.move()

        self.assertGreater(player.get_left(), 0)

    def test_border_y_bottom(self):
        player = Player([0, 2])
        mock_window_height = 400

        while player.get_bottom() <= mock_window_height:
            player.move()

        player.handle_window_border_y()

        player.move()

        self.assertLess(player.get_bottom(), mock_window_height)

    def test_border_y_top(self):
        player = Player([0, -2])

        while player.get_top() > 0:
            player.move()

        player.handle_window_border_y()

        player.move()

        self.assertGreater(player.get_top(), 0)


if __name__ == "__main__":
    unittest.main()
