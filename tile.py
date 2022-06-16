import pygame

import tile


class Tile:
    width = 121
    height = 121
    number = 0
    occupied_turn = False

    colours = {
        0: (160, 160, 160),
        2: (240, 240, 40),
        4: (70, 200, 70),
        8: (255, 83, 0),
        16: 'red',
        32: 'blue',
        64: 'purple',
        128: (70, 150, 240),
        256: (100, 250, 0),
        512: 'orange',
        1024: (0, 255, 255),
        2048: (255, 255, 255),
        4096: (255, 200, 190),
        8192: (190, 160, 255)
    }

    text_offset = {
        0: 42,
        2: 48,
        4: 42,
        8: 42,
        16: 32,
        32: 32,
        64: 32,
        128: 22,
        256: 22,
        512: 22,
        1024: 10,
        2048: 10,
        4096: 10,
        8192: 10
    }

    def occupied(self):  # kijkt of de tile een nummer heeft
        return self.number > 0

    def __init__(self, x, y, win, font):
        self.x = x
        self.y = y
        self.win = win
        self.font = font
        pygame.draw.rect(win, self.colours.get(0), (x, y, self.width, self.height))

    def get_occupied_turn(self):  # geeft de occupied van deze turn
        return self.occupied_turn

    def change_occupied_turn(self, value):  # verandert de van occupied deze turn
        self.occupied_turn = value

    def get_number(self):  # geeft het nummer van een tile
        return self.number

    def change_number(self, number):  # verandert het nummer van een tile
        self.number = number
        pygame.draw.rect(self.win, self.colours.get(number), (self.x, self.y, self.width, self.height))
        if number != 0:
            text = self.font.render(str(number), True, (0, 0, 0))
            self.win.blit(text, ((self.x) + self.text_offset.get(number), (self.y) + 36))
