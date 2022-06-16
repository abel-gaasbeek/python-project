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
asking_user = False

font = pygame.font.SysFont('Courier', 45)

width = (board_width / game_size) - 4
size = board_width / game_size
height = width

tiles = [[], [], [], []]


def random_tiles():  # verandert een random lege tile naar 2
    column = random.randint(0, 3)
    row = random.randint(0, 3)
    while tiles[column][row].occupied():
        column = random.randint(0, 3)
        row = random.randint(0, 3)

    tiles[column][row].change_number(2)


def fail_state():  # checkt of er nog bewogen kan worden op het bord
    occupied_board = True
    for column in range(0, 4):
        for row in range(0, 4):
            if occupied_board:
                if not tiles[column][row].occupied():
                    occupied_board = False
                    random_tiles()

    if occupied_board:
        for column in range(0, 4):
            for row in range(0, 4):
                row_under = row + 1
                column_next = column + 1
                if row_under < 4:
                    if tiles[column][row_under].get_number() == tiles[column][row].get_number():
                        occupied_board = False
                if column_next < 4:
                    if tiles[column_next][row].get_number() == tiles[column][row].get_number():
                        occupied_board = False

    return occupied_board


def moving_up_down(column, row, kant, tile_next):  # kan tiles omhoog of omlaag bewegen
    destination = -1
    while -1 < tile_next < 4:
        if not tiles[column][tile_next].occupied():
            destination = tile_next
        else:
            if not tiles[column][tile_next].get_occupied_turn():
                if tiles[column][tile_next].get_number() == tiles[column][row].get_number():
                    tiles[column][tile_next].change_number(tiles[column][row].get_number() * 2)
                    tiles[column][row].change_number(0)
                    tiles[column][tile_next].change_occupied_turn(True)
                    destination = -1
                break
        tile_next = tile_next + kant
    if destination != -1:
        tiles[column][destination].change_number(tiles[column][row].get_number())
        tiles[column][row].change_number(0)


def moving_left_right(column, row, kant, tile_next):  # kan tiles links of rechts bewegen
    destination = -1
    while -1 < tile_next < 4:
        if not tiles[tile_next][row].occupied():
            destination = tile_next
        else:
            if not tiles[tile_next][row].get_occupied_turn():
                if tiles[tile_next][row].get_number() == tiles[column][row].get_number():
                    tiles[tile_next][row].change_number(tiles[column][row].get_number() * 2)
                    tiles[column][row].change_number(0)
                    tiles[tile_next][row].change_occupied_turn(True)
                    destination = -1
                break
        tile_next = tile_next + kant
    if destination != -1:
        tiles[destination][row].change_number(tiles[column][row].get_number())
        tiles[column][row].change_number(0)


def moving(move):  # Kiest welk actie er moet gebeuren en bepaalt de loops die moeten gebeuren
    if move == 'right':
        for row in range(0, 4):
            for column in range(2, -1, -1):
                if tiles[column][row].occupied():
                    kant = 1
                    column_next = column + kant
                    moving_left_right(column, row, kant, column_next)
    if move == 'left':
        for row in range(0, 4):
            for column in range(0, 4):
                if tiles[column][row].occupied():
                    kant = -1
                    column_next = column + kant
                    moving_left_right(column, row, kant, column_next)
    if move == 'up':
        for column in range(0, 4):
            for row in range(0, 4):
                if tiles[column][row].occupied():
                    kant = -1
                    row_next = row + kant
                    moving_up_down(column, row, kant, row_next)
    if move == 'down':
        for column in range(0, 4):
            for row in range(2, -1, -1):
                if tiles[column][row].occupied():
                    kant = 1
                    row_next = row + kant
                    moving_up_down(column, row, kant, row_next)
    for row in range(0, 4):
        for column in range(0, 4):
            tiles[column][row].change_occupied_turn(False)


def draw_grid():
    for row in range(0, 4):
        x = 2 + size * row
        for column in range(0, 4):
            y = 2 + size * column
            tiles[row].append(Tile(x, y, win, font))


def empty_grid():  # maakt de hele grid leeg
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 500, 500))
    for row in range(0, 4):
        for column in range(0, 4):
            tiles[column][row].change_number(0)
    random_tiles()
    random_tiles()


draw_grid()
random_tiles()
random_tiles()

while game == 'playing':
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN or pygame.K_RIGHT or pygame.K_DOWN:
                action = 'nothing'
                if event.key == pygame.K_UP:
                    action = 'up'
                elif event.key == pygame.K_DOWN:
                    action = 'down'
                elif event.key == pygame.K_RIGHT:
                    action = 'right'
                elif event.key == pygame.K_LEFT:
                    action = 'left'

                if action != 'nothing' and not asking_user:
                    moving(action)
                    if fail_state():
                        asking_user = True
                        pygame.draw.rect(win, (60, 60, 70), (45, 45, 410, 410))
                        text = font.render('game over', True, (0, 0, 0))
                        win.blit(text, (125, 102))
                        text = font.render('press N to quit', True, (0, 0, 0))
                        win.blit(text, (50, 200))
                        text = font.render('press Y to', True, (0, 0, 0))
                        win.blit(text, (120, 298))
                        text = font.render('play again', True, (0, 0, 0))
                        win.blit(text, (120, 350))
                elif asking_user:
                    # check gebruiker antwoord
                    if event.key == pygame.K_n:
                        game = 'over'

                    elif event.key == pygame.K_y:
                        asking_user = False
                        empty_grid()
                        # init bord + speel nog een keer

        if event.type == pygame.QUIT:
            game = 'over'

    pygame.display.update()
pygame.quit()
