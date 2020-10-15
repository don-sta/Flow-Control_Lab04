# ETTG 1801
# Donald Stapleton
# Lab04 Flow Control
# Date: 09/29/2020
import pygame
import random
import time

pygame.display.init()

window = pygame.display.set_mode((500, 500))

myColors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

print(myColors)

for number in range(101):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pygame.draw.circle(window, random.choice(myColors), (x, y), 30, 00)

pygame.display.update()

time.sleep(5)
