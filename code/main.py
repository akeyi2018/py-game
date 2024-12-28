import pygame as pg
from settings import *
from os.path import join

from player import Player
from sprites import BackGround

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
        self.background_group = pg.sprite.Group()
        self.back_ground = BackGround()

        self.player_group = pg.sprite.Group()
        self.player = Player((64,64), self.player_group)
        
        # self.all_sprites.add(self.player.surf)

    def draw_background(self):
        for x, y in self.background_sprites:
            tile_image = pg.image.load('../maps/base_tile.png').convert()
            self.main_screen.blit(tile_image, (x, y))

    def run(self):
        
        # ゲーム速度
        dt = self.clock.tick(FPS) / 1000
        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            # キャラクター移動更新
            self.player.update(dt)

            # draw
            self.main_screen.fill(BLUE)
            
            self.back_ground.draw(self.main_screen)

            self.player_group.draw(self.main_screen)

            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = main()
    new_game.run()

