import pygame as pg
from config import SCREEN

class Rect():

    def __init__(self, colour, xpos, ypos, width, height) -> None:
        self.colour = colour
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

    def draw(self) -> None:
        pg.draw.rect(SCREEN, self.colour, pg.Rect(
            self.xpos, self.ypos, self.width, self.height
        ))