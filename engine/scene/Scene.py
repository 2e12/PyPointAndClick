import pygame


class Scene:

    objects = []
    background = None
    size = None

    def __init__(self, background):
        self.load_background(background)

    def load_background(self, background):
        self.background = pygame.image.load(background)
        self.size = self.background.get_rect().size

    def draw(self):
        return self.background
