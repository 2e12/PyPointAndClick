from engine.object.object import Object


class Character(Object):
    tiles = []
    active_tile = 0
    steps = 0

    def __init__(self, image, position, tile_size=(64, 64), animation_steps=3):
        super().__init__(image, position)
        self.tile_size = tile_size
        self.tile_count = int(self.screen.get_width() / tile_size[0])
        self.animation_steps = animation_steps
        self.generate_images_form_tiles()

    def generate_images_form_tiles(self):
        for i in range(self.tile_count):
            # ((left, top), (width, height))
            tile = self.screen.subsurface((i * self.tile_size[0], 0), self.tile_size)
            self.tiles.append(tile)

    def draw(self):
        self.process_animation()
        return self.tiles[self.active_tile]

    def update_active_tile(self):
        self.steps += 1
        if self.steps >= self.tile_count * self.animation_steps:
            self.steps = 0
        self.active_tile = int(self.steps / self.animation_steps)

    def process_animation(self):
        if self.animation:
            self.update_active_tile()
        super().process_animation()