import pygame as pg
from settings import *
from player_data import *
from wall import Block
from enemy import Enemy
from enemy_maneger import EntryEnemy
from player import Player
from utils import TextSprite
from status import PlayerStatus
import random

class Map(pg.sprite.Sprite):
    def __init__(self, parent, all_sprites, *groups):
        super().__init__(*groups)

        self.parent = parent

        self.block_images = {
            "B" : "../maps/tree.png",
            "N" : "../maps/town/yh001.png",
            "G" : "../maps/grass.png"
        }
        self.name = 'map_01'
        self.current_map = TILE[self.name]

        # 通過不可Sprite
        self.collision_sprites = pg.sprite.Group()

        self.enemy_sprites = self.parent.enemy_sprites

        self.npc_sprites = pg.sprite.Group()

        self.all_sprites = all_sprites

    def create(self):
        
        # 下地処理
        self.draw_grass()

        # BlockとNPCの配置
        self.draw_block()

        x,y = self.get_player_pos()

        self.player = Player(self.parent, (x,y), self.collision_sprites, self.enemy_sprites, self.npc_sprites, self.all_sprites)

        self.draw_status()

        return self.player, self.current_map, self.bar
    
    def get_player_pos(self):

        for i, row in enumerate(self.current_map):
            for j, column in enumerate(row):
                x = j * TILE_SIZE
                y = i * TILE_SIZE

                if column == 'P':
                    return x , y

    def reset(self, save_info):

        # 下地処理
        self.draw_grass()
        
        # BlockとNPCの配置
        self.draw_block()

        x = save_info["x"] * TILE_SIZE
        y = save_info["y"] * TILE_SIZE
        # playerの配置
        self.player = Player(self.parent, (x,y), self.collision_sprites, self.enemy_sprites, self.npc_sprites, self.all_sprites)

        self.draw_status()

        return self.player, self.current_map, self.bar
    
    def draw_status(self):

        # 主人公ステータス表示
        character_name = TextSprite(
            NAME,
            20,
            (255,255,255),
            (0,0,0),
            100,100, self.all_sprites
        )
        self.bar = PlayerStatus(
            self.all_sprites
        )
        # self.bar.draw_bar_of_main(100,100+30, self.parent.display_surface)
    
    def draw_grass(self):

        for i, row in enumerate(self.current_map):
            for j, column in enumerate(row):
                x = j * TILE_SIZE
                y = i * TILE_SIZE

                if column != '':
                    self.block = Block((x,y), self.block_images['G'], self.all_sprites)

    def draw_block(self):
        # BlockとPlayerの配置
        for i, row in enumerate(self.current_map):
            for j, column in enumerate(row):
                x = j * TILE_SIZE
                y = i * TILE_SIZE

                if column == 'B':
                    self.block = Block((x,y), self.block_images['B'], self.collision_sprites, self.all_sprites)

                if column == 'N':
                    self.block = Block((x,y), self.block_images['N'], self.npc_sprites, self.all_sprites)
