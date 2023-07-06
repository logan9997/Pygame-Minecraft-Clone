import pygame as pg
from config import FONT, SCREEN

class Text():

    def __init__(self, colour:tuple[int], xpos:int, ypos:int, text:str, font_size:int) -> None:
        pg.font.init()
        self.colour = colour
        self.xpos = xpos
        self.ypos = ypos
        self.text = text
        self.font_size = font_size
        self.font = pg.font.SysFont(FONT, font_size)
        self.text_surface = self.font.render(self.text, False, self.colour)

    def blit(self):
        SCREEN.blit(self.text_surface, (self.xpos, self.ypos))

    def update_text(self, text):
        self.text_surface = self.font.render(text, False, self.colour)