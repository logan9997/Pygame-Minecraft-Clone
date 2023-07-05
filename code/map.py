from config import MAP_BLOCK_SIZE, MAP_DIMENSIONS, SCREEN
import pygame as pg

class Map:

    def __init__(self) -> None:
        self.map_width = MAP_DIMENSIONS[0]
        self.map_height = MAP_DIMENSIONS[1]
        self._map_file = 'map.txt'

    def load_map(self):
        with open(self._map_file, 'r') as file:
            self._map = file.readlines()

        
    def render(self):
        for i in range(self.map_height-1):
            for j in range(self.map_width-1):
                square = self._map[i][j]
                if square == '0':
                    colour = (10, 255, 40)
                else:
                    colour = (10, 40, 240)
                pg.draw.rect(SCREEN, colour, pg.Rect(
                    i * MAP_BLOCK_SIZE,
                    j * MAP_BLOCK_SIZE,
                    MAP_BLOCK_SIZE,
                    MAP_BLOCK_SIZE
                ))
    
# a = Map().generate_map()
# print(a)