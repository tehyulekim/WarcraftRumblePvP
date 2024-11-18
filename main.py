import enum
import pyautogui
import threading
import time
import Constants


def main():
    player_state = Player()
    t_controller = threading.Thread(target=keyboard_controller, args=[player_state])

    window_position = GameWindow(Constants.GAME_WINDOW_ORIGIN, Constants.GAME_WINDOW_VERTEX)
    # window_position2 = GameWindow(GAME_WINDOW_ORIGIN_2, GAME_WINDOW_VERTEX_2)

    computer_player = ComputerPlayer(player_state, window_position)
    # computer_player2 = ComputerPlayer(player_state, window_position2)

    t_player = threading.Thread(target=computer_player.play)
    # t_player2 = threading.Thread(target=computer_player2.play)

    t_controller.start()
    t_player.start()

    t_controller.join()
    t_player.join()


class State(enum.Enum):
    EXIT = enum.auto()
    STOP = enum.auto()
    RUN = enum.auto()


class Player:
    def __init__(self) -> None:
        self.state = State.STOP
        self.event_flag_play = threading.Event()  # Purpose is to pause computer_player thread
        self.event_flag_play.clear()  # flag is False when stopped. True when resuming


# class GameComputer:  
def keyboard_controller(player: Player):
    while player.state != State.EXIT:
        action = input("Write Action and Enter. Action: x to Exit. s to Stop. r to Run.")
        match action:
            case 'x':
                player.state = State.EXIT
                player.event_flag_play.set()  # to exit when stopped state
            case 's':
                player.state = State.STOP
                player.event_flag_play.clear()
            case 'r':
                player.state = State.RUN
                player.event_flag_play.set()


class PositionNormalized:
    def __init__(self):
        self.origin = Constants.GAME_WINDOW_ORIGIN  # (3, 33)
        self.vertex = Constants.GAME_WINDOW_VERTEX  # (1020, 1389)

        self.width = self.vertex[0] - self.origin[0]
        self.height = self.vertex[1] - self.origin[1]

        # Normalized position has n_ prefix
        self.n_back_button_l = self.normalize_position(Constants.BACK_BUTTON_L)
        self.n_back_button_r = self.normalize_position(Constants.BACK_BUTTON_R)


    # MousePos.exe absolute position to normalized position
    def normalize_position(self, position: tuple) -> tuple:
        position_normal_x = (position[0] - self.origin[0]) / self.width
        position_normal_y = (position[1] - self.origin[1]) / self.height
        return position_normal_x, position_normal_y




# Instance
class GameWindow:
    def __init__(self, top_left: tuple, bot_right: tuple):
        self.origin = top_left  # (3, 33)
        self.vertex = bot_right  # (1020, 1389)
        self.width = bot_right[0] - top_left[0]
        self.height = bot_right[1] - top_left[1]

        self.back_button_l = self.absolute_position()
        self.back_button_r = self.absolute_position()

    def absolute_position(self, position_normal: tuple) -> tuple:
        position_x = round(position_normal[0] * self.width + self.origin[0])
        position_y = round(position_normal[1] * self.height + self.origin[1])
        return position_x, position_y

    def get_screenshot(self):
        return pyautogui.screenshot()

    def get_screenshot_save(self):
        screenshot1 = pyautogui.screenshot('screenshot1.png')
        return screenshot1


class ComputerPlayer:
    def __init__(self, player: Player, game_window: GameWindow):
        self.player = player
        self.game_window = game_window

    def play(self):
        while self.player.state != State.EXIT:
            while self.player.state == State.STOP:
                self.player.event_flag_play.wait()  # wait when flag is False
            while self.player.state == State.RUN:
                print(str(self.player.state))
                time.sleep(2) # randomize timing

                # screenshot

                if self.Rumble_Back_button_found():
                    self.Rumble_button_click()

                if self.Continue_button_found():
                    self.Continue_button_click()

                if self.Gold_10_found():
                    self.Mini_deploy()

    def Button_match(self, button_l: tuple, button_r: tuple, color: tuple) -> bool:
        match1 = pyautogui.pixelMatchesColor(button_l[0], button_l[1], color, tolerance=64)
        match2 = pyautogui.pixelMatchesColor(button_r[0], button_r[1], color, tolerance=64)
        return match1 and match2

    def Button_click_humanized(self, origin: tuple, vertex: tuple):

        pass

    def Rumble_Back_button_found(self):
        return self.Button_match(self.game_window.back_button_l, self.game_window.back_button_r, (182, 49, 37))

    def Rumble_button_click(self):
        pass

    def Continue_button_found(self):
        pass

    def Continue_button_click(self):
        pass

    def Gold_10_found(self):
        pass

    def Mini_deploy(self):
        pass


if __name__ == '__main__':
    main()
