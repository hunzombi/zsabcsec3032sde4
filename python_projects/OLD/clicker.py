import pyautogui
from time import sleep

sleep(5)

color = (0, 0, 255)

def click():
    run = True
    s = pyautogui.screenshot()
    for x in range(0, s.width, 80):
        for y in range(0, s.height, 80):
            print(s.getpixel((x, y)))
            if s.getpixel((x, y)) == color and run:
                pyautogui.click(x+5, y+5)
                run = False

while True:
    click()