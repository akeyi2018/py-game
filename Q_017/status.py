import pygame as pg
from utils import TextSprite 
from settings import *
from player_data import *

class PlayerStatus(pg.sprite.Sprite):
    def __init__(self, bg_size, battle_sprites, *groups):
        super().__init__(*groups)

        self.offset = pg.Vector2()
        self.offset.x = 231
        self.offset.y = 0
        
        self.bg_size = bg_size
        self.view_status = {
            "name": NAME,
            "job": JOB,
            "HP": HP,
            "MP": MP,
            "LV": LV
        }
        self.infact_status = {
            'ATK': 30,
            'DEF': 25
        }

        self.font = pg.font.Font("../battle/Meiryo.ttf", 22)
        self.battle_sprites = battle_sprites

    def draw_status(self, screen):
        # 枠
        self.p_area = pg.Rect(
            0,
            0, 
            self.offset.x -2,
            HEIGHT -2)
        self.surface = pg.Surface(self.p_area.size, pg.SRCALPHA)
        self.surface.fill((142,118,152,100))
        self.screen = screen
        self.screen.blit(self.surface,
                        [
                            self.p_area.x + 2 + self.offset.x + self.bg_size[0],
                            self.p_area.y + 2 + self.offset.y,
                            self.p_area.width -2,
                            self.p_area.height -2
                        ])
        y_pos = []
        span = 30
        for i in range(1,6):
            y_pos.append(self.offset.y + span * i)

        for (k,v), y in zip(self.view_status.items(), y_pos):
            text_sprite = TextSprite(
                k + ' : ' + str(v), 
                self.font, 
                (255,255,255),(0,0,0), 
                self.offset.x + self.bg_size[0] + span,
                y, self.battle_sprites)
            text_sprite.draw(screen)

        pg.draw.rect(self.screen,
                    '#D3DED0',
                    [
                        self.p_area.x + self.offset.x + self.bg_size[0],
                        self.offset.y,
                        self.offset.x,
                        int(HEIGHT )
                    ], 
                    3, 
                    border_radius=5)
