from sub.settings import * 
import pygame as pg
import random
from enemy import Enemy
from enemy_maneger import EntryEnemy


class Player(pg.sprite.Sprite):
    
    def __init__(self, parent, pos, collision_sprites, enemy_sprites, npc_sprites, all_sprites, *groups):
        super().__init__(*groups)

        self.parent = parent
        self.collision_sprites = collision_sprites
        self.enemy_sprites = enemy_sprites
        self.npc_sprites = npc_sprites
        self.all_sprites = all_sprites
        self.pos = pos

        # イメージの読み込み
        self.ori_surface = pg.image.load(IMAGE_PATH).convert_alpha()
        self.surface = pg.transform.scale(self.ori_surface,(TILE_SIZE, TILE_SIZE))

        # 矩形（rect）と位置情報
        self.rect = self.surface.get_frect(topleft=self.pos)
        self.hit_box_rect = self.rect.inflate(-10,-10)

        # 移動関連
        self.key_speed = 10
        self.direction = pg.Vector2(0, 0)
        self.game_stage = 'main'
        # self.enemy_name = ''
        self.collided_enemy = None
        
        self.all_sprites.add(self)

    def handle_input(self, dt):
        """キーボード入力で移動処理を行う"""
        keys = pg.key.get_pressed()

        # キーが押されたときだけ移動
        self.direction.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.direction.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        
        self.direction = self.direction.normalize() if self.direction else self.direction

    def collision_enemy(self, dt, base_map):

        collided_enemies = []  # 衝突した敵を記録するリスト

        # 水平方向、垂直方向の衝突判定を処理
        self.hit_box_rect.x += self.direction.x * self.key_speed * dt
        self.hit_box_rect.y += self.direction.y * self.key_speed * dt

        for enemy_sprite in self.enemy_sprites:
            if enemy_sprite.rect.colliderect(self.hit_box_rect):
                # print(f'{enemy_sprite.name}と衝突しました！')
                # print(f'x:{int(self.hit_box_rect.centerx / TILE_SIZE)}\
                #       y:{int(self.hit_box_rect.centery / TILE_SIZE)}')
                try:
                    # att = enemy_sprite.surface
                    # print(att)
                    self.collided_enemy = enemy_sprite
                    # print(type(self.collided_enemy))
                    # print(enemy_sprite.__dict__.keys())
                    # print('OK')
                    self.parent.game_stage = 'battle'
                    collided_enemies.append(enemy_sprite) #あとで集計ログで使うので残す
                except Exception as e:
                    print(f'予想しない敵と衝突: {e}')

        # Mobの位置を取得
        self.mob_pos_info = [enemy.mob_pos for enemy in self.enemy_sprites]

        # 衝突した敵を削除
        for enemy_sprite in collided_enemies:
            if enemy_sprite in self.enemy_sprites:
                # スプライトグループから削除
                enemy_sprite.kill()
                # self.enemy_sprites.remove(enemy_sprite)

                # self.enemy_sprites = [e for e in self.enemy_sprites if e.alive()]  # `alive()` で生存チェック

        if len(self.mob_pos_info) < MAX_ENEMY_NUM:
            # Mob生成
            self.general_mob(base_map)
        
        # メイン矩形をヒットボックスに同期
        self.rect.center = self.hit_box_rect.center
        # self.debug_enemy_sprites()

    def cal_mob_area(self, mob_pos_info, max_y, max_x):

        all_list = []
        for px, py in mob_pos_info:

            # NONエリアの計算
            px_min = max(0, px - MOB_AREA)
            px_max = min(max_x - 1, px + MOB_AREA)
            py_min = max(0, py - MOB_AREA)
            py_max = min(max_y - 1, py + MOB_AREA)

            mob_area = []
            for p_y in range(py_min, py_max + 1):
                for p_x in range(px_min, px_max + 1):
                    mob_area.append([p_x, p_y])  # 各座標をリストに追加
            
            all_list.extend(mob_area)

        return all_list
    
    def debug_enemy_sprites(self):
        print("=== Debug Enemy Sprites ===")
        for enemy in self.enemy_sprites:
            print(f"Enemy at ({enemy.rect.x}, {enemy.rect.y}) - Alive: {enemy.alive()}")

        print(f"Total enemies: {len(self.enemy_sprites)}")
    
    def place_exits_mob(self, map_data, mob_pos_info, num):
        max_y = len(map_data)
        max_x = len(map_data[0])

        for x, y in mob_pos_info:
            # 範囲外アクセスを防ぐチェック
            # if 0 <= y < max_y and 0 <= x < max_x:
            if map_data[y][x] == 0:  # 配置可能な場所
                map_data[y][x] = num  # モンスターを配置
            else:
                # print(f"座標 ({x}, {y}) にモンスターを配置できません。")
                pass
            # else:
            #     print(f"座標 ({x}, {y}) はマップの範囲外です。")
        return map_data

    def get_base_map(self, current_map):
        base_map = []
        for i, row in enumerate(current_map):
            row_area = []
            for j, column in enumerate(row):
                # BlockとNPC
                if column == 'B' or column == 'N':
                    row_area.append(1) 
                else:
                    row_area.append(0)
            base_map.append(row_area)

        return base_map

    def general_mob(self, map_data):

        max_map_y = len(map_data)
        max_map_x = len(map_data[0])

        # Mob配置禁止エリアの計算
        self.non_mob_area = self.cal_mob_area(self.mob_pos_info, max_map_y, max_map_x)

        # 既存のMobを配置する
        self.updated_map = self.place_exits_mob(map_data, self.non_mob_area, 9)

        # 配置禁止エリアの計算
        p = self.cal_player_area(max_map_y, max_map_x)
        self.place_result_map = self.place_exits_mob(self.updated_map, p, 3)

        # 配置可能な座標を取得
        zero_positions = [(i, j) for i, row in enumerate(self.place_result_map) for j, val in enumerate(row) if val == 0]
        # print(zero_positions)
        if zero_positions:
            new_mob = random.sample(zero_positions, 1)
            flattened_list = [item for tup in new_mob for item in tup]
            print(f'配置したモンスター: {flattened_list}')
            # ランダムでMobを生成
            id = random.randint(0, 2)
            x = flattened_list[0] * TILE_SIZE
            y = flattened_list[1] * TILE_SIZE

            # Mob生成
            entry = EntryEnemy()
            mob_info = entry.generate_random_enemy()
            Enemy((y, x), mob_info, flattened_list, self.enemy_sprites)
        else:
            print("モンスターを配置できるスペースがありません。")

        # return new_enemy
    
    def cal_player_area(self, max_y, max_x):
        # プレイヤーのタイル位置を計算
        px = int(self.rect.centerx / TILE_SIZE)
        py = int(self.rect.centery / TILE_SIZE)

        # NONエリアの計算
        px_min = max(0, px - NON_ENEMY_AREA)
        px_max = min(max_x - 1, px + NON_ENEMY_AREA)
        py_min = max(0, py - NON_ENEMY_AREA)
        py_max = min(max_y - 1, py + NON_ENEMY_AREA)

        player_area = []
        for p_y in range(py_min, py_max + 1):
            for p_x in range(px_min, px_max + 1):
                player_area.append([p_x, p_y])  # 各座標をリストに追加

        return player_area


    def collision_npc(self, dt):
        """ブロックとの衝突判定と位置調整を行う"""
        # 水平方向の衝突処理
        self.hit_box_rect.x += self.direction.x * self.key_speed *dt
        for block in self.npc_sprites:
            if block.rect.colliderect(self.hit_box_rect):
                # print('ここから先には行けません。')
                self.parent.game_stage = 'community'
                if self.direction.x > 0:  # 右に移動中
                    self.hit_box_rect.right = block.rect.left
                elif self.direction.x < 0:  # 左に移動中
                    self.hit_box_rect.left = block.rect.right
                # 衝突後、移動量をリセット
                self.direction.x = 0


        # 垂直方向の衝突処理
        self.hit_box_rect.y += self.direction.y * self.key_speed *dt
        for block in self.npc_sprites:
            if block.rect.colliderect(self.hit_box_rect):
                # print('ここから先には行けません。')
                if self.direction.y > 0:  # 下に移動中
                    self.hit_box_rect.bottom = block.rect.top
                elif self.direction.y < 0:  # 上に移動中
                    self.hit_box_rect.top = block.rect.bottom
                # 衝突後、移動量をリセット
                self.direction.y = 0

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
                if self.direction.x < 0:  # 左に移動中
                    self.hit_box_rect.left = block.rect.right
                # 衝突後、移動量をリセット
                self.direction.x = 0

        # 垂直方向の衝突処理
        self.hit_box_rect.y += self.direction.y * self.key_speed *dt
        for block in self.collision_sprites:
            if block.rect.colliderect(self.hit_box_rect):
                if self.direction.y > 0:  # 下に移動中
                    self.hit_box_rect.bottom = block.rect.top
                if self.direction.y < 0:  # 上に移動中
                    self.hit_box_rect.top = block.rect.bottom
                # 衝突後、移動量をリセット
                self.direction.y = 0

        # メイン矩形をヒットボックスに同期
        self.rect.center = self.hit_box_rect.center

    def update(self, dt, current_map):
        base_map = self.get_base_map(current_map)
        self.handle_input(dt)
        self.collision_block(dt)
        self.collision_npc(dt)
        self.collision_enemy(dt, base_map)


    def check_map_transition(self):
        """
        プレイヤーの位置を監視し、マップ遷移をチェックする
        """
        # print(f'X:{self.rect.x} Y:{self.rect.y}')
        tile_x = int(self.rect.centerx / TILE_SIZE)
        tile_y = int(self.rect.centery / TILE_SIZE)

        # 左端
        if self.rect.left < 0:
            return "left"  # 左マップへ遷移
        # 右端
        elif tile_x > TILE * len(self.current_map[0]):
            return "right"  # 右マップへ遷移
        # 上端
        elif self.rect.top < 0:
            return "up"  # 上マップへ遷移
        # 下端
        elif self.rect.bottom > TILE * len(self.current_map):
            return "down"  # 下マップへ遷移
        return None  # 遷移なし
