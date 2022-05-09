# -*- coding: utf-8 -*-
import this
import pygame
import sys, time

import settings
import colors
import handler_frame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('8 Puzzle Report')

        self.handlerFrame =  handler_frame.HandlerFrame()
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    def run(self):
        last_time = time.time()
        while True:  
            dt = time.time() - last_time
            last_time = time.time()
                    
            # Handler Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.handlerFrame.current_frame.ui_event(event)

            # Update Display
            self.handlerFrame.current_frame.update(dt)

            self.display_surface.fill(colors.WHITE)

            # Render Display
            self.handlerFrame.current_frame.render(self.display_surface)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
