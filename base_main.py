import pygame as pg
from settings import *
from player import Player
from random import randint
from sprites import CollisionSprite, Sprite
from groups import AllSprites
from pytmx.util_pygame import load_pygame
from os.path import join
from os import walk

class game:
    def __init__(self):
        pg.init()

        # screen
        self.display_surface = pg.display.set_mode((WIDTH, HEIGHT))
        # title
        pg.display.set_caption(TITLE)
        # clock
        self.clock = pg.time.Clock()
        self.running = True
        # group
        self.all_sprites = AllSprites()
        self.collision_sprites = pg.sprite.Group()

        self.setup()

        # sprites
        # self.player = Player((400,300), self.all_sprites, self.collision_sprites)

   
    
    def setup(self):
        map = load_pygame(join('./maps','world.tmx'))
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE, y * TILE), image, self.all_sprites)

        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, self.all_sprites, self.collision_sprites)

        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x, obj.y), pg.Surface((obj.width, obj.height)), self.collision_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x,obj.y), self.all_sprites, self.collision_sprites)


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
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)

            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = game()
    new_game.run()
