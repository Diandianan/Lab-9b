#Diandian Wu

import random

class Agent:
    def __init__(self, name):
        self.name = name
        self.position = None

    def find_empty_patch(self, world):
        empty_patches = world.get_empty_patches()
        if empty_patches:
            return random.choice(empty_patches)
        else:
            return None

    def move_to_patch(self, new_position):
        self.position = new_position

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    