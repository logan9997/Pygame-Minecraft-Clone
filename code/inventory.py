import pygame as pg
import json
import math

from pprint import pprint
from entities import Rect
from config import (
    SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, INVENTORY_WIDTH, INVENTORY_HEIGHT,
    INVENTORY_BOX_SIZE
)

class InventoryItem:

    def __init__(self, colour, width, height, name, qty) -> None:
        self.colour = tuple(colour)
        self.width = width
        self.height = height
        self.name = name
        self.qty = qty


    def draw(self, xpos, ypos):
        pg.draw.rect(SCREEN, self.colour, pg.Rect(
            xpos, ypos, self.width, self.height
        ))


class Inventory(Rect):

    def __init__(self, colour, xpos, ypos, width, height) -> None:
        super().__init__(colour, xpos, ypos, width, height)
        self._save_file = 'inventory.json'
        self.open = False
        self.rows = INVENTORY_HEIGHT // INVENTORY_BOX_SIZE
        self.cols = INVENTORY_WIDTH // INVENTORY_BOX_SIZE

    def load_inventory(self):
        with open(self._save_file, 'r') as inventory:
            self.items = json.loads(inventory.read())['items']
            self.items = [InventoryItem(**item) for item in self.items]
            
            used_rows = math.ceil(len(self.items) / self.cols)
            self.items = [
                self.items[(i-1) * self.cols : i * self.cols] 
                for i in range(1, used_rows+1)
            ]

    def shade_boxes(self):
        for i in range(INVENTORY_HEIGHT // INVENTORY_BOX_SIZE):
            for j in range(INVENTORY_WIDTH // INVENTORY_BOX_SIZE):
                pg.draw.rect(SCREEN, (i * 10, j * 10, j * 10), pg.Rect(
                    (j * INVENTORY_BOX_SIZE) + (SCREEN_WIDTH//2) - (self.width//2), 
                    i * INVENTORY_BOX_SIZE + self.ypos,
                    INVENTORY_BOX_SIZE, 
                    INVENTORY_BOX_SIZE 
                ))

    def display(self):
    
        for i in range(len(self.items)):
            for j in range(len(self.items[i])):
                self.items[i][j].draw(
                    (j * INVENTORY_BOX_SIZE) + self.xpos + (INVENTORY_BOX_SIZE // 2) - (self.items[i][j].width // 2),
                    (i * INVENTORY_BOX_SIZE) + self.ypos + (INVENTORY_BOX_SIZE // 2) - (self.items[i][j].height // 2)
                )

    def select_item(self, mouse_pos:tuple[int]):
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        box_x = (mouse_x // INVENTORY_BOX_SIZE) - ((SCREEN_WIDTH - INVENTORY_WIDTH) // 2) // INVENTORY_BOX_SIZE
        box_y = ((2 * mouse_y) - SCREEN_HEIGHT + INVENTORY_HEIGHT) // (2 * INVENTORY_BOX_SIZE)

        print(box_x, box_y)
