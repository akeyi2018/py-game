import pygame as pg
from settings import *


class Block(pg.sprite.Sprite):
    def __init__(self, pos, img_path, collision_sprites):
        super().__init__(collision_sprites)

        # イメージの読み込み
        self.img_path = img_path
        self.surface = pg.image.load(self.img_path).convert_alpha()
        # 位置
        self.pos = pos
        # rect
        self.rect = self.surface.get_frect(topleft=pos)

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, id, mob_pos, enemy_sprites):
        super().__init__(enemy_sprites)

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
    
    


