import pygame as pg
from settings import *
from os.path import join

from player import Player
from sprites import Sprite

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
        # self.all_sprites = pg.sprite.Group()

        # sprites
        self.player = Player((400,300))
        
        # self.all_sprites.add(self.player.surf)


    def run(self):
        
        # ゲーム速度
        dt = self.clock.tick(FPS) / 1000

        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False


            # update 
            # キャラクター移動更新
            self.player.update(dt)

            # draw
            self.main_screen.fill(BLUE)

            # メイン画面にキャラクターを追加描画する
            self.main_screen.blit(self.player.surf, self.player.rect)
            

            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = main()
    new_game.run()

