# -*- coding: utf-8 -*-
import pygame
import sys
from settings import *
from ship import *
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    ship = Ship(screen)
    pygame.display.set_caption('飞机大战')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()
