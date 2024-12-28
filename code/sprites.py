# Sprite classes
import pygame as pg
from settings import *
from os.path import join

vec = pg.math.Vector2

class CollisionSprite(pg.sprite.Sprite):
    def __init__(self, pos, surf, *groups):
        super().__init__(*groups)
        self.image = surf
        # self.image.fill(BLUE)
        self.rect = self.image.get_frect(topleft = pos)
        # self.grd = True

class Sprite(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.grd = True

class BackGround(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.full_image = pg.image.load(join('../maps','base_map.png'))

        # 画像を切り取る範囲を指定（左上から32x32の範囲）
        crop_rect = pg.Rect(0, 0, 32, 32)  # (x, y, width, height)

        # 切り取った部分を新しいSurfaceとして取得
        cropped_surface = self.full_image.subsurface(crop_rect).copy()

        # スプライトの位置を設定
        # self.rect = self.image.get_rect(topleft=pos)
        # 切り取った画像を縦横2倍に拡大
        self.image = pg.transform.scale(cropped_surface, (64, 64))

        self.background_sprites = []
        self.create_map()

    def create_map(self):
        # ここから
        for i, row in enumerate(TILE_MAP):
            for j, column in enumerate(row):
                if column == '.':
                    x = j * TILE
                    y = i * TILE
                    self.background_sprites.append((x, y))

    def draw(self, screen):
        for x, y in self.background_sprites:
            screen.blit(self.image, (x, y))