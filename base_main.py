import pygame as pg
from settings import *

class game:
    def __init__(self):
        pg.init()

        # screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # title
        pg.display.set_caption('Game Title')
        # clock
        self.clock = pg.time.Clock()
        self.running = True

    def run(self):
        """ゲームループ"""
        self.clock.tick(30)

        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = game()
    new_game.run()
