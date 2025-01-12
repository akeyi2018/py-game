import pygame as pg 
from settings import * 

class Util:
    pass

# ボタンのクラス
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (0, 0, 200)
        self.hover_color = (200, 0, 0)
        self.font = pg.font.Font("../battle/Meiryo.ttf", 24)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.current_color = self.color  # 現在の色

    def draw(self, screen):
        
        # マウスがホバーしている場合の色を変更
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
            
        pg.draw.rect(screen, self.current_color, self.rect, border_radius=5)
        screen.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
class TextSprite(pg.sprite.Sprite):
    def __init__(self, text, font, fore_color, bg_color, x, y, all_sprites):
        super().__init__()
        self.text = text
        self.font = font
        self.color = fore_color
        self.bg_color = bg_color
        # self.image = self.font.render(self.text, True, self.color, self.bg_color)
        self.image = self.font.render(self.text, True, self.color)
        self.surface = self.image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.alpha = 0
        self.all_sprites = all_sprites
        self.all_sprites.add(self)

    def update_message(self, screen, message):
        self.screen = screen
        self.text = message
        self.image = self.font.render(self.text, True, self.color)
        self.surface = self.image

    def draw(self, screen):
        self.screen = screen
        self.screen.blit(self.surface, self.rect.topleft)

class TextAnimation(pg.sprite.Sprite):
    def __init__(self, font, fore_color, bg_color, x, y, screen):
        super().__init__()
        self.font = font
        self.color = fore_color
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.screen = screen
        
        # アニメーション用の変数
        self.current_text = ''  # 現在表示されている文字列
        self.full_text = ''  # アニメーションで表示するテキスト
        self.animation_timer = 0  # アニメーション用のタイマー
        self.fixed_texts = []  # 表示済みの固定テキスト
        self.animation_complete = False  # アニメーション完了フラグ
        self.is_updating = False  # アニメーションが進行中かどうかを示すフラグ
        self.ready_to_finalize = False  # finalize_animationを呼び出す準備ができたかのフラグ
        self.pending_addition = None  # 次に追加する文字列

    def start_animation(self, string):
        """アニメーションを開始"""
        # print(f"Starting animation with text: {string}")  # デバッグ用メッセージ
        self.current_text = ''  # アニメーションの現在テキストを初期化
        self.full_text = string  # アニメーション対象のフルテキスト
        self.animation_complete = False  # アニメーション完了フラグをリセット
        self.is_updating = True  # アニメーションが進行中とする
        self.ready_to_finalize = False  # finalize_animationの準備ができていない

    def update(self, delta_time):
        """アニメーション処理"""
        if self.animation_complete and not self.ready_to_finalize:
            return  # アニメーション完了時、finalizeが準備できていなければ処理しない

        if self.is_updating:  # アニメーション中であれば、テキストを更新
            self.animation_timer += delta_time
            if self.animation_timer >= 2:  # 30msごとに1文字追加
                if len(self.current_text) < len(self.full_text):
                    self.current_text += self.full_text[len(self.current_text)]  # 次の1文字を追加
                else:
                    self.animation_complete = True  # アニメーションが完了
                    self.is_updating = False  # アニメーション更新を停止
                    self.ready_to_finalize = True  # finalize_animationを呼べる状態に
                self.animation_timer = 0  # タイマーをリセット

    def draw(self):
        """現在の状態を描画"""
        # アニメーション中のテキストを描画（アニメーション中だけ）
        if not self.animation_complete:
            text_surface = self.font.render(self.current_text, True, self.color)
            self.screen.blit(text_surface, (self.x, self.y))

    def finalize_animation(self):
        """アニメーション終了後、テキストを固定リストに追加"""
        if self.ready_to_finalize:  # finalize準備ができていれば実行
            self.animation_complete = False  # 次のアニメーション用にリセット
            self.ready_to_finalize = False  # finalize準備をリセット
        return None

    def start_animation(self, string):
        """アニメーションを開始"""
        self.current_text = ''  # アニメーションの現在テキストを初期化
        self.full_text = string  # アニメーション対象のフルテキスト
        # print(self.full_text)
        self.animation_complete = False  # アニメーション完了フラグをリセット
        self.is_updating = True  # アニメーションが進行中とする
        self.ready_to_finalize = False  # finalize_animationの準備ができていない

    def finalize_animation(self):
        """アニメーション終了後、テキストを固定リストに追加"""
        if self.ready_to_finalize:  # finalize準備ができていれば実行
            self.animation_complete = False  # 次のアニメーション用にリセット
            self.ready_to_finalize = False  # finalize準備をリセット
            # return self.full_text  # 完了した文字列を返す
        return None


