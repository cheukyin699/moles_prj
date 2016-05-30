#!/usr/bin/env python
import pygame
pygame.init()

SIZE = (600, 600)
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
RED         = (200, 0, 0)
GREEN       = (0, 200, 0)
BLUE        = (0, 0, 200)

scrn = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    clock.tick(FPS)

    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False

        # Handle keyboard inputs

    # Update the state

    scrn.fill(BLACK)

    # Draw the state

    pygame.display.flip()
