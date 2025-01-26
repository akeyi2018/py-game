import pygame as pg
from settings import *
from status import PlayerStatus
from utils import TextSprite

class Profile:
    def __init__(self):

        self.status = PlayerStatus()

    def get_player_name(self):
        
        print(self.status.view_status["name"])

    def draw(self):

        pass


if __name__ == '__main__':
    ins = Profile()

    ins.get_player_name()
