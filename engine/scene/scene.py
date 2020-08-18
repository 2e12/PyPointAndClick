import pygame

from engine.object.animation import Animation
from engine.object.object import Object


class Scene:

    background = None
    size = None
    screen = None
    player: Object = None
    stage = None
    mouse_pos = [0, 0]

    def __init__(self, background, name):
        self.objects = []
        self.load_background(background)
        self.name = name

    def switch_scene(self, scene_nr: int):
        if self.stage:
            self.stage.set_scene(self.stage.scenes[scene_nr])

    def switch_scene(self, scene_name: str):
        if self.stage:
            for scene in self.stage.scenes:
                if scene.name == scene_name:
                    self.stage.set_scene(scene)
                    break

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
