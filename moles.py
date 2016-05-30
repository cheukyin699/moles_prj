#!/usr/bin/env python
import pygame
import state
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
curr_state = state.GameState(scrn)

while running:
    clock.tick(FPS)

    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False

        # Handle keyboard inputs
        curr_state.handle(e)

    # Update the state
    curr_state.update(clock.get_time())

    scrn.fill(BLACK)

    # Draw the state
    curr_state.draw()

    pygame.display.flip()
