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
        self.alpha += alpha
        if self.alpha >= 255: self.alpha = 0
        self.image = self.font.render(self.text, True, self.color, (0,0,255))
        self.image.set_alpha(self.alpha)

    def update_color(self, new_color):
        """色を更新"""
        self.color = new_color
        self.image = self.font.render(self.text, True, self.color, (0,0,255))

# 使用例
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Text Sprite Example")

# フォントの設定
font = pg.font.Font(None, 64)

# テキストスプライトの作成
text_sprite = TextSprite("Hello, Pygame!", font, (255, 255, 255), 100, 100)
all_sprites = pg.sprite.Group(text_sprite)
ct = 10000
test_text = 'test_001'
li = []
# ゲームループ
running = True
while running:
    screen.fill((50, 50, 50))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # テキストを更新
                ct /= 10
                # if ct > 100000000 : ct = 5
                li.append(str(ct) + 'test')
                if len(li) > 5:
                    del li[0]

                view_message = ['  ' + item for item in li]
                view_message = '\n'.join(view_message)
                text_sprite.update_text(view_message, 10)
                # text_sprite.update_color((255,0,0))

    # スプライトグループの描画
    all_sprites.draw(screen)

    pg.display.flip()

pg.quit()
