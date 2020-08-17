class Animation:
    def __init__(self, target_position, speed=2):
        self.speed = speed
        self.target_position = target_position

    def process_step(self, position):
        ended = True
        for index, target in enumerate(self.target_position):
            if target > position[index]:
                position[index] += int(self.speed)
                ended = False
                print("front")
            if target < position[index]:
                position[index] -= int(self.speed)
                print("back")
                ended = False

        return ended
