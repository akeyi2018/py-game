import pygame as pg
from utils import TextSprite 
from settings import *
from player_data import *

class PlayerStatus(pg.sprite.Sprite):
    def __init__(self, offset, bg_size, battle_sprites, *groups):
        super().__init__(*groups)

        self.offset = offset
        self.bg_size = bg_size
        self.status_list = {
            "name": NAME,
            "job": JOB,
            "HP": HP,
            "MP": MP,
            "LV": LV
        }
        self.font = pg.font.Font("../battle/Meiryo.ttf", 22)
        self.battle_sprites = battle_sprites

    def draw_status(self, screen):
        y_pos = []
        span = 30
        for i in range(1,6):
            y_pos.append(self.offset.y + span * i)

        for (k,v), y in zip(self.status_list.items(), y_pos):
            TextSprite(
                k + ' : ' + str(v), 
                self.font, 
                (255,255,255),(0,0,0), 
                self.offset.x + self.bg_size[0] + span,
                y, self.battle_sprites)

        # 枠
        self.p_area = pg.Rect(
            0,
            0, 
            self.offset.x -2,
            HEIGHT -2)
        self.surface = pg.Surface(self.p_area.size, pg.SRCALPHA)
        self.surface.fill((142,118,152,128))
        self.screen = screen
        self.screen.blit(self.surface,
                        [
                            self.p_area.x + 2 + self.offset.x + self.bg_size[0],
                            self.p_area.y + 2 + self.offset.y,
                            self.p_area.width -2,
                            self.p_area.height -2
                        ])
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







