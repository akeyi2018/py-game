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
    def __init__(self, pos, enemy_obj, enemy_sprites):
        super().__init__(enemy_sprites)

        # イメージの読み込み
        self.enemy_obj = enemy_obj
        # name
        self.name = self.enemy_obj['name']
        self.surface = pg.image.load(self.enemy_obj['path']).convert_alpha()
        self.surface = pg.transform.scale(self.surface, (64, 64))
        # 位置
        self.pos = pos
        # rect
        self.rect = self.surface.get_frect(topleft=pos)
    
    def general_enemy(self):
        # Pの周囲に配置しないように最低限なマス数を決める
        non_enemy_area = 4

        # 敵を配置可能かどうか判定結果Listを作成