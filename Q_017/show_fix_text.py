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
            if self.animation_timer >= 100:  # 30msごとに1文字追加
                if len(self.current_text) < len(self.full_text):
                    self.current_text += self.full_text[len(self.current_text)]  # 次の1文字を追加
                else:
                    self.animation_complete = True  # アニメーションが完了
                    self.is_updating = False  # アニメーション更新を停止
                    self.ready_to_finalize = True  # finalize_animationを呼べる状態に
                self.animation_timer = 0  # タイマーをリセット

    def draw(self, fixed_texts):
        """現在の状態を描画"""
        # self.fixed_texts = fixed_texts
        # v = fixed_texts[:-1]
        # # すでに表示された固定テキストを描画
        # for i, text in enumerate(v):
        #     text_surface = self.font.render(text, True, self.color)
        #     self.screen.blit(text_surface, (self.x, self.y + i * 40)) 
        # アニメーション中のテキストを描画（アニメーション中だけ）
        if not self.animation_complete:
            # print('NNNNN')
            text_surface = self.font.render(self.current_text, True, self.color)
            # if len(fixed_texts) > 0:
            #     pos = len(fixed_texts) -1
            # else:
            #     pos = 0
            self.screen.blit(text_surface, (self.x, self.y + 40))

    def finalize_animation(self):
        """アニメーション終了後、テキストを固定リストに追加"""
        if self.ready_to_finalize:  # finalize準備ができていれば実行
            print(f"Finalizing animation with text: {self.full_text}")  # アニメーション終了時に表示する文字列
            # self.fixed_texts.append((self.full_text, True))  # アニメーション済みとして追加
            print(f"Finalizing animation with text: {self.fixed_texts}")
            self.animation_complete = False  # 次のアニメーション用にリセット
            self.ready_to_finalize = False  # finalize準備をリセット
            # return self.full_text  # 完了した文字列を返す
        return None

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
            text_animation.start_animation(new_string)  # 新しい文字列でアニメーション開始
              
            fix_list.append(new_string)
            if len(fix_list) > 5:
                del fix_list[0]
            # print(f"test string {fix_list}")  

    # 背景を白で塗りつぶし
    screen.fill(WHITE)

    # アニメーションを更新
    text_animation.update(delta_time)

    # アニメーションが終了したら現在の文字列を固定
    if text_animation.animation_complete:
        text_animation.finalize_animation()

    # 描画
    text_animation.draw(fix_list)

    # 画面を更新
    pg.display.flip()
