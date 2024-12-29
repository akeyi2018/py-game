import pygame as pg
from settings import *
from os.path import join

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, enemy_type, *groups):
        super().__init__(*groups)

        self.enemy_type = enemy_type  # 敵の種類

        # 画像を読み込み
        original_image = self.get_enemy_image(enemy_type)  # 種類に応じた画像

        # 画像をリサイズ
        self.image = pg.transform.scale(original_image, (64, 64))

        # スプライトの位置を設定
        self.rect = self.image.get_rect(center=pos)
        self.rect.y += 30

    def get_enemy_image(self, enemy_type):
        """
        種類に応じた画像を返す
        """
        if enemy_type == 'E':
            return pg.image.load(join('../img', 'enemy', 'e001.png')).convert_alpha()
        elif enemy_type == 'F':
            return pg.image.load(join('../img', 'enemy', 'e002.png')).convert_alpha()
        elif enemy_type == 'G':
            return pg.image.load(join('../img', 'enemy', 'e003.png')).convert_alpha()
        else:
            raise ValueError(f"未知の敵タイプ: {enemy_type}")