import pygame

from engine.stage import Stage


class Display:

    stage: Stage = None
    running = True
    screen = None
    size = (300, 200)

    def __init__(self, stage: Stage):
        self.stage = stage

    def loop(self):
        self.py_game_init()
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

