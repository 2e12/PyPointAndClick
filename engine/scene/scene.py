import pygame


class Scene:

    objects = []
    background = None
    size = None
    screen = None

    def __init__(self, background):
        self.load_background(background)

    def load_background(self, background):
        self.background = pygame.image.load(background)
        self.size = self.background.get_rect().size
        self.screen = pygame.Surface(self.size)

    def add_object(self, obj):
        self.objects.append(obj)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for scene_object in self.objects:
            self.screen.blit(scene_object.draw(), scene_object.position)
        return self.screen
