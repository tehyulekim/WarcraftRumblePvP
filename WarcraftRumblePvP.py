import Constants
import enum
import random
import pyautogui
import threading
import time

GameWindow_2_ON = True

def main():
    player_state = Player()
    t_controller = threading.Thread(target=keyboard_controller, args=[player_state])
    t_controller.start()

    window_position_1 = GameWindow(Constants.GAME_WINDOW_ORIGIN_1, Constants.GAME_WINDOW_VERTEX_1)
    computer_player_1 = ComputerPlayer(player_state, window_position_1)
    t_player_1 = threading.Thread(target=computer_player_1.play)
    t_player_1.start()

    if GameWindow_2_ON:
        window_position_2 = GameWindow(Constants.GAME_WINDOW_ORIGIN_2, Constants.GAME_WINDOW_VERTEX_2)
        computer_player_2 = ComputerPlayer(player_state, window_position_2)
        t_player_2 = threading.Thread(target=computer_player_2.play)
        t_player_2.start()

    t_controller.join()
    t_player_1.join()


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
        action = input("Write Action and Enter. Action: x to Exit. s to Stop. r to Run.\n")
        match action:
            case 'x':
                player.state = State.EXIT
                player.event_flag_play.set()  # to exit when stopped state
            case 's':
                player.state = State.STOP
                player.event_flag_play.clear()  # to False
                print("Stop flagged")
            case 'r':
                player.state = State.RUN
                player.event_flag_play.set()  # to True
                print("Running")


