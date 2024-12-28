from settings import * 
import pygame as pg
from os.path import join
from os import walk


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.frames = self.crop_character_frames(join('../img', 'char.png'))
        self.state = 'down'
        self.frame_index = 0

        self.image = pg.image.load(join('../img', 'char.png')).convert_alpha()
        self.crop_rect = pg.Rect(0,0,52,76)
        # 切り抜き用のサーフェスを作成して描画
        self.crop_img = pg.Surface(self.crop_rect.size, pg.SRCALPHA)  # 透過対応
        self.crop_img.blit(self.image, (0, 0), self.crop_rect)  # 切り抜きを適用

        self.surf = self.crop_img

        # get_frectでないとバグがある
        self.rect = self.crop_img.get_frect(center = pos)

        # self.hitbox_rect = self.rect.inflate(-30,-30)

        # # movement
        self.direction = pg.Vector2(0,0)
        self.speed = 64


        # self.collision_sprites = collision_sprites

    def crop_character_frames(self, image_path):
        """
        キャラクター画像を上下左右4コマずつ切り抜く関数。

        Args:
            image_path (str): キャラクター画像のパス。

        Returns:
            dict: 各方向（'up', 'down', 'left', 'right'）に対応するフレーム画像のリスト。
        """
        # 画像を読み込む
        image = pg.image.load(image_path).convert_alpha()

        # コマサイズを計算
        frame_width = 208 // 4  # 横方向のコマ数
        frame_height = 304 // 4  # 縦方向のコマ数

        # # リサイズ後のサイズ
        # resized_frame_width = frame_width // 2
        # resized_frame_height = frame_height // 2

        # 切り抜き領域を計算して保存
        directions = ['down', 'left', 'right', 'up']
        frames = {direction: [] for direction in directions}

        for i, direction in enumerate(directions):
            for frame in range(4):
                x = frame * frame_width  # 横の位置
                y = i * frame_height  # 縦の位置（上下左右の順）
                crop_rect = pg.Rect(x, y, frame_width, frame_height)

                # 切り抜き用サーフェス
                cropped_surface = pg.Surface((frame_width, frame_height), pg.SRCALPHA)
                cropped_surface.blit(image, (0, 0), crop_rect)

                # # サイズを半分にリサイズ
                # resized_surface = pg.transform.scale(
                #     cropped_surface, (resized_frame_width, resized_frame_height)
                # )

                # フレームをリストに追加
                frames[direction].append(cropped_surface)

        return frames

    def input(self):
        keys = pg.key.get_pressed()
        # キーが押されたときだけ移動
        self.direction.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.direction.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        
        self.direction = self.direction.normalize() if self.direction else self.direction
    
    def move(self, dt):
        # directionに基づいて移動
        self.rect.x += self.direction.x * self.speed * (dt) 
        self.rect.y += self.direction.y * self.speed * (dt)
        
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

         # フレームの切り替え速度を調整
        self.animation_speed = 4  # フレーム切り替え速度
        self.frame_index = self.frame_index + self.animation_speed * (dt) if self.direction else 0

        # アニメーションフレームのループ処理
        if self.frame_index >= len(self.frames[self.state]):
            self.frame_index = 0

        # 現在のフレーム画像を設定
        self.image = self.frames[self.state][int(self.frame_index)]
        self.surf = self.image

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)