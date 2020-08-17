import pygame

from engine.object.animation import Animation


class Object:

    screen = None
    size = None
    position = None
    animation: Animation = None

    def __init__(self, image, position):
        self.set_image(image)
        self.position = position

    def set_image(self, image):
        self.screen = pygame.image.load(image)
        self.size = self.screen.get_rect().size

    def process_animation(self):
        if self.animation:
            animation_ended = self.animation.process_step(self.position)
            if animation_ended:
                self.animation = None

    def draw(self):
        self.process_animation()
        return self.screen

    def set_animation(self, animation: Animation):
        self.animation = animation
