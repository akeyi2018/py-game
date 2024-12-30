import pygame as pg
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


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, pos, gif_loader, groups):
        super().__init__(groups)
        self.gif_loader = gif_loader
        self.frames = gif_loader.convert_to_surface()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]  # 最初のフレーム
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_speed = 0.1  # アニメーション速度
        self.frame_timer = 0

    def update(self, dt):
        # フレーム切り替えのタイミング
        self.frame_timer += dt
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]  # 次のフレームに更新


# メインコード
pg.init()

# ウィンドウ設定
window_width, window_height = 800, 600
window = pg.display.set_mode((window_width, window_height))
clock = pg.time.Clock()

# GIFの読み込み
gif_loader = GifLoader("../img/enemy/enemy_0003.gif")

# Spriteグループ作成
all_sprites = pg.sprite.Group()

# AnimatedSpriteをグループに追加
sprite = AnimatedSprite((100, 100), gif_loader, all_sprites)

running = True
while running:
    dt = clock.tick(60) / 1000  # フレーム時間を秒単位で取得

    # イベント処理
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # スプライト更新
    all_sprites.update(dt)

    # 描画
    window.fill((255, 255, 255))  # 背景を白に
    all_sprites.draw(window)

    pg.display.flip()

pg.quit()
