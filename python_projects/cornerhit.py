import pygame
import sys

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
myFony = pygame.font.Font(None, 32)
pixels = []

def drawPixels():
    for pixel in pixels:
        rect = pygame.rect.Rect(pixel[0], pixel[1], 1, 1)
        pygame.draw.rect(screen, "red", rect)

class myRect(object):
    def __init__(self):
        self.w = 100
        self.h = 60
        self.x = 0
        self.y = 0
        self.x_vel = 2
        self.y_vel = 2
        self.colors = ["red", "blue", "yellow", "green"]
        self.colorIndex = 0
    
    def draw(self, win):
        rect = pygame.rect.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win, self.colors[self.colorIndex], rect)
    
    def next_color(self):
        if self.colorIndex == len(self.colors) - 1:
            self.colorIndex = 0
        else:
            self.colorIndex += 1
    
    def move(self):
        global pixels
        if (self.x + self.w // 2, self.y + self.h // 2) not in pixels:
            pixels.append((self.x + self.w // 2, self.y + self.h // 2))
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x + self.w > WIDTH or self.x < 0:
            self.x_vel = -self.x_vel
            self.next_color()
        
        if self.y + self.h > HEIGHT or self.y < 0:
            self.y_vel = -self.y_vel
            self.next_color()

myrect = myRect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    myrect.move()
    
    screen.fill("black")
    drawPixels()
    myrect.draw(screen)

    pygame.display.flip()
    pygame.display.update()
