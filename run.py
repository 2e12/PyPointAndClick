from engine.display import Display
from engine.scene.Scene import Scene
from engine.stage import Stage


scene = Scene("test.png")
stage = Stage(scene)

Display(stage).loop()
