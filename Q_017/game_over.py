import pygame as pg

from settings import *
from utils import TextSprite

class GameOver:
    def __init__(self):
        self.game_over_sprites = pg.sprite.Group()
        self.font = pg.font.Font("../battle/Meiryo.ttf", 36)
        self.text = TextSprite('Game Over', self.font, 
                               (255,255,255),  
                               (0,0,255), 
                               WIDTH / 2 -100, HEIGHT /2, self.game_over_sprites)
        self.font = pg.font.Font("../battle/Meiryo.ttf", 20)
        self.text2 = TextSprite('SPACE KEY TO CONTINUE...', self.font, 
                               (255,255,255),  
                               (0,0,255), 
                               WIDTH / 2 -150, HEIGHT /2 + HEIGHT/4, self.game_over_sprites)
