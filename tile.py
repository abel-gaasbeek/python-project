import pygame


class Tile:
    width=121
    height=121
    state='unoccupied'

    colours =  {
        0: (160, 160, 160),
        2: (200, 150, 20),
        4: (60, 200, 40)
    }

    def __init__(self, x, y, win, font):
        self.x = x
        self.y = y
        self.win = win
        self.font = font
        pygame.draw.rect(win, self.colours.get(0), (x, y, self.width, self.height) )

    def change_number(self, number):
        pygame.draw.rect(self.win, self.colours.get(number), (self.x, self.y, self.width, self.height))
        wtf = self.font.render(str(number), True, (0, 0, 0))
        self.win.blit(wtf, (self.x, self.y))


#is dit er nog