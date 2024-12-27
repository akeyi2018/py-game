from settings import * 
import pygame as pg

class AllSprites(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.Vector2()

    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WIDTH / 2)
        self.offset.y = -(target_pos[1] - HEIGHT / 2)
        
        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'grd')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'grd')]

        # 背景の描画
        for sprite in ground_sprites:
            self.display_surface.blit(sprite.image, sprite.rect.center + self.offset)

        # スプライトのソートをやるとレイヤーの表示がおかしくなる
        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.center + self.offset)
