# 2048 in python
import random

import pygame

from tile import Tile

pygame.init()
game_size = 4

board_width = 500
board_height = 500

win = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("2048")
game = 'playing'

font = pygame.font.SysFont('Courier', 50)

width = (board_width / game_size) - 4
size = board_width / game_size
height = width

tiles = [[], [], [], []]


def random_tiles():
    column = random.randint(0,3)
    row = random.randint(0,3)
    tiles[column][row].change_number(2)


def draw_grid(width, height):
    for row in range(0, 4):
        x = 2 + size * row
        for column in range(0, 4):
            y = 2 + size * column
            tiles[row].append(Tile(x, y, win, font))
            # pygame.draw.rect(win, (160, 160, 160), (x, y, width, height))


draw_grid(width, height)

random_tiles()

while game == 'playing':
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 'over'

    pygame.display.update()

pygame.quit()
