#!/usr/bin/env python
import pygame
pygame.init()

SIZE = (600, 600)

scrn = pygame.display.set_mode(SIZE)
running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
