import pygame as pg

from utils import TextSprite 

class game:

    def __init__(self):
        # 使用例
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Text Sprite Example")

        # フォントの設定
        self.font = pg.font.Font(None, 64)
        # テキストスプライトの作成
        self.all_sprites = pg.sprite.Group()
        self.text_sprite = TextSprite("Hello, Pygame!            ", self.font, (255, 255, 255), 100, 100, self.all_sprites)
        # self.all_sprites = pg.sprite.Group(self.text_sprite)
        self.ct = 10
        self.li = [""] * 5

        self.clock = pg.time.Clock()

        self.game_stage = 'main'

        self.stop = True

    def set_message(self, new_message):
        self.li.append(new_message)
        if len(self.li) > 5: del self.li[0]
        view_message = ['  ' + item for item in self.li]
        return '\n'.join(view_message)

    def main(self, dt):

        if self.stop:

            # self.screen.fill((0, 0, 0))
            
            # self.back_ground_img = pg.transform.scale(pg.image.load('../battle/bg.png'), (819, 614))
            # self.rect = self.back_ground_img.get_frect()
            # self.screen.blit(self.back_ground_img, self.rect)

            v = self.set_message(str(self.ct) + self.game_stage)
            self.text_sprite.update_message(self.screen, v)

            self.all_sprites.draw(self.screen)
            self.stop = False

        # ts = pg.Surface((400,400), pg.SRCALPHA)
        # ts.fill((0, 0, 255, 128)) 
        # self.screen.blit(ts, [0,0,600,800])
         # スプライトグループの描画
        

    def sub(self, dt):

        if self.stop:
            self.screen.fill((0, 0, 0))
            self.back_ground_img = pg.transform.scale(pg.image.load('../battle/fortress.png'), (819, 614))
            self.rect = self.back_ground_img.get_frect()

            self.screen.blit(self.back_ground_img, self.rect)

            v = self.set_message(str(self.ct) + self.game_stage)
            self.text_sprite.update_message(self.screen, v)
            # スプライトグループの描画
            self.all_sprites.draw(self.screen)
            self.stop = False
        

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        # テキストを更新
                        self.ct += 1
                        if self.ct % 2 == 1: 
                            self.game_stage = 'main'
                            if self.stop == False: self.stop = True

                        else:
                            self.game_stage = 'sub'
                            if self.stop == False: self.stop = True

    def run(self):

        # ゲームループ
        self.running = True

        dt = self.clock.tick(60) / 1000
        while self.running:

            # self.screen.fill((50, 50, 50))

            self.events()

            if self.game_stage == 'main':
                self.main(dt)

            elif self.game_stage == 'sub':
                self.sub(dt)

           

            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    new_game = game()
    new_game.run()
