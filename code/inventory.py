import pygame as pg
import json

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

    def load_inventory(self):
        with open(self._save_file, 'r') as inventory:
            self.items = json.loads(inventory.read())['items']

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
        for i, item in enumerate(self.items):
            item = InventoryItem(**item)
            item.draw(
                ((i+1) * INVENTORY_BOX_SIZE) + (SCREEN_WIDTH//2) - self.width//2,
                self.ypos + INVENTORY_BOX_SIZE
            )

    def select_item(self, mouse_pos:tuple[int]):
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        box = (mouse_x // INVENTORY_BOX_SIZE, mouse_y // INVENTORY_BOX_SIZE)

        print(box)

