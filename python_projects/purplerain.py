import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bg_color = pygame.color.Color(33, 33, 33)
r = 179
g = 4
b = 173

class RainDrop(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.a = 255
        self.color = pygame.color.Color(r, g, b, self.a)
    
    def setup(self):
        self.h = random.choice([5, 10, 15, 20, 25])
        self.w = self.h // 4
        self.x = random.randint(1, WIDTH - self.w - 1)
        self.y = 0 - self.h - random.randint(0, 700)
        if self.h == 5:
            self.a = 100
        elif self.h == 10:
            self.a = 150
        elif self.h == 15:
            self.a = 200
        else:
            self.a = 255
        self.color = pygame.Color(r, g, b, self.a)
    
    def draw(self, win):
        rect = pygame.rect.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win, self.color, rect)
    
    def move(self):
        if self.y >= HEIGHT:
            self.setup()
        self.y += 5
    
    def update(self, win):
        self.move()
        self.draw(win)
    

raindrops = []
for i in range(200):
    raindrops.append(RainDrop())

for x in raindrops:
    x.setup()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill(bg_color)
    for i in raindrops:
        i.update(screen)
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)
