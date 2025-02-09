import pygame
import sys
from pygame.locals import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 500

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font("../battle/Meiryo.ttf", 36)

# 背景用のサーフェス
background_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
background_surface.fill(WHITE)

def display_text():
    """ 先に表示する固定テキスト """
    text = 'first test....................'
    y_position = 10  # 初期のy座標位置

    # テキストを背景サーフェスに描画
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (0, y_position)
    background_surface.blit(text_surface, text_rect.topleft)

def display_text_animation(string):
    """ アニメーションでテキストを1文字ずつ表示 """
    text = ''
    y_position = 50  # アニメーションテキストの初期y座標

    for i in range(len(string)):
        char = string[i]

        # 画面を背景サーフェスで塗りつぶす（固定テキストを維持）
        DISPLAYSURF.blit(background_surface, (0, 0))

        # 1文字ずつ追加して描画
        text += char
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (0, y_position)
        DISPLAYSURF.blit(text_surface, text_rect.topleft)

        pygame.display.update()
        pygame.time.wait(30)

def main():
    # 背景に固定テキストを描画
    display_text()

    # メッセージを順番に表示
    display_text_animation('10ダメージを与えました。敵を倒しました。\n10ダメージを与えました。反撃を受けました\n1000ダメージを与えました。敵を倒しました。')

    # イベントループ
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()
