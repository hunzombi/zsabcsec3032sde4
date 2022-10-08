import pygame
import zsompy
pygame.init()


class Screen64(object):
    
    def __init__(self):
        self.w = 10
        self.h = 10
        self.WIDTH = self.w * 64
        self.HEIGHT = self.h * 64
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.pixels = zsompy.zeros((64, 64))
        self.colors = ["black", "green"]
    
    def draw_pixels(self):
        for y, row in enumerate(self.pixels):
            for x, pixel in enumerate(row):
                rect = pygame.rect.Rect(x, y, 10, 10)
                pygame.draw.rect(self.screen, self.colors[pixel], rect)
        return self
    
    def set_color(self, positionInArray, color):
        self.colors[positionInArray] = color
        return self
    

if __name__ == '__main__':
    scr = Screen64()
    while True:
        scr.draw_pixels()