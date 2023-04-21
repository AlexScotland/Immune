from lib.base_classes.cell import Cell
import arcade
from lib.helper_functions import *

class CivilianCell(Cell):
    def __init__(self, x, y, multiplier = 1, color=arcade.color.WHITE):
        super().__init__(x, y, color, multiplier)
        self.vision = self.size + 20
        self.speed = 1 * multiplier
        self.hunting = False

    