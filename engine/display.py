import pygame

from pygame.locals import *
from engine.stage import Stage
from engine import color


class Display:

    stage: Stage = None
    running = True
    screen = None
    size = (800, 650)

    def __init__(self, stage: Stage):
        self.stage = stage
        pygame.init()
        self.init_screen()

    def loop(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(self.stage.fps)
            self.set_stage_scale_factor()
            self.handle_events()
            self.draw()

    def reset_display(self):
        self.screen.fill(color.GREY)

    def draw(self):
        self.reset_display()
        self.screen.blit(self.stage.draw(), (0,0))
        pygame.display.flip()

    def init_screen(self):
        self.screen = pygame.display.set_mode(self.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.VIDEORESIZE:
                self.size = (event.w, event.h)
                self.init_screen()

    def set_stage_scale_factor(self):
        self.stage.scale_factor = self.get_stage_scale_factor()

    def get_stage_scale_factor(self):
        scale_width = self.size[0] / self.stage.origin_size[0]
        scale_height = self.size[1] / self.stage.origin_size[1]
        if scale_width < scale_height:
            return scale_width
        else:
            return scale_height
