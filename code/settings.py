
# game options/settings
TITLE = "RPG Game"
MAIN_WIDTH, MAIN_HEIGHT = 1280, 720
FPS = 60
FONT_NAME = 'arial'
TILE = 64

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 1.2
PLAYER_JUMP = 20

TILE_MAP = {
    "map_01": [
        'BBBBBBBBBBBB.BBBBBBBBBBBBBBBBBBBBBBBBB',
        'B.........B..........................B',
        'B.........B.......BB.........B.......B',
        'B....BBBBBB.......BB.........B.......B',
        'B...................................P.',
        'B.....BBB.........BB.........B.......B',
        'B.....BBB.........BB.........B.......B',
        'B......BB.B.......BB.........B.......B',
        'B........E...F....BB.........B.......B',
        'B....BBBB.BB......BB.........B.......B',
        'B.........B.......BB.........B.......B',
        'B...........G.....BB.........B.......B',
        'B.................BB.........B.......B',
        'B....................................B',
        'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    ],
     "map_02": [
        'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
        'B....................................B',
        'B.................BB.........B.......B',
        'B....BBBBBB.......BB.........B.......B',
        'B.................BB.........B.......B',
        'B.....BBB.........BB.........B.......B',
        'B.....BBB.........BB.........B.......B',
        'B......BB.B..E....BB.........B.......B',
        'B.................BB.........B.......B',
        'B....BBBB.BB......BB.........B.......B',
        'B.........B.......BB.........B.......B',
        'B.................BB.........B.......B',
        'B.................BB.........B.......B',
        'B...........P........................B',
        'BBBBBBBBBBBB.BBBBBBBBBBBBBBBBBBBBBBBBB',
    ],
     "map_03": [
        'BBBBBBBBBBBBBBBBBBB',
        'B.................B',
        '..P...............B',
        '.....BBBBBB.......B',
        'BBBBBBBBBBBBBBBBBBB',
    ],
}

MAP_CONNECTIONS = {
    "map_01": {
        "up": ("map_02",(782,798)),
        "right": ("map_03",(80,102))
        },
    "map_02": {
        "down": ("map_01",(771,80))
        },
    "map_03": {
        "left": ("map_01",(2300,243))
        },
}

MAP_GRD = {
    "map_01": {
        ".": "grass.png"
    },
    "map_02": {
        ".": "g_002.png"
    },
    "map_03": {
        ".": "grass.png"
    }
}

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
