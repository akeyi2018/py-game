import pygame as pg
from settings import *
from wall import Block
from enemy import Enemy
from enemy_maneger import EntryEnemy
from player import Player
import random

class Map(pg.sprite.Sprite):
    def __init__(self, parent, all_sprites, *groups):
        super().__init__(*groups)

        self.parent = parent

        self.block_images = {
            "B" : "../maps/tree.png",
            "N" : "../maps/town/yh001.png",
        }
        self.name = 'map_01'
        self.current_map = TILE[self.name]

        # 通過不可Sprite
        self.collision_sprites = pg.sprite.Group()

        self.enemy_sprites = pg.sprite.Group()

        self.npc_sprites = pg.sprite.Group()

        self.all_sprites = all_sprites

    def create(self):
        
        # 敵の配置
        self.create_enemy()

        # BlockとPlayerの配置
        for i, row in enumerate(self.current_map):
            for j, column in enumerate(row):
                x = j * TILE_SIZE
                y = i * TILE_SIZE

                if column == 'B':
                    self.block = Block((x,y), self.block_images['B'], self.collision_sprites, self.all_sprites)

                if column == 'N':
                    self.block = Block((x,y), self.block_images['N'], self.npc_sprites, self.all_sprites)

                if column == 'P':
                    self.player = Player(self.parent, (x,y), self.collision_sprites, self.enemy_sprites, self.npc_sprites, self.all_sprites)

        return self.player, self.current_map
    
    def reset(self, save_info):
        
        # BlockとPlayerの配置
        for i, row in enumerate(self.current_map):
            for j, column in enumerate(row):
                x = j * TILE_SIZE
                y = i * TILE_SIZE

                if column == 'B':
                    self.block = Block((x,y), self.block_images['B'], self.collision_sprites, self.all_sprites)
                if column == 'N':
                    self.block = Block((x,y), self.block_images['N'], self.npc_sprites, self.all_sprites)

        print(type(save_info))
        x = save_info["x"] * TILE_SIZE
        y = save_info["y"] * TILE_SIZE
        # playerの配置
        self.player = Player(self.parent, (x,y), self.collision_sprites, self.enemy_sprites, self.npc_sprites, self.all_sprites)

        return self.player, self.current_map
    
    def cal_player_in_tile(self, x, y):
        tile_x = int(x / TILE_SIZE)
        tile_y = int(y / TILE_SIZE)


    def create_enemy(self):
        #生成時作業用ID
        entry = EntryEnemy()

        # 敵の配置
        self.replace_zeros_with_nines()
        for i, row in enumerate(self.grid):
            # print(row)
            for j, column in enumerate(row):
                x = j * TILE_SIZE
                y = i * TILE_SIZE
                if column == 9:
                    # モブ生成
                    mob_info = entry.generate_random_enemy()
                    self.enemy = Enemy((x,y), mob_info, [j,i], self.enemy_sprites, self.all_sprites)

    def cal_player_area(self, max_y, max_x):
        # px 
        px = -1
        py = -1
        for i, row in enumerate(self.current_map):
            for j, column in enumerate(row):
                if column == 'P':
                    px = j
                    py = i
                    break

        # NONエリアの計算
        px_min = max(0, px - NON_ENEMY_AREA)
        px_max = min(max_x - 1, px + NON_ENEMY_AREA)
        py_min = max(0, py - NON_ENEMY_AREA)
        py_max = min(max_y - 1, py + NON_ENEMY_AREA)

        return px_min, px_max, py_min, py_max
        
    def cal_non_enemy_area(self):

        map_data = self.get_base_map()

        # mapデータの最大値を取得する
        max_map_y = len(map_data)
        max_map_x = len(map_data[0])

        # Playerエリアの計算
        px_min, px_max, py_min, py_max = self.cal_player_area(max_map_x, max_map_y)

        # 敵を配置できるエリアの取得
        self.loc_enemy_area = []
        for i, row in enumerate(self.current_map):
            row_area = []
            for j, column in enumerate(row):
                if column == '.':
                    px = j
                    py = i
                    if (px > px_min and py > py_min) and (px < px_max and py < py_max):
                        row_area.append(1)
                    else:
                        row_area.append(0) 
                else:
                    row_area.append(1)
            self.loc_enemy_area.append(row_area)

        return self.loc_enemy_area

    def replace_zeros_with_nines(self):
        """リスト内の0をランダムに選択して指定された数を9に置き換える。"""
        # 0の座標を探す
        self.grid = self.cal_non_enemy_area()

        zero_positions = [(i, j) for i, row in enumerate(self.grid) for j, val in enumerate(row) if val == 0]
        
        # 指定された数だけランダムに選択
        if MAX_ENEMY_NUM > len(zero_positions):
            raise ValueError("0の数より置き換える数が多いです。")
        
        random_positions = random.sample(zero_positions, MAX_ENEMY_NUM)
        
        # 選択された位置を9に置き換える
        for i, j in random_positions:
            self.grid[i][j] = 9

    def get_base_map(self):
        base_map = []
        for i, row in enumerate(self.current_map):
            row_area = []
            for j, column in enumerate(row):
                if column == 'B':
                    row_area.append(1) 
                else:
                    row_area.append(0)
            base_map.append(row_area)

        return base_map