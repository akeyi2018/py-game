import pygame as pg
from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, pos, img_path, *groups):
        super().__init__(*groups)

        try:
            # イメージの読み込み

            self.image = pg.image.load(img_path).convert_alpha()
            self.surface = pg.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        except:
            pass

        # rect
        self.rect = self.surface.get_frect(topleft=pos)

