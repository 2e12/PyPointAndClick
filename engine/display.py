import pygame

from engine.stage import Stage


class Display:

    stage: Stage = None
    running = True
    screen = None
    size = (600, 500)

    def __init__(self, stage: Stage):
        self.stage = stage
        stage.scale_factor = self.get_stage_scale_factor()
        self.py_game_init()

    def loop(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(self.stage.fps)
            self.handle_events()

    def py_game_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def get_stage_scale_factor(self):
        scale_width = self.size[0] / self.stage.origin_size[0]
        scale_height = self.size[1] / self.stage.origin_size[1]
        if scale_width < scale_height:
            return scale_width
        else:
            return scale_height