class GameWindow:
    def __init__(self, origin: tuple, vertex: tuple):
        self.origin = origin  # (3, 33) top left
        self.vertex = vertex  # (1020, 1389) bot right
        self.width = vertex[0] - origin[0]
        self.height = vertex[1] - origin[1]

        self.pvp_button_l = self.absolute_position(Constants.N_PVP_BUTTON_L)
        self.pvp_button_r = self.absolute_position(Constants.N_PVP_BUTTON_R)
        self.pvp_button_origin = self.absolute_position(Constants.N_PVP_BUTTON_ORIGIN)
        self.pvp_button_vertex = self.absolute_position(Constants.N_PVP_BUTTON_VERTEX)

        self.back_button_l = self.absolute_position(Constants.N_BACK_BUTTON_L)
        self.back_button_r = self.absolute_position(Constants.N_BACK_BUTTON_R)
        self.rumble_button_origin = self.absolute_position(Constants.N_RUMBLE_BUTTON_ORIGIN)
        self.rumble_button_vertex = self.absolute_position(Constants.N_RUMBLE_BUTTON_VERTEX)

        self.continue_button_l = self.absolute_position(Constants.N_CONTINUE_BUTTON_L)
        self.continue_button_r = self.absolute_position(Constants.N_CONTINUE_BUTTON_R)
        self.continue_button_origin = self.absolute_position(Constants.N_CONTINUE_BUTTON_ORIGIN)
        self.continue_button_vertex = self.absolute_position(Constants.N_CONTINUE_BUTTON_VERTEX)

        self.connection_error_ok_l = self.absolute_position(Constants.N_CONNECTION_ERROR_OK_BUTTON_L)
        self.connection_error_ok_r = self.absolute_position(Constants.N_CONNECTION_ERROR_OK_BUTTON_R)
        self.connection_error_ok_origin = self.absolute_position(Constants.N_CONNECTION_ERROR_OK_BUTTON_ORIGIN)
        self.connection_error_ok_vertex = self.absolute_position(Constants.N_CONNECTION_ERROR_OK_BUTTON_VERTEX)

        self.session_button_l = self.absolute_position(Constants.N_SESSION_BUTTON_L)
        self.session_button_r = self.absolute_position(Constants.N_SESSION_BUTTON_R)
        self.session_button_origin = self.absolute_position(Constants.N_SESSION_BUTTON_ORIGIN)
        self.session_button_vertex = self.absolute_position(Constants.N_SESSION_BUTTON_VERTEX)

        self.gold_8 = self.absolute_position(Constants.N_GOLD_8)
        self.gold_9 = self.absolute_position(Constants.N_GOLD_9)
        self.mini_1_origin = self.absolute_position(Constants.N_MINI_1_ORIGIN)
        self.mini_1_vertex = self.absolute_position(Constants.N_MINI_1_VERTEX)
        self.mini_2_origin = self.absolute_position(Constants.N_MINI_2_ORIGIN)
        self.mini_2_vertex = self.absolute_position(Constants.N_MINI_2_VERTEX)
        self.mini_3_origin = self.absolute_position(Constants.N_MINI_3_ORIGIN)
        self.mini_3_vertex = self.absolute_position(Constants.N_MINI_3_VERTEX)
        self.mini_4_origin = self.absolute_position(Constants.N_MINI_4_ORIGIN)
        self.mini_4_vertex = self.absolute_position(Constants.N_MINI_4_VERTEX)
        self.deploy_area_origin = self.absolute_position(Constants.N_DEPLOY_AREA_ORIGIN)
        self.deploy_area_vertex = self.absolute_position(Constants.N_DEPLOY_AREA_VERTEX)

    def absolute_position(self, position_normal: tuple) -> tuple:
        x = round(position_normal[0] * self.width + self.origin[0])
        y = round(position_normal[1] * self.height + self.origin[1])
        return x, y

    def button_match_color(self, button_l: tuple, button_r: tuple, color: tuple) -> bool:
        match1 = pyautogui.pixelMatchesColor(button_l[0], button_l[1], color, tolerance=64)
        match2 = pyautogui.pixelMatchesColor(button_r[0], button_r[1], color, tolerance=64)
        return match1 and match2

    def click_button_area_random(self, origin: tuple, vertex: tuple) -> None:
        x = random.randrange(origin[0], vertex[0])
        y = random.randrange(origin[1], vertex[1])
        pyautogui.click(x, y)

    # Game Actions
    def button_PvP_is_visible(self):
        return self.button_match_color(self.pvp_button_l, self.pvp_button_r, Constants.PVP_BUTTON_COLOR)

    def button_PvP_click(self):
        self.click_button_area_random(self.pvp_button_origin, self.pvp_button_vertex)

    def button_Rumble_Back_is_visible(self):
        return self.button_match_color(self.back_button_l, self.back_button_r, Constants.BACK_BUTTON_COLOR)

    def button_Rumble_click(self):
        self.click_button_area_random(self.rumble_button_origin, self.rumble_button_vertex)

    def button_Continue_is_visible(self):
        return self.button_match_color(self.continue_button_l, self.continue_button_r, Constants.CONTINUE_BUTTON_COLOR)

    def button_Continue_click(self):
        self.click_button_area_random(self.continue_button_origin, self.continue_button_vertex)

    def button_Connection_Error_OK_is_visible(self):
        return self.button_match_color(self.connection_error_ok_l, self.connection_error_ok_r, Constants.OK_BUTTON_COLOR)

    def button_Connection_Error_OK_click(self):
        self.click_button_area_random(self.connection_error_ok_origin, self.connection_error_ok_vertex)

    def button_Session_is_visible(self):
        return self.button_match_color(self.session_button_l, self.session_button_r, Constants.OK_BUTTON_COLOR)

    def button_Session_click_OK(self):
        self.click_button_area_random(self.session_button_origin, self.session_button_vertex)

    def gold_8_9_is_visible(self):
        return self.button_match_color(self.gold_8, self.gold_9, Constants.GOLD_COLOR)

    def mini_click_deploy(self, slot: int):
        match slot:
            case 1:
                self.click_button_area_random(self.mini_1_origin, self.mini_1_vertex)
            case 2:
                self.click_button_area_random(self.mini_2_origin, self.mini_2_vertex)
            case 3:
                self.click_button_area_random(self.mini_3_origin, self.mini_3_vertex)
            case 4:
                self.click_button_area_random(self.mini_4_origin, self.mini_4_vertex)
        time.sleep(0.2 + random.random() * 0.2)
        self.click_button_area_random(self.deploy_area_origin, self.deploy_area_vertex)
        time.sleep(0.2 + random.random() * 0.2)


class ComputerPlayer:
    def __init__(self, player: Player, game_window: GameWindow):
        self.player = player
        self.game_window = game_window

    def play(self):
        while self.player.state != State.EXIT:
            while self.player.state == State.STOP:
                print("Stopped")
                self.player.event_flag_play.wait()  # wait when event flag is False

            while self.player.state == State.RUN:
                if self.game_window.gold_8_9_is_visible():
                    slot = [1, 2, 3, 4]
                    random.shuffle(slot)
                    # print("mini slot: ", slot)
                    for x in slot:
                        self.game_window.mini_click_deploy(x)

                elif self.game_window.button_Rumble_Back_is_visible():
                    self.game_window.button_Rumble_click()

                elif self.game_window.button_Continue_is_visible():
                    self.game_window.button_Continue_click()

                elif self.game_window.button_Connection_Error_OK_is_visible():
                    self.game_window.button_Connection_Error_OK_click()

                # elif self.game_window.button_Session_is_visible():
                #     self.game_window.button_Session_click_OK()

                elif self.game_window.button_PvP_is_visible():
                    self.game_window.button_PvP_click()

                time.sleep(3 + random.random())  # randomize timing


if __name__ == '__main__':
    main()
