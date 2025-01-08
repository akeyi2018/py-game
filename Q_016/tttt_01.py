import pygame as pg

class TextSprite(pg.sprite.Sprite):
    def __init__(self, text, font, color, x, y):
        super().__init__()
        self.text = text
        self.font = font
        self.color = color
        self.image = self.font.render(self.text, True, self.color, (0,0,255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.alpha = 0

    def update_text(self, new_text, alpha):
        """テキストを更新"""
        self.text = new_text
        self.alpha = alpha
        if self.alpha >= 255: self.alpha = 0
        self.image = self.font.render(self.text, True, self.color, (0,0,255))
        self.image.set_alpha(self.alpha)

class game:

    def __init__(self):
        # 使用例
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Text Sprite Example")

        # フォントの設定
        self.font = pg.font.Font(None, 64)
        # テキストスプライトの作成
        self.text_sprite = TextSprite("Hello, Pygame!", self.font, (255, 255, 255), 100, 100)
        self.all_sprites = pg.sprite.Group(self.text_sprite)
        self.ct = 10
        self.li = []

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

        

    def run(self):

        # ゲームループ
        running = True

        dt = self.clock.tick(60) / 1000
        while running:

            # self.screen.fill((50, 50, 50))

            if self.game_stage == 'main':
                self.main(dt)

            elif self.game_stage == 'sub':
                self.sub(dt)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        # テキストを更新
                        self.ct += 1
                        self.li.append(str(self.ct) + 'test')
                        if len(self.li) > 5:
                            del self.li[0]

                        if self.ct % 2 == 0: 
                            self.game_stage = 'sub'
                        else:
                            self.game_stage = 'main'

                        view_message = ['  ' + item for item in self.li]
                        view_message = '\n'.join(view_message)
                        self.text_sprite.update_text(view_message, 128)
                        print(view_message)

            # スプライトグループの描画
            self.all_sprites.draw(self.screen)

            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    new_game = game()
    new_game.run()
