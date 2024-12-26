from settings import * 
import pygame as pg
from os.path import join


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pg.image.load(join('./img','F1.png')).convert_alpha()
        # get_frectでないとバグがある
        self.rect = self.image.get_frect(center = pos)

        self.hitbox_rect = self.rect.inflate(-10,0)

        # movement
        self.direction = pg.Vector2(0,0)
        self.speed = 15
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pg.key.get_pressed()
        # キーが押されたときだけ移動
        self.direction.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.direction.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        # directionに基づいて移動
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        # hitboxで衝突を検知し、座標を戻す
        self.rect.center = self.hitbox_rect.center

    def collision(self,direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                elif direction == 'vertical':
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom


    def update(self, dt):
        self.input()
        self.move(dt)