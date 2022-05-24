import pygame


class Tile:
    width=121
    height=121
    state='unoccupied'


    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        pygame.draw.rect(win, (160, 160, 160), (x, y, self.width, self.height) )

#is dit er nog