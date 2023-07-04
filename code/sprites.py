import pygame as pg

from config import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from entities import Rect

class Player(Rect):

    def __init__(self, color, xpos, ypos, width, height, speed, health) -> None:
        super().__init__(color, xpos, ypos, width, height)
        self.speed = speed
        self.health = health

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.xpos -= self.speed
        if keys[pg.K_d]:
            self.xpos += self.speed
        if keys[pg.K_w]:
            self.ypos -= self.speed
        if keys[pg.K_s]:
            self.ypos += self.speed