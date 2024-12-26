
# game options/settings
TITLE = "RPG Game"
WIDTH = 1280
HEIGHT = 720
FPS = 60
FONT_NAME = 'arial'

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 1.2
PLAYER_JUMP = 20

# NEW!! Platformをリスト化
# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
MOJICOLOR = (255,255,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (27, 140, 141)
LIGHTGREY = (189, 195, 199)
GREEN = (60, 186, 84)
RED = (219, 50, 54)
YELLOW = (244, 194, 13)
BLUE = (72, 133, 237)
LIGHTBLUE = (41, 128, 185)
BGCOLOR = LIGHTBLUE
