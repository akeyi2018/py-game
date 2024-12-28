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

        self.grass = pg.image.load(join('../maps','grass.png'))
        self.block = pg.image.load(join('../maps','block.png'))
        self.background_sprites = []
        self.block_sprites = []
        self.create_map()

    def create_map(self):
        # ここから
        for i, row in enumerate(TILE_MAP):
            for j, column in enumerate(row):
                x = j * TILE
                y = i * TILE
                
                self.background_sprites.append((x, y))
                if column == 'B':
                    self.block_sprites.append((x,y))

    def draw(self, screen):
        for x, y in self.background_sprites:
            screen.blit(self.grass, (x, y))

        for x, y in self.block_sprites:
            screen.blit(self.block, (x, y))