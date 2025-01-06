import pygame as pg

# Pygameの初期化
pg.init()

# 画面のサイズ
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

# フォント設定
font = pg.font.SysFont("yumincho", 36)

# ボタンのクラス
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (0, 0, 255)  # ボタンの色
        self.text_surface = font.render(self.text, True, (255, 255, 255))  # ボタンのテキスト

    def draw(self, surface):
        # ボタンを描画
        pg.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, (self.rect.x + (self.rect.width - self.text_surface.get_width()) // 2,
                                        self.rect.y + (self.rect.height - self.text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        # マウスクリック時にボタンが押されたかを判定
        return self.rect.collidepoint(pos)


# アクションを定義する関数
def attack_action():
    print("攻撃!")

def magic_action():
    print("魔法!")

def escape_action():
    print("逃げる!")

# ゲームのメインループ
def game_loop():
    running = True
    buttons = [
        Button(100, 400, 200, 60, "攻撃", attack_action),
        Button(300, 400, 200, 60, "魔法", magic_action),
        Button(500, 400, 200, 60, "逃げる", escape_action)
    ]
    
    while running:
        screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし

        # イベントの処理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                # クリックされた位置を取得
                mouse_pos = pg.mouse.get_pos()
                # 各ボタンをクリックしたか判定
                for button in buttons:
                    if button.is_clicked(mouse_pos):
                        button.action()  # ボタンに対応するアクションを実行

        # ボタンを描画
        for button in buttons:
            button.draw(screen)

        # 画面更新
        pg.display.flip()

# ゲームループを実行
game_loop()

# Pygameの終了
pg.quit()
