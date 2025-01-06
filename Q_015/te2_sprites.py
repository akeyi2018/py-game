import pygame as pg

# 初期化
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Text Background Example")

# フォントの設定
font = pg.font.Font(None, 48)

# TextWithBackground クラスをスプライトとして定義
class TextWithBackground(pg.sprite.Sprite):
    def __init__(self, text, font, text_color, x, y):
        super().__init__()
        self.text = text
        self.font = font
        self.text_color = text_color
        self.x = x
        self.y = y
        
        # テキストの Surface と矩形設定
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(topleft=(x, y))
        
        # 背景の矩形設定
        self.text_area_rect = pg.Rect(x - 10, y - 10, self.text_surface.get_width() + 20, self.text_surface.get_height() + 20)
        
        # 透明背景 Surface
        self.transparent_surface = pg.Surface(self.text_area_rect.size, pg.SRCALPHA)
        self.transparent_surface.fill((0, 0, 255, 255))  # 半透明の青色背景
        
        # スプライトの image 属性に透明背景を設定
        self.image = self.transparent_surface
        
        # スプライトの rect 属性を設定
        self.rect = self.text_area_rect

        # デバッグ用に Surface の型を確認
        print("transparent_surface type:", type(self.transparent_surface))  # ここで型確認
        print("text_surface type:", type(self.text_surface))  # ここで型確認
    
    def update(self):
        # ここでは特に何も更新しませんが、必要ならテキストや背景を動的に更新できます
        pass

    def draw(self, screen):
        # # 背景を描画
        # screen.blit(self.image, self.rect.topleft)
        
        # テキストを描画（テキストを背景の上に描画）
        screen.blit(self.text_surface, self.text_rect.topleft)

# スプライトグループの作成
all_sprites = pg.sprite.Group()

# スプライトインスタンスの作成
text_sprite = TextWithBackground("Hello, Pygame!", font, (255, 255, 255), 250, 430)
all_sprites.add(text_sprite)

# ゲームループ
running = True
while running:
    screen.fill((0, 0, 0))  # 背景を黒に設定

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # スプライトグループの更新と描画
    all_sprites.update()  # スプライトの更新
    all_sprites.draw(screen)  # スプライトの描画

    pg.display.flip()

pg.quit()
