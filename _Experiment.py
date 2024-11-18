import unittest
import pyautogui
import Constants
import random
from main import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # player_state = Player()
        # window_position = GameWindow(Constants.GAME_WINDOW_ORIGIN, Constants.GAME_WINDOW_VERTEX)
        # self.computer_player = ComputerPlayer(player_state, window_position)
        pass

    def test_position(self):
        position = pyautogui.position()
        print(position)
        pixel = pyautogui.pixel(position[0],position[1])
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
        print(random.randrange(0,11))
        pass


if __name__ == '__main__':
    unittest.main()
