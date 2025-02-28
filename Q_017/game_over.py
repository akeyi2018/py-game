import pygame as pg

from settings import *
from utils import TextSprite, Button, TextAnimation
from save_load import GameData

class GameOver:
    def __init__(self, parent):
        self.parent = parent
        self.screen = self.parent.display_surface
        self.game_over_sprites = pg.sprite.Group()
        self.text = TextSprite('Game Over', 36, 
                               (255,255,255),  
                               (0,0,255), 
                               WIDTH / 2 -100, HEIGHT /2, self.game_over_sprites)

        self.text2 = TextSprite('Press Return Key TO CONTINUE...', 20, 
                               (255,255,255),  
                               (0,0,255), 
                               WIDTH / 2 -150, HEIGHT /2 + HEIGHT/4, self.game_over_sprites)
        
        self.input()
        
    def draw(self):
        self.text.draw(self.screen)
        self.text2.draw(self.screen)

    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            self.parent.game_stage = 'start_menu'
