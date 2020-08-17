import pygame

from engine.object.animation import Animation
from engine.object.object import Object


class Scene:

    objects = []
    background = None
    size = None
    screen = None
    player: Object = None
    mouse_pos = [0, 0]

    def __init__(self, background):
        self.load_background(background)

    def load_background(self, background):
        self.background = pygame.image.load(background)
        self.size = self.background.get_rect().size
        self.screen = pygame.Surface(self.size)

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def set_player(self, obj):
        if obj not in self.objects:
            self.objects.append(obj)
        self.player = obj

    def on_mouse_move(self, position):
        self.update_mouse_postion(position)

    def on_mouse_click(self, position):
        self.update_mouse_postion(position)
        if self.player:
            self.player.set_animation(Animation(target_position=self.get_mouse_position()))

    def update_mouse_postion(self, position):
        self.mouse_pos = position

    def get_mouse_position(self):
        return self.mouse_pos

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for scene_object in self.objects:
            self.screen.blit(scene_object.draw(), scene_object.position)
        return self.screen
