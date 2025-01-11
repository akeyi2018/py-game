import pygame as pg
import sys

class TextAnimation(pg.sprite.Sprite):
    def __init__(self, font, fore_color, bg_color, x, y, all_sprites, screen):
        super().__init__()
        self.font = font
        self.color = fore_color
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.screen = screen
        self.all_sprites = all_sprites
        self.all_sprites.add(self)
        
        # アニメーション用の変数
        self.current_text = ''  # 現在表示されている文字列（1文字ずつ表示）
        self.full_text = ''  # アニメーションで表示するテキスト
        self.animation_timer = 0  # アニメーションの経過時間
        self.text_position = (x, y)
        self.fixed_text_surface = None  # 固定テキストを保存
        self.fixed_text_position = None
        self.animation_complete = False  # アニメーション完了フラグ

    def set_fixed_text(self, text):
        """固定テキストを設定し描画"""
        self.fixed_text_surface = self.font.render(text, True, self.color)
        self.fixed_text_position = (self.x, self.y)  # 固定テキストの描画位置
        self.screen.blit(self.fixed_text_surface, self.fixed_text_position)
        pg.display.update()

    def start_animation(self, string):
        """アニメーションを開始"""
        self.current_text = ''  # アニメーション用の現在のテキストを初期化
        self.full_text = string  # アニメーション対象のフルテキスト
        self.animation_complete = False  # フラグをリセット

    def update(self, delta_time):
        """アニメーション処理"""
        if self.animation_complete:
            # アニメーションが完了している場合は、最後の状態を保持
            self.image = self.font.render(self.current_text, True, self.color)
            self.screen.blit(self.image, (self.x, self.y + 40))  # 完了後も表示を維持
            return

        self.animation_timer += delta_time
        if self.animation_timer >= 30:  # 30msごとに1文字追加
            if len(self.current_text) < len(self.full_text):
                self.current_text += self.full_text[len(self.current_text)]  # 1文字追加
                self.image = self.font.render(self.current_text, True, self.color)
                self.screen.blit(self.fixed_text_surface, self.fixed_text_position)  # 固定テキストを再描画
                self.screen.blit(self.image, (self.x, self.y + 40))  # アニメーションテキストを描画
                pg.display.update()
            else:
                self.animation_complete = True  # アニメーションが完了
            self.animation_timer = 0  # タイマーをリセット

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Text Animation Example")
font = pg.font.Font("../battle/Meiryo.ttf", 24)
all_sprites = pg.sprite.Group()
clock = pg.time.Clock()

# テキストアニメーションクラスの初期化
text_animation = TextAnimation(font, BLACK, WHITE, 50, 50, all_sprites, screen)

# 固定テキストの設定
# text_animation.set_fixed_text("This is fixed text!")

# アニメーションテキストの開始
text_animation.start_animation("This text will appear character by character.")
# text_animation.set_fixed_text("This is fixed text!")
# メインループ
while True:
    delta_time = clock.tick(10)  # 毎秒60フレームで更新
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # 背景を白で塗りつぶして固定テキストを再描画
    screen.fill(WHITE)
    text_animation.set_fixed_text("This is fixed text!")
    # text_animation.start_animation("This text will appear character by character.")

    # アニメーションの更新
    text_animation.update(delta_time)

    # アニメーションが終了した後も表示を維持
    # if text_animation.animation_complete:
    #     print("Animation completed!")  # アニメーションが終了したらメッセージを表示（他の処理に置き換え可能）

    pg.display.flip()
