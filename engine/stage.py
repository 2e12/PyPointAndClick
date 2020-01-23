import pygame

from pygame import Surface
from engine import color


class Stage:
    origin_size = (250, 250)
    fps = 30
    scale_factor = 1
    screen = None

    def __init__(self, resolution):
        self.origin_size = resolution
        self.create_surface()

    def create_surface(self):
        self.screen = Surface(self.origin_size)

    def reset_display(self):
        self.screen.fill(color.WHITE)

    def draw(self):
        self.reset_display()
        return self.screen

