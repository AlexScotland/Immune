from cell import Cell
import random, arcade

class Pathogen(Cell):

    def __init__(self, x, y):
        super().__init__(x, y, arcade.color.ANDROID_GREEN)
    