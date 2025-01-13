import pygame as pg
import sys

class TextAnimation(pg.sprite.Sprite):
    def __init__(self, font, fore_color, bg_color, x, y, screen):
        super().__init__()
        self.font = font
        self.color = fore_color
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.screen = screen
        
    def draw(self, fixed_texts, counter, speed):
        """現在の状態を描画"""
        self.fixed_texts = fixed_texts
        last_line = len(self.fixed_texts)
        # すでに表示された固定テキストを描画
        for i, text in enumerate(self.fixed_texts):
            if i == last_line -1:
                text_surface = self.font.render(text[0:counter//speed], True, self.color)
                self.screen.blit(text_surface, (self.x, self.y + i * 40))
            else:
                text_surface = self.font.render(text, True, self.color)
                self.screen.blit(text_surface, (self.x, self.y + i * 40))

# 画面設定
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Text Animation Example")
screen.fill(WHITE)

# フォント設定
font = pg.font.Font(None, 36)  # `None`を使うとデフォルトフォントが利用されます
clock = pg.time.Clock()

# TextAnimationクラスのインスタンスを作成
text_animation = TextAnimation(font, BLACK, WHITE, 50, 50, screen)

# 表示用のリスト（アニメーション状態を管理する）
init_list = ["test string 001"]  # (テキスト, アニメーション済みフラグ)
fix_list = []

count = 0
counter = 0

# メインループ
while True:
    
    delta_time = clock.tick(60)  # 毎秒60フレームで更新
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # スペースキーでリストを更新
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:

            # 新しい文字列を作成し、アニメーションを開始
            if count == 0:
                new_string = init_list[0]
            else:
                new_string = f"test string 0{count} test 009"
            count += 1

            # view_string = new_string.split('\n')

            # for s in view_string:
            # print(f"New string to animate: {new_string}")  # ログの表示
            # text_animation.start_animation(new_string)  # 新しい文字列でアニメーション開始
            counter = 0
            fix_list.append(new_string)
            if len(fix_list) > 5:
                del fix_list[0]


    # 背景を白で塗りつぶし
    screen.fill(WHITE)

    if len(fix_list) > 0:

        # print(f"test string {fix_list}")
        
        speed = 2
        if counter <= speed * len(fix_list[-1]):
            counter += 1
        elif counter >= speed * len(fix_list[-1]):
            pass

        # 描画
        text_animation.draw(fix_list, counter, speed)

    # 画面を更新
    pg.display.flip()
