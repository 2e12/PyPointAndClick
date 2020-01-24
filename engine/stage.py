import pygame

from pygame import Surface
from engine import color


class Stage:
    origin_size = None
    mouse_pos = (0, 0)
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

    def convert_mouse_position_to_origin_size(self, position):
        factor = self.scale_factor
        x = position[0] / factor
        y = position[1] / factor
        return x, y

    def on_mouse_move(self, position):
        self.mouse_pos = self.convert_mouse_position_to_origin_size(position)

    def on_mouse_click(self, position):
        self.mouse_pos = self.convert_mouse_position_to_origin_size(position)

    def draw(self):
        self.reset_display()
        width = int(self.origin_size[0] * self.scale_factor)
        height = int(self.origin_size[1] * self.scale_factor)
        return pygame.transform.scale(self.screen, (width, height))

