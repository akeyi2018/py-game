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
        self.text_sprite = TextSprite("Hello, Pygame!", self.font, (255, 255, 255), 100, 100, self.all_sprites)
        # self.all_sprites = pg.sprite.Group(self.text_sprite)
        self.ct = 10
        self.li = [""] * 5

        self.clock = pg.time.Clock()

        self.game_stage = 'main'


    def main(self, dt):
        self.screen.fill((250, 0, 0))
        self.back_ground_img = pg.transform.scale(pg.image.load('../battle/bg.png'), (819, 614))
        self.rect = self.back_ground_img.get_frect()

        self.screen.blit(self.back_ground_img, self.rect)

    def sub(self, dt):
        # self.screen.fill((0, 0, 0))
        self.back_ground_img = pg.transform.scale(pg.image.load('../battle/fortress.png'), (819, 614))
        self.rect = self.back_ground_img.get_frect()

        self.screen.blit(self.back_ground_img, self.rect)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        # テキストを更新
                        self.ct += 1
                        self.li.append(str(self.ct) + 'test')
                        if len(self.li) > 5:
                            del self.li[0]

                        if self.ct % 2 == 1: 
                            self.game_stage = 'sub'
                        else:
                            self.game_stage = 'main'

                        view_message = ['  ' + item for item in self.li]
                        view_message = '\n'.join(view_message)
                        self.text_sprite.update_text(view_message, 128)
                        # print(view_message)

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

            
                

            # スプライトグループの描画
            self.all_sprites.draw(self.screen)

            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    new_game = game()
    new_game.run()
