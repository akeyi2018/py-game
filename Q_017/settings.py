# game options/settings
TITLE = "RPG Game"
WIDTH = 1280
HEIGHT = 640
BATTLE_WIN_WIDTH = 1000
BATTLE_WIN_HEIGHT = 640
FPS = 60

BLUE = (72, 133, 237)
RED = (255,0,0)
GREEN = (0,200,0)
WHITE = (255,255,255)

SURFACE_POS = (50,50)
BUILT_POS = (200,150)

IMAGE_PATH = '../img/F1.png'
BLOCK_PATH = '../maps/block1.png'

TILE_SIZE = 64
MAX_ENEMY_NUM = 5
NON_ENEMY_AREA = 2
MOB_AREA = 2 
TILE = {
    "map_01": [
        'BBBBBBBBBBBBBBBBBBB',
        'B.................B',
        'B.P...............B',
        'B.................B',
        'B.................B',
        'B.....BBBB........B',
        'B.................B',
        'B.................B',
        'BBBBBBBBBBBBBBBBBBB',
    ],
    }

MAX_MESSAGE = 6
MESSAGE_FONT_SIZE = 20
BG_SIZE_WIDTH = 819

FONT = "appmin.otf"

BGM = {
    "start_menu": '../music/kaisou/winter_flut.mp3',
    "main": '../music/town/Sky-Airship.mp3',
    "battle": '../music/battle/Battle-Rosemoon.mp3',
    "game_over": '../music/kaisou/reminiscence.mp3',
}

STAGE = 'start_menu'