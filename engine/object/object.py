import pygame


class Object:

    screen = None
    size = None
    position = None

    def __init__(self, image, position):
        self.set_image(image)
        self.position = position

    def set_image(self, image):
        self.screen = pygame.image.load(image)
        self.size = self.image.get_rect().size

    def draw(self):
        return self.screen