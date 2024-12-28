import pygame as pg
from settings import *
from os.path import join
from groups import AllSprites
from player import Player
from sprites import Sprite, CollisionSprite

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

        # レイヤーごとにスプライトを配置する
        self.set_sprites_layer()

    def set_sprites_layer(self):
        self.grass = pg.image.load(join('../maps','grass.png'))
        self.block = pg.image.load(join('../maps','tree.png')).convert_alpha()
        for i, row in enumerate(TILE_MAP):
            for j, column in enumerate(row):
                x = j * TILE
                y = i * TILE
                # バックグランド
                Sprite((x,y), self.grass, self.all_sprites)
                if column == 'B':
                    CollisionSprite((x,y), self.block, self.all_sprites, self.collision_sprites)
                elif column == 'P':
                    self.player = Player((x,y), self.all_sprites, self.collision_sprites)

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

            # draw
            self.main_screen.fill(BLUE)
            self.all_sprites.draw(self.player.rect.center)

            pg.display.update()

        pg.quit()

if __name__ == "__main__":
    new_game = main()
    new_game.run()

