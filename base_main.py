import pygame as pg
from settings import *
from player import Player
from random import randint
from sprites import CollisionSprite


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
        self.collision_sprites = pg.sprite.Group()

        # sprites
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
        for i in range(6):
            x,y = randint(0, WIDTH), randint(0, HEIGHT)
            w,h = randint(60,100),randint(50,100)
            CollisionSprite((x,y), (w,h), self.all_sprites, self.collision_sprites)

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
