import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, mob_info, mob_pos, *groups):
        super().__init__(*groups)

        self.base_path = '../enemy/img/'
        self.mob_img_path = self.base_path + mob_info['IMG']

        self.mob_info = mob_info
        # 論理配置
        self.mob_pos = mob_pos
        # name
        self.name = self.mob_info['name']
        self.original = pg.image.load(self.mob_img_path).convert_alpha()
        self.battle_surface = pg.transform.scale(self.original, (150, 150))
        self.surface = pg.transform.scale(self.original, (64, 64))
        # 画面での位置
        self.pos = pos
        # rect
        self.rect = self.surface.get_frect(topleft=pos)
        self.enemy_sprites_type = True
