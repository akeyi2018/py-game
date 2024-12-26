import pygame as pg
from settings import *
from player import Player

class game:
    def __init__(self):
        pg.init()

        # screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # title
        pg.display.set_caption(TITLE)
        # clock
        self.clock = pg.time.Clock()
        self.running = True
        # group
        self.all_sprites = pg.sprite.Group()

        # sprites
        self.player = Player((400,300), self.all_sprites)

    def run(self):
        """ゲームループ"""
        dt = self.clock.tick(FPS) / 1000

        while self.running:
            # イベント処理
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.screen.fill('black')
            self.all_sprites.draw(self.screen)

            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    new_game = game()
    new_game.run()
