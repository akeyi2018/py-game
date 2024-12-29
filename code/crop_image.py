import pygame as pg

from settings import *
from os.path import join

class BackGround(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pg.init()
        pg.display.set_mode((400,200))
        # 元画像を読み込む
        self.full_image = pg.image.load(join('../maps', 'base_map.png')).convert_alpha()

        # 切り取る範囲を指定（左上から32x32の範囲）
        crop_rect = pg.Rect(1, 705, 32, 32)  # (x, y, width, height)

        # 切り取った部分を新しいSurfaceとして取得
        cropped_surface = self.full_image.subsurface(crop_rect).copy()

        # 切り取った画像を縦横2倍に拡大
        self.image = pg.transform.scale(cropped_surface, (64, 64))

        # 切り取った画像を保存
        self.save_cropped_image(self.image, '../maps/cropped_image.png')

        pg.quit()

    def save_cropped_image(self, image, save_path):
        """
        切り取った画像を指定されたパスに保存する。

        Args:
            image (Surface): 保存するSurfaceオブジェクト。
            save_path (str): 保存先のファイルパス。
        """
        pg.image.save(image, save_path)
        print(f"画像を保存しました: {save_path}")

if __name__ == "__main__":
    new_game = BackGround()
    # new_game.run()