# Sprite classes
import pygame as pg
from settings import *

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

class Ground(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y