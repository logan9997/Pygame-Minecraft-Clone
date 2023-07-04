import pygame as pg

from config import (
    SCREEN, BACKGROUND_COLOUR, FPS, SCREEN_WIDTH, SCREEN_HEIGHT,
    INVENTORY_WIDTH, INVENTORY_HEIGHT
)
from sprites import Player
from items import Item
from inventory import Inventory

def main():

    clock = pg.time.Clock()

    player = Player(
        (255, 0, 0),
        xpos=100,
        ypos=200,
        width=40,
        height=50,
        speed=1,
        health=100
    )

    inv = Inventory(
        colour=(20, 20, 20),
        xpos=SCREEN_WIDTH//2 - 300,
        ypos=SCREEN_HEIGHT//2 - 200,
        width=INVENTORY_WIDTH,
        height=INVENTORY_HEIGHT
    )

    inv.load_inventory()

    while True:

        SCREEN.fill(BACKGROUND_COLOUR)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_e]:
                    if inv.open:
                        inv.open = False
                    else:
                        inv.open = True

            if event.type == pg.MOUSEBUTTONDOWN and inv.open:
                mouse_pos = pg.mouse.get_pos()
                inv.select_item(mouse_pos)

        player.draw()
        if not inv.open:
            player.move()

        if inv.open:
            inv.draw()
            inv.display()
            inv.shade_boxes()

        clock.tick(FPS)
        pg.display.update()
        

if __name__ == '__main__':
    pg.init()
    main()