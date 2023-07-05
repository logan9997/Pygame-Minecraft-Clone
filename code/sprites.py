import pygame as pg

from config import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from entities import Rect
from utils import distance_between_two_points

class Sprite(Rect):

    def __init__(self, colour, xpos, ypos, width, height, speed, health) -> None:
        super().__init__(colour, xpos, ypos, width, height)
        self.speed = speed
        self.health = health

    def boundaries(self):
        if self.xpos >= SCREEN_WIDTH - (self.width):
            self.xpos = SCREEN_WIDTH - (self.width)
        elif self.xpos <= 0:
            self.xpos = 0 
        
        if self.ypos >= SCREEN_HEIGHT - self.height:
            self.ypos = SCREEN_HEIGHT - self.height
        elif self.ypos <= 0:
            self.ypos = 0 

class Player(Sprite):

    def __init__(self, color, xpos, ypos, width, height, speed, health) -> None:
        super().__init__(color, xpos, ypos, width, height, speed, health)

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
    
        self.boundaries()


class Enemy(Sprite):

    def __init__(self, colour, xpos, ypos, width, height, speed, health, view_radius) -> None:
        super().__init__(colour, xpos, ypos, width, height, speed, health)
        self.view_radius = view_radius

    def move(self, player:Player) -> None:
        distance = distance_between_two_points(
            player.xpos, self.xpos, player.ypos, self.ypos
        )
        if distance <= self.view_radius:
            if self.xpos < player.xpos:
                self.xpos += self.speed
            elif self.xpos > player.xpos:
                self.xpos -= self.speed

            if self.ypos < player.ypos:
                self.ypos += self.speed
            elif self.ypos > player.ypos:
                self.ypos -= self.speed      