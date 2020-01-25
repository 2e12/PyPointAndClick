from engine.display import Display
from engine.object.object import Object
from engine.scene.scene import Scene
from engine.stage import Stage


scene = Scene("test.png")
test_object = Object("test.png", [50, 50])

scene.add_object(test_object)

stage = Stage(scene)

Display(stage).loop()
