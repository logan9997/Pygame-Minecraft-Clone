import pygame as pg

from entities import Rect

class Item(Rect):

    def __init__(self, color, xpos, ypos, width, height, name, qty) -> None:
        super().__init__(color, xpos, ypos, width, height)
        self.name = name
        self.qty = qty

