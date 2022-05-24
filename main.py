#2048 in python
import pygame

from tile import Tile

pygame.init()
gamesize=4

boardwidth=500
boardheight=500

win =pygame.display.set_mode((boardwidth, boardheight))
pygame.display.set_caption("2048")
game = 'playing'

width= (boardwidth / gamesize)-4
size=boardwidth / gamesize
height= width


def draw_grid(width, height):
    for row in range(0, 4):
        x = 2 + size * row
        for column in range(0, 4):
            y = 2 + size * column
            Tile(x,y,win)
            # pygame.draw.rect(win, (160, 160, 160), (x, y, width, height))


    pygame.display.update()

while game=='playing':
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game='over'
    draw_grid(width, height)

pygame.quit()
