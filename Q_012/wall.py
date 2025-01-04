import pygame as pg
from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, pos, img_path, *groups):
        super().__init__(*groups)

        try:
            # イメージの読み込み
            self.surface = pg.image.load(img_path).convert_alpha()
        except:
            pass

        # rect
        self.rect = self.surface.get_frect(topleft=pos)

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, id, mob_pos, *groups):
        super().__init__(*groups)

        # イメージの読み込み
        self.enemy_obj = [
            {
                "name": "bat",
                "path": "../img/enemy/e001.png"
            },
            {
                "name": "sneck",
                "path": "../img/enemy/e002.png"
            },
            {
                "name": "サソリ",
                "path": "../img/enemy/e003.png"
            },
        ]

        self.id = id
        # 論理配置
        self.mob_pos = mob_pos
        # name
        self.name = self.enemy_obj[self.id]['name']
        self.surface = pg.image.load(self.enemy_obj[self.id]['path']).convert_alpha()
        self.surface = pg.transform.scale(self.surface, (64, 64))
        # 画面での位置
        self.pos = pos
        # rect
        self.rect = self.surface.get_frect(topleft=pos)
        self.enemy_sprites_type = True

