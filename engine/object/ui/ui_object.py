from pygame.surface import Surface

from engine.object.object import Object


class UiObject(Object):
    def __init__(self, position, size):
        self.position = position
        self.set_size(size)

    def set_size(self, size):
        self.size = size
        self.screen = Surface(size)
