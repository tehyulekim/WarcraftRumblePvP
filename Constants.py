# Game Window
GAME_WINDOW_ORIGIN_1 = (3, 33)
GAME_WINDOW_VERTEX_1 = (1020, 1392)

# Game Window 2
GAME_WINDOW_ORIGIN_2 = (0, 0)
GAME_WINDOW_VERTEX_2 = (1, 1)

# --------------------------------------------
# Game Window for Normalizing Position
GAME_WINDOW_ORIGIN = (3, 33)
GAME_WINDOW_VERTEX = (1020, 1392)

# Back Button pixels for Rumble Button detection
BACK_BUTTON_L = (260, 1276)
BACK_BUTTON_R = (420, 1276)
BACK_BUTTON_COLOR = (182, 49, 37)

# Rumble Button area to click and start PvP
RUMBLE_BUTTON_ORIGIN = (595, 1263)
RUMBLE_BUTTON_VERTEX = (758, 1292)

# Continue Button for detection
CONTINUE_BUTTON_L = (404, 1272)
CONTINUE_BUTTON_R = (614, 1272)
CONTINUE_BUTTON_COLOR = (25, 91, 198)

# Continue Button for pressing
CONTINUE_BUTTON_ORIGIN = (420, 1260)
CONTINUE_BUTTON_VERTEX = (600, 1290)

r"""
--------586-----------------
| 7  SAFE ZONE DEPLOY  1014 |    # 1/12 margin inner box length
--------854------------------
 
PvP menu
------- 1141------
SAFE ZONE for mini selection
-------1207-------
box height = 66


Mini button box
--------y 1101-------
| 302 Mini1 444 | 445 Mini 2 589 | 590  M3  733 | 734 M4 877 |
-------y 1314-------
box width = 142 # /4 = 36
box height = 213  # /4 = 53, don't use this, use safe zone instead, 66/4 = 16
Inner box is 25% less length. 

"""

# Gold for detection
GOLD_8 = (731, 1352)
GOLD_9 = (781, 1352)
GOLD_COLOR = (223, 207, 73)  # max (255, 238, 84), tolerance=64

# Mini 1 for pressing
MINI_1_ORIGIN = (338, 1157)
MINI_1_VERTEX = (408, 1191)
MINI_2_ORIGIN = (481, 1157)
MINI_2_VERTEX = (553, 1191)
MINI_3_ORIGIN = (626, 1157)
MINI_3_VERTEX = (697, 1191)
MINI_4_ORIGIN = (770, 1157)
MINI_4_VERTEX = (841, 1191)

DEPLOY_AREA_ORIGIN = (91, 608)
DEPLOY_AREA_VERTEX = (930, 832)

# PositionNormalized is based on Game Window 1 positions
origin = GAME_WINDOW_ORIGIN
vertex = GAME_WINDOW_VERTEX
width = vertex[0] - origin[0]
height = vertex[1] - origin[1]


def normalize_position(position: tuple) -> tuple:
    position_normal_x = (position[0] - origin[0]) / width
    position_normal_y = (position[1] - origin[1]) / height
    return position_normal_x, position_normal_y


n_back_button_l = normalize_position(BACK_BUTTON_L)
print(n_back_button_l)
