# # 3440x1440
# # Game Window
# GAME_WINDOW_ORIGIN_1 = (2, 33)
# GAME_WINDOW_VERTEX_1 = (1020, 1392)
#
# # Game Window 2
# GAME_WINDOW_ORIGIN_2 = (1056, 33)
# GAME_WINDOW_VERTEX_2 = (2072, 1392)

# 1600x900
# Game Window
GAME_WINDOW_ORIGIN_1 = (2, 33)
GAME_WINDOW_VERTEX_1 = (614, 852)

# Game Window 2
GAME_WINDOW_ORIGIN_2 = (953, 33)
GAME_WINDOW_VERTEX_2 = (1566, 852)

# --------------------------------------------
# Game Window for Normalizing Position
GAME_WINDOW_ORIGIN = (2, 33)
GAME_WINDOW_VERTEX = (1020, 1392)

# PvP Button for detection
PVP_BUTTON_L = (618, 1164)
PVP_BUTTON_R = (738, 1164)
PVP_BUTTON_COLOR = (224, 164, 14)
PVP_BUTTON_ORIGIN = (632, 1148)
PVP_BUTTON_VERTEX = (726, 1182)

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
CONTINUE_BUTTON_ORIGIN = (420, 1260)
CONTINUE_BUTTON_VERTEX = (600, 1290)

# OK Button
CONNECTION_OK_BUTTON_COLOR = (174, 46, 34)
SESSION_OK_BUTTON_COLOR = (183, 48, 36)  # (188, 50, 36)

r"""
------------586--------------
| 7  SAFE ZONE DEPLOY  1014 |    # 1/12 margin inner box length
------------854--------------
 
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

# Mini for pressing
MINI_1_ORIGIN = (338, 1157)
MINI_1_VERTEX = (408, 1191)
MINI_2_ORIGIN = (481, 1157)
MINI_2_VERTEX = (553, 1191)
MINI_3_ORIGIN = (626, 1157)
MINI_3_VERTEX = (697, 1191)
MINI_4_ORIGIN = (770, 1157)
MINI_4_VERTEX = (841, 1191)

# Deploy mini randomly in this area
DEPLOY_AREA_ORIGIN = (91, 608)
DEPLOY_AREA_VERTEX = (930, 832)

# -----------------------------------------
# PositionNormalized is based on Game Window 1 positions
origin = GAME_WINDOW_ORIGIN
vertex = GAME_WINDOW_VERTEX
width = vertex[0] - origin[0]
height = vertex[1] - origin[1]


def normalize_position(position: tuple) -> tuple:
    position_normal_x = (position[0] - origin[0]) / width
    position_normal_y = (position[1] - origin[1]) / height
    return position_normal_x, position_normal_y


# Normalized Positions
N_PVP_BUTTON_L = normalize_position(PVP_BUTTON_L)
N_PVP_BUTTON_R = normalize_position(PVP_BUTTON_R)
N_PVP_BUTTON_ORIGIN = normalize_position(PVP_BUTTON_ORIGIN)
N_PVP_BUTTON_VERTEX = normalize_position(PVP_BUTTON_VERTEX)

N_BACK_BUTTON_L = normalize_position(BACK_BUTTON_L)
N_BACK_BUTTON_R = normalize_position(BACK_BUTTON_R)
N_RUMBLE_BUTTON_ORIGIN = normalize_position(RUMBLE_BUTTON_ORIGIN)
N_RUMBLE_BUTTON_VERTEX = normalize_position(RUMBLE_BUTTON_VERTEX)

N_CONTINUE_BUTTON_L = normalize_position(CONTINUE_BUTTON_L)
N_CONTINUE_BUTTON_R = normalize_position(CONTINUE_BUTTON_R)
N_CONTINUE_BUTTON_ORIGIN = normalize_position(CONTINUE_BUTTON_ORIGIN)
N_CONTINUE_BUTTON_VERTEX = normalize_position(CONTINUE_BUTTON_VERTEX)

N_GOLD_8 = normalize_position(GOLD_8)
N_GOLD_9 = normalize_position(GOLD_9)

N_MINI_1_ORIGIN = normalize_position(MINI_1_ORIGIN)
N_MINI_1_VERTEX = normalize_position(MINI_1_VERTEX)
N_MINI_2_ORIGIN = normalize_position(MINI_2_ORIGIN)
N_MINI_2_VERTEX = normalize_position(MINI_2_VERTEX)
N_MINI_3_ORIGIN = normalize_position(MINI_3_ORIGIN)
N_MINI_3_VERTEX = normalize_position(MINI_3_VERTEX)
N_MINI_4_ORIGIN = normalize_position(MINI_4_ORIGIN)
N_MINI_4_VERTEX = normalize_position(MINI_4_VERTEX)

N_DEPLOY_AREA_ORIGIN = normalize_position(DEPLOY_AREA_ORIGIN)
N_DEPLOY_AREA_VERTEX = normalize_position(DEPLOY_AREA_VERTEX)

# ---------------
GAME_WINDOW_ORIGIN_1600 = (2, 33)
GAME_WINDOW_VERTEX_1600 = (614, 852)

origin1600 = GAME_WINDOW_ORIGIN_1600
vertex1600 = GAME_WINDOW_VERTEX_1600
width1600 = vertex1600[0] - origin1600[0]
height1600 = vertex1600[1] - origin1600[1]


def normalize_position1600(position: tuple) -> tuple:
    position_normal_x = (position[0] - origin1600[0]) / width1600
    position_normal_y = (position[1] - origin1600[1]) / height1600
    return position_normal_x, position_normal_y


N_PVP_LOGO = normalize_position1600((297, 117))
PVP_LOGO_COLOR = (177, 127, 41)
N_PVP_RUMBLE_BUTTON = normalize_position1600((400, 770))
PVP_RUMBLE_BUTTON_COLOR = (45, 174, 33)

# Calculate normal position at Experiment, must not overlap with PvP Cancel button
N_CONNECTION_ERROR_OK_BUTTON_L = normalize_position1600((260, 533))
N_CONNECTION_ERROR_OK_BUTTON_R = normalize_position1600((342, 533))
N_CONNECTION_ERROR_OK_BUTTON_ORIGIN = (0.4713584288052373, 0.5934065934065934)
N_CONNECTION_ERROR_OK_BUTTON_VERTEX = (0.5253682487725041, 0.6092796092796092)

# Session Timeout OK Button
# N_SESSION_BUTTON_L = (0.43044189852700493, 0.5995115995115995)
# N_SESSION_BUTTON_R = (0.43044189852700493, 0.5995115995115995)
# N_SESSION_BUTTON_ORIGIN = (0.4713584288052373, 0.5934065934065934)
# N_SESSION_BUTTON_VERTEX = (0.5253682487725041, 0.6092796092796092)

N_MAP_BUTTON_ORIGIN = (0.469721767594108, 0.9706959706959707)
N_MAP_BUTTON_VERTEX = (0.5188216039279869, 0.9731379731379731)


# When stuck searching for PvP, must cancel
N_PVP_CANCEL_BUTTON = normalize_position1600((310, 580))