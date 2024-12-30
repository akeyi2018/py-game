import pygame as pg
from settings import *
from os.path import join
from PIL import Image, ImageSequence
import numpy as np

class GifLoader:
    def __init__(self, gif_path):
        self.gif_path = gif_path
        self.frames = self.load_transparent_gif()

    # GIFを読み込む関数
    def load_transparent_gif(self):
        gif = Image.open(self.gif_path)
        rgba_frames = []
        for frame in ImageSequence.Iterator(gif):
            frame_rgba = frame.convert("RGBA")
            frame_data = np.array(frame_rgba)
            alpha = frame_data[:, :, 3]  # アルファチャンネル

            # 背景を透明に設定
            frame_data[alpha == 0] = (255, 255, 255, 0)  # 完全に透明な部分は白色に
            rgba_frames.append(frame_data)

        return rgba_frames

    # GIFフレームをSurfaceに変換
    def convert_to_surface(self):
        loaded_frames = []
        for frame in self.frames:
            surface = pg.image.frombuffer(
                frame.tobytes(), frame.shape[1::-1], "RGBA"
            )
            loaded_frames.append(surface)
        return loaded_frames

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, enemy_type, *groups):
        super().__init__(*groups)

        # self.enemy_type = enemy_type  # 敵の種類

        # # 画像を読み込み
        # original_image = self.get_enemy_image(enemy_type)  # 種類に応じた画像

        # # 画像をリサイズ
        # self.image = pg.transform.scale(original_image, (64, 64))

        # # スプライトの位置を設定
        # self.rect = self.image.get_rect(center=pos)
        # self.rect.y += 30

        self.enemy_type = enemy_type  # 敵の種類



        # 画像を読み込み
        gif_loader = GifLoader(self.get_enemy_image_path(enemy_type))  # GIFを読み込む

        # GIFをSurfaceに変換
        self.frames = gif_loader.convert_to_surface()

        # 最初のフレームを設定
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=pos)
        self.rect.y += 30

        # アニメーションの設定
        self.frame_index = 0
        self.animation_speed = 0.5  # アニメーション速度
        self.frame_timer = 0

    def get_enemy_image_path(self, enemy_type):
        """
        種類に応じた画像を返す
        """
        if enemy_type == 'E':
            return join('../img', 'enemy', 'enemy_0020.gif')
        elif enemy_type == 'F':
            return join('../img', 'enemy', 'enemy_0003.gif')
        elif enemy_type == 'G':
            return join('../img', 'enemy', 'enemy_0010.gif')
        else:
            raise ValueError(f"未知の敵タイプ: {enemy_type}")
        
    def update(self, dt):
        # フレーム切り替えのタイミング
        self.frame_timer += dt
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]  # 次のフレームに更新
            self.rect = self.image.get_rect(center=self.rect.center)  # 位置更新