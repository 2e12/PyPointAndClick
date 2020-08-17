from __future__ import annotations  # Import this in order to use this class('Object') for type hinting
from typing import Callable, List
from engine.object.animation import Animation
import pygame


class Object:

    screen = None
    size = None
    position = None
    animation: Animation = None
    _onclick_handlers: List[Callable[[Object], None]] = []

    def __init__(self, image, position):
        self.set_image(image)
        self.position = position

    def set_image(self, image):
        self.screen = pygame.image.load(image)
        self.size = self.screen.get_rect().size

    def get_rect(self):
        rect = self.screen.get_rect()
        rect.x = self.position[0]
        rect.y = self.position[1]
        return rect

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

    def add_on_click_handler(self, onclick: Callable[[Object], None]):
        if onclick not in self._onclick_handlers:
            self._onclick_handlers.append(onclick)

    def remove_on_click_handler(self, onclick: Callable[[Object], None]):
        if onclick in self._onclick_handlers:
            self._onclick_handlers.remove(onclick)

    def get_on_click_handlers(self):
        return self._onclick_handlers
