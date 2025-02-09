import pygame
import sys

# 初期設定
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# レイヤー定義
BACKGROUND_LAYER = 0
BLOCK_LAYER = 1
ENEMY_LAYER = 2
NPC_LAYER = 3
PLAYER_LAYER = 4

# 色の定義
COLORS = {
    BACKGROUND_LAYER: (135, 206, 235),  # 空色
    BLOCK_LAYER: (139, 69, 19),         # 茶色
    ENEMY_LAYER: (255, 0, 0),           # 赤
    NPC_LAYER: (0, 255, 0),             # 緑
    PLAYER_LAYER: (0, 0, 255)           # 青
}

# スプライトクラスの定義
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, color, pos, size, *groups, layer=0):
        super().__init__(*groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self._layer = layer  # レイヤーを設定

# スプライトグループの作成
all_sprites = pygame.sprite.LayeredUpdates()

# 各スプライトの作成とグループへの追加
background = GameSprite(COLORS[BACKGROUND_LAYER], (0, 0), (800, 600), all_sprites, layer=BACKGROUND_LAYER)
block = GameSprite(COLORS[BLOCK_LAYER], (100, 100), (100, 50), all_sprites, layer=BLOCK_LAYER)
enemy = GameSprite(COLORS[ENEMY_LAYER], (200, 150), (50, 50), all_sprites, layer=ENEMY_LAYER)
npc = GameSprite(COLORS[NPC_LAYER], (300, 200), (50, 50), all_sprites, layer=NPC_LAYER)
player = GameSprite(COLORS[PLAYER_LAYER], (400, 300), (50, 50), all_sprites, layer=PLAYER_LAYER)

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 描画
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
