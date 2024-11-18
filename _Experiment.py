import unittest
import pyautogui
import Constants
import random
from WarcraftRumblePvP import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # player_state = Player()
        # window_position = GameWindow(Constants.GAME_WINDOW_ORIGIN, Constants.GAME_WINDOW_VERTEX)
        # self.computer_player = ComputerPlayer(player_state, window_position)
        pass

    def test_position_color(self):
        position = pyautogui.position()
        print(position)
        pixel = pyautogui.pixel(position[0], position[1])
        print(pixel)
        pass

    def test_2(self):
        # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
        pyautogui.click(500, 500, 1)
        # pyautogui.rightClick(500, 500, 1)
        pass

    def test_3(self):
        try:
            v1 = pyautogui.locateOnScreen('Image_Button/Back.png')
            print(v1)
        except:
            pass

    def test_4(self):
        screenshot1 = pyautogui.screenshot('screenshot1.png')  # , region=(0, 0, 1600, 900))
        pixel1 = screenshot1.getpixel((1960, 1040))  # (182, 49, 37)
        match1 = pyautogui.pixelMatchesColor(1960, 1040, (182, 49, 37), tolerance=16)
        pass

    def test_screenshot(self):
        self.computer_player.game_window.screenshot_save()
        pass

    def test_Button_found(self):
        x = self.computer_player.Rumble_Back_button_found()
        pass

    def test_random(self):
        print(random.randrange(0, 11))

        a1 = [1, 2, 3, 4]
        random.shuffle(a1)
        print(a1)

        pass

    def test_normalize(self):
        GAME_WINDOW_ORIGIN_1 = (3, 33)
        GAME_WINDOW_VERTEX_1 = (614, 852)
        origin = GAME_WINDOW_ORIGIN_1
        vertex = GAME_WINDOW_VERTEX_1
        width = vertex[0] - origin[0]
        height = vertex[1] - origin[1]

        def normalize_position(position: tuple) -> tuple:
            position_normal_x = (position[0] - origin[0]) / width
            position_normal_y = (position[1] - origin[1]) / height
            return position_normal_x, position_normal_y

        # Session Timeout OK Button detection
        N_SESSION_BUTTON_L = normalize_position(0.4, 0.65) #
        N_SESSION_BUTTON_R = normalize_position(0.6, 0.65) #

        # Session Timeout OK Button for pressing
        N_SESSION_BUTTON_ORIGIN = normalize_position(0.4, 0.6) #
        N_SESSION_BUTTON_VERTEX = normalize_position(0.6, 0.7) #

        pass


if __name__ == '__main__':
    unittest.main()
