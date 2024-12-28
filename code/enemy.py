import pygame as pg
from settings import *
from os.path import join

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)

        # 画像を読み込み
        original_image = pg.image.load(join('../img', 'enemy', 'e001.png')).convert_alpha()

        # 画像をリサイズ
        self.image = pg.transform.scale(original_image, (64, 64))

        # スプライトの位置を設定
        self.rect = self.image.get_rect(center=pos)
        self.rect.y += 30
