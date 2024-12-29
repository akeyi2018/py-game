# Sprite classes
import pygame as pg
from settings import *
from os.path import join

vec = pg.math.Vector2

class CollisionSprite(pg.sprite.Sprite):
    def __init__(self, pos, surface, all_sprites, collision_sprites):
        super().__init__(all_sprites, collision_sprites)

        # 画像を設定
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)

        # mask を作成（画像の不透明部分に基づいて作成）
        self.mask = pg.mask.from_surface(self.image)

class Sprite(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.grd = True
