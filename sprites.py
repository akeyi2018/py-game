# Sprite classes
import pygame as pg
from settings import *

vec = pg.math.Vector2

class CollisionSprite(pg.sprite.Sprite):
    def __init__(self, pos, size, *groups):
        super().__init__(*groups)
        self.image = pg.Surface(size)
        self.image.fill(BLUE)
        self.rect = self.image.get_frect(center = pos)
