import importlib.util
import os
import sys

from engine.display import Display
from engine.stage import Stage


class Load:
    scenes = []

    def __init__(self):
        self.load("data")
        stage = Stage(self.scenes[0])
        Display(stage).loop()

    def load(self, path):
        for file in os.listdir(path):
            if os.path.isdir("{}/{}".format(path, file)):
                if os.path.exists("{}/{dir}/{dir}.py".format(path, dir=file)):
                    import_path = "{}.{dir}.{dir}".format(path, dir=file)
                    scene_module = importlib.import_module(import_path)
                    self.scenes.append(scene_module.scene)


Load()
