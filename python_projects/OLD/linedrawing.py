from cmath import pi
import pygame
from sys import exit
from MyModules import zsompy

pygame.init()
screen = pygame.display.set_mode((500, 500))

pixels = zsompy.zeros((50, 50))
print(pixels)
pixels[24][24] = 1
pixels[24][25] = 1
pixels[23][26] = 1

def draw_pixels():
    for row_index, row in enumerate(pixels):
        for pixel_index, pixel in enumerate(row):
            color = 'black'
            if pixel == 1:
                color = "white"
            square = pygame.rect.Rect(pixel_index*10, row_index*10, 10, 10)
            pygame.draw.rect(screen, color, square)


def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('black')
        draw_pixels()
        
        pygame.display.flip()
        pygame.display.update()

main_loop()