from settings import * 
import pygame as pg

class Player(pg.sprite.Sprite):
    
    def __init__(self, pos, collision_sprites, enemy_sprites):
        super().__init__()

        self.collision_sprites = collision_sprites
        self.enemy_sprites = enemy_sprites
        # イメージの読み込み
        self.surface = pg.image.load(IMAGE_PATH).convert_alpha()

        # 矩形（rect）と位置情報
        self.rect = self.surface.get_frect(topleft=pos)
        self.hit_box_rect = self.rect.inflate(-10,-10)

        # 移動関連
        self.key_speed = 10
        self.direction = pg.Vector2(0, 0)
        self.game_stage = 'main'
        self.enemy_name = ''

    def handle_input(self, dt):
        """キーボード入力で移動処理を行う"""
        keys = pg.key.get_pressed()

        # キーが押されたときだけ移動
        self.direction.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.direction.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        
        self.direction = self.direction.normalize() if self.direction else self.direction

    def collision_enemy(self, dt, enemy_list):

        collided_enemies = []  # 衝突した敵を記録するリスト

        # 水平方向、垂直方向の衝突判定を処理
        self.hit_box_rect.x += self.direction.x * self.key_speed * dt
        self.hit_box_rect.y += self.direction.y * self.key_speed * dt

        for enemy_sprite, enemy in zip(self.enemy_sprites, enemy_list):
            if enemy_sprite.rect.colliderect(self.hit_box_rect):
                print(f'{enemy.name}と衝突しました！')
                self.game_stage = 'battle'
                self.enemy_name = enemy.name
                collided_enemies.append((enemy_sprite, enemy))

        # 衝突した敵を削除
        for enemy_sprite, enemy in collided_enemies:
            if enemy_sprite in self.enemy_sprites:
                self.enemy_sprites.remove(enemy_sprite)  # スプライトグループから削除
            if enemy in enemy_list:
                enemy_list.remove(enemy)  # インスタンスリストから削除
            # enemy.destroy()  # 敵のリソースを解放

        # メイン矩形をヒットボックスに同期
        self.rect.center = self.hit_box_rect.center

    def collision_block(self,dt):
        """ブロックとの衝突判定と位置調整を行う"""
        # 水平方向の衝突処理
        self.hit_box_rect.x += self.direction.x * self.key_speed *dt
        for block in self.collision_sprites:
            if block.rect.colliderect(self.hit_box_rect):
                if self.direction.x > 0:  # 右に移動中
                    self.hit_box_rect.right = block.rect.left
                elif self.direction.x < 0:  # 左に移動中
                    self.hit_box_rect.left = block.rect.right
                # 衝突後、移動量をリセット
                self.direction.x = 0

        # 垂直方向の衝突処理
        self.hit_box_rect.y += self.direction.y * self.key_speed *dt
        for block in self.collision_sprites:
            if block.rect.colliderect(self.hit_box_rect):
                if self.direction.y > 0:  # 下に移動中
                    self.hit_box_rect.bottom = block.rect.top
                elif self.direction.y < 0:  # 上に移動中
                    self.hit_box_rect.top = block.rect.bottom
                # 衝突後、移動量をリセット
                self.direction.y = 0

        # メイン矩形をヒットボックスに同期
        self.rect.center = self.hit_box_rect.center

    def update(self, dt, enemy_list):
        self.handle_input(dt)
        self.collision_block(dt)
        self.collision_enemy(dt, enemy_list)
