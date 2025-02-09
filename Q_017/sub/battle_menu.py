import pygame as pg
from sub.settings import *
from utils import Button

class BattleMenu:
    def __init__(self, actions):
        self.display_surface = pg.display.get_surface()
        
        self.px = 30
        self.main_pos_y = [30, 80, 530]
        self.sub_pos_y = [30, 80, 130, 180] 

        self.buttons = {
            "main": self.create_buttons(actions['main'], self.px, self.main_pos_y),
            "sub": self.create_buttons(actions['sub'], self.px, self.sub_pos_y),
        }
        
        self.current_command = "main"

    def create_buttons(self, actions, x, y_positons):
        btn_width, btn_height = 100, 40
        return [
            Button(x, y_positons[i], btn_width, btn_height, name, action)
            for i, (name, action) in enumerate(actions)
        ]

    def show_main_commands(self):
        self.current_command = 'main'
        # print(f"Current Command: {self.current_command}")  # デバッグ用
        self.draw_buttons(self.layout)

    def show_sub_commands(self):
        self.current_command = 'sub'
        # print(f"Current Command: {self.current_command}")  # デバッグ用
        self.draw_buttons(self.layout)

    # 描画
    def draw_buttons(self, layout):
        # print(f"Drawing buttons for: {self.current_command}")  # デバッグ用
        self.layout = layout
        # メニューの背景を再描画（前回のボタンをクリア）
        layout.draw_menu_background()

        for button in self.buttons[self.current_command]:
            button.draw(self.display_surface)

    def handle_mouse_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # クリックした位置を取得
            for button in self.buttons[self.current_command]:
                if button.check_click(mouse_pos):  # ボタンがクリックされたか判定
                    button.action()  # ボタンに設定された関数を呼び出し
                    if button.text == 'cancel':
                        return False
                    else:
                        return True
        return False