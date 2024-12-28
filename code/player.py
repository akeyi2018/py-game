from settings import * 
import pygame as pg
from os.path import join
from os import walk


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # self.load_images()
        # self.image = pg.image.load(join('./img','F1.png')).convert_alpha()
        # get_frectでないとバグがある
        # self.rect = self.image.get_frect(center = pos)
        # self.state, self.frame_index = 'up', 0
        self.image = pg.image.load(join('../img', 'player', 'down', '0.png')).convert_alpha()
        self.surf = self.image
        # self.rect = self.image.get_frect(center = pos)

        # self.hitbox_rect = self.rect.inflate(-30,-30)

        # # movement
        # self.direction = pg.Vector2(0,0)
        # self.speed = 15
        # self.collision_sprites = collision_sprites

    def load_images(self):
        self.frames = {'left': [], 'right': [], 'up': [], 'down': []}

        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('img', 'player', state)):
                if file_names:
                    for file_name in sorted(file_names, key= lambda name: int(name.split('.')[0])):                     
                        full_path = join(folder_path, file_name)
                        surf = pg.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)

    def input(self):
        keys = pg.key.get_pressed()
        # キーが押されたときだけ移動
        self.direction.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.direction.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        # directionに基づいて移動
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        # self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        # self.collision('vertical')
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

    def animate(self, dt):
        # get state
        if self.direction.x != 0:
            self.state = 'right' if self.direction.x > 0 else 'left'
        elif self.direction.y != 0:
            self.state = 'down' if self.direction.y > 0 else 'up'

        # animate
        # 停止している場合は、アニメーション処理しない
        self.frame_index = self.frame_index + 3 * (dt / 5) if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def update(self, dt):
        pass
        # self.input()
        # self.move(dt)
        # self.animate(dt)