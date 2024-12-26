from settings import * 
import pygame as pg
from os.path import join

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load(join('./img','F1.png')).convert_alpha()
        # get_frectでないとバグがある
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.direction = pg.Vector2(0,0)
        self.speed = 10
        # self.moving = False  # 移動中かどうかを追跡

    def input(self):
        keys = pg.key.get_pressed()
        # キーが押されたときだけ移動
        self.direction.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.direction.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        # directionに基づいて移動
        self.rect.center += self.direction * self.speed * dt


    def update(self, dt):
        self.input()
        self.move(dt)