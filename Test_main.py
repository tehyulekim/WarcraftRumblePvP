import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        player_state = Player()
        window_position = GameWindow(GAME_WINDOW_ORIGIN, GAME_WINDOW_VERTEX)
        computer_player = ComputerPlayer(player_state, window_position)

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_normalize_position(self):
        """
        Input is absolute position, and output is normalized position eg (0 to 1)

        :return: normalized position
        """
        GAME_WINDOW_ORIGIN = (3, 33)  # x is where arrow disappears <->
        GAME_WINDOW_VERTEX = (1020, 1389)

        window_position = main.GameWindow(GAME_WINDOW_ORIGIN, GAME_WINDOW_VERTEX)

        # test input x (1020 - 3 )/ 2 = 508.5  => 0.5
        # test input y (1389-33) /2 = 678 => 0.5
        position_normalized = window_position.normalize_position((508.5, 678+33))

        self.assertAlmostEquals(position_normalized, 0.5)

        pass

    def test_position_absolute(self):
        GAME_WINDOW_ORIGIN = (3, 33)  # x is where arrow disappears <->
        GAME_WINDOW_VERTEX = (1020, 1389)

        window_position = main.GameWindow(GAME_WINDOW_ORIGIN, GAME_WINDOW_VERTEX)

        p =window_position.absolute_position((0.5,0.5))


        pass

if __name__ == '__main__':
    unittest.main()
