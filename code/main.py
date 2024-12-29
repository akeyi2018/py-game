import pygame as pg
from settings import *
from os.path import join
from groups import AllSprites
from player import Player
from sprites import Sprite, CollisionSprite
from enemy import Enemy

class main:
    def __init__(self):
        # pygame初期化
        pg.init()

        # ゲームメイン画面
        self.main_screen = pg.display.set_mode((MAIN_WIDTH, MAIN_HEIGHT))

        # title
        pg.display.set_caption(TITLE)

        # clock
        self.clock = pg.time.Clock()

        # flag
        self.running = True

        # group
        # すべてのスプライト
        self.all_sprites = AllSprites()

        # 衝突用スプライトグループ
        self.collision_sprites = pg.sprite.Group()

        # 敵スプライトグループ
        self.enemy_sprites = pg.sprite.Group()

        # レイヤーごとにスプライトを配置する(Mapロード)
        self.current_map_name = 'map_01'
        self.current_map = TILE_MAP[self.current_map_name]

        # self.player_start_pos = None
        self.set_sprites_layer()

        # self.debug_sprite_groups()

    def set_sprites_layer(self, start_pos=None):
        # スプライトグループをクリア
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.enemy_sprites.empty()

        self.grass = pg.image.load(join('../maps',MAP_GRD[self.current_map_name]["."]))
        self.block = pg.image.load(join('../maps','tree.png')).convert_alpha()
        for i, row in enumerate(self.current_map):
            for j, column in enumerate(row):
                x = j * TILE
                y = i * TILE
                # バックグランド
                Sprite((x,y), self.grass, self.all_sprites)
                if column == 'B':
                    CollisionSprite((x,y), self.block, self.all_sprites, self.collision_sprites)
                elif column == 'P':
                    if start_pos == None:
                        self.player = Player(
                            (x,y),
                            self.current_map, 
                            self.all_sprites, 
                            self.collision_sprites, 
                            self.enemy_sprites)
                    else:
                        self.player = Player(
                            start_pos,
                            self.current_map, 
                            self.all_sprites, 
                            self.collision_sprites, 
                            self.enemy_sprites)
                elif column == 'E':
                    self.mob = Enemy((x,y), column, self.all_sprites, self.enemy_sprites)
                elif column == 'F':
                    self.mob = Enemy((x,y), column, self.all_sprites, self.enemy_sprites)
                elif column == 'G':
                    self.mob = Enemy((x,y), column, self.all_sprites, self.enemy_sprites)

    def run(self):
        
        # ゲーム速度
        dt = self.clock.tick(FPS) / 1000
        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)
            self.transition = self.player.check_map_transition()

            if self.transition:
                # print(self.transition)
                print()
                self.after_transition_name, player_start_pos = MAP_CONNECTIONS[self.current_map_name][self.transition]
                self.current_map = TILE_MAP[self.after_transition_name]
                self.current_map_name = self.after_transition_name
                self.set_sprites_layer(player_start_pos)

            # draw
            self.main_screen.fill(BLUE)
            self.all_sprites.draw(self.player.rect.center)

            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = main()
    new_game.run()

