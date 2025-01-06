import pygame as pg

# Pygame 初期化
pg.init()

# ボタンのクラス
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        # マウスがホバーしている場合の色を変更
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, self.hover_color, self.rect)
        else:
            pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# ゲームクラス
class Game:
    def __init__(self):
        self.display_surface = pg.display.set_mode((800, 600))
        pg.display.set_caption("Main and Sub Commands")
        
        # メインコマンドのボタン
        self.main_buttons = [
            Button(30, 30, 100, 40, "攻撃", self.show_sub_commands),
            Button(30, 80, 100, 40, "魔法", self.magic),
            Button(30, 130, 100, 40, "逃げる", self.escape),
        ]

        # サブコマンドのボタン
        self.sub_buttons = [
            Button(30, 30, 100, 40, "ホイミ", self.hoimi),
            Button(30, 80, 100, 40, "メラ", self.mera),
            Button(30, 130, 100, 40, "戻る", self.show_main_commands),
        ]

        # 現在表示するボタンセットを設定（初期状態はメインコマンド）
        self.current_buttons = self.main_buttons

    # メインコマンドを表示
    def show_main_commands(self):
        self.current_buttons = self.main_buttons

    # サブコマンドを表示
    def show_sub_commands(self):
        self.current_buttons = self.sub_buttons

    # 描画
    def draw_buttons(self):
        for button in self.current_buttons:
            button.draw(self.display_surface)

    # マウスイベント処理
    def handle_mouse_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for button in self.current_buttons:
                if button.check_click(mouse_pos):
                    button.action()  # ボタンのアクションを実行

    # アクション関数
    def attack(self):
        print("攻撃!")

    def magic(self):
        print("魔法!")

    def escape(self):
        print("逃げる!")

    def hoimi(self):
        print("ホイミ!")

    def mera(self):
        print("メラ!")

# ゲームループ
game = Game()
running = True
while running:
    game.display_surface.fill((0, 0, 0))  # 背景を黒でクリア

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        game.handle_mouse_event(event)

    # ボタンを描画
    game.draw_buttons()

    pg.display.flip()

pg.quit()
