from typing import Tuple

import pygame

from pygame import Surface
from engine import color
from engine.scene.scene import Scene


class Stage:
    origin_size: Tuple[int, int] = None
    mouse_pos = (0, 0)
    fps: int = 30
    scale_factor: int = 1
    screen: pygame.Surface = None
    scene: Scene = None
    scenes = []

    def create_surface(self):
        self.screen = Surface(self.origin_size)

    def reset_display(self):
        self.screen.fill(color.WHITE)

    def set_scene(self, scene: Scene):
        if scene not in self.scenes:
            self.scenes.append(scene)
        self.origin_size = scene.size
        self.scene = scene
        self.create_surface()

    def convert_mouse_position_to_origin_size(self, position):
        factor = self.scale_factor
        x = int(position[0] / factor)
        y = int(position[1] / factor)
        return x, y

    def on_mouse_move(self, position):
        self.scene.on_mouse_move(self.convert_mouse_position_to_origin_size(position))

    def on_mouse_click(self, position):
        click_position = self.convert_mouse_position_to_origin_size(position)
        self.scene.on_mouse_click(click_position)
        for object in self.scene.objects:
            if object.get_rect().collidepoint(click_position):
                for handler in object.get_on_click_handlers():
                    handler(object)

    def draw(self):
        self.reset_display()
        width = int(self.origin_size[0] * self.scale_factor)
        height = int(self.origin_size[1] * self.scale_factor)
        self.screen.blit(self.scene.draw(), (0, 0))

        # Scale stage up to the size of the display.
        return pygame.transform.scale(self.screen, (width, height))

