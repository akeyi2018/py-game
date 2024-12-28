import pygame as pg
from settings import *
from os.path import join


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


    def run(self):
        
        # ゲーム速度
        dt = self.clock.tick(FPS) / 1000

        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            # update

            # draw
            self.main_screen.fill(BLUE)

            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = main()
    new_game.run()

