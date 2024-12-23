import pygame as pg 
from settings import *


class game:
    def __init__(self):
        pg.init()

        # screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

    def intro_screen(self):
        self.screen.fill(BGCOLOR)
        pg.display.flip()

    def run(self):
        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            # 描画の更新
            self.intro_screen()
            self.clock.tick(60)  # フレームレートを設定 (例: 60FPS)

        pg.quit()


if __name__ == "__main__":
    new_game = game()
    new_game.run()
