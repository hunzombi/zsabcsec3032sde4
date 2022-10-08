from random import randint
import random
import pygame
from math import sqrt


run = True
WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# Making a class
class Circ():
    def __init__(self, rad):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.rad = rad
        self.color = (0, 0, 255)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)


def dist(x1, x2, y1, y2):
    return sqrt(((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))


# The game
def main():
    point = 0
    global run
    player = Circ(50)
    def move():
        player.x = randint(0+player.rad, WIDTH-player.rad)
        player.y = randint(0+player.rad, HEIGHT-player.rad)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if dist(player.x, x, player.y, y) <= player.rad:
                    point += 1
                    player.color = random.choice(["blue", "red", "yellow", "green", "orange", "purple"])
                    pygame.display.set_caption(str(point))
                    move()
        WIN.fill((0, 0, 0))
        player.draw(WIN)
        pygame.display.update()

main()