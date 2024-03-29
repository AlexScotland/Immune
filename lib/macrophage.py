from lib.base_classes.cell import Cell
import arcade
from lib.helper_functions import *
from lib.civilian import CivilianCell
from lib.pathogen import Pathogen

class Macrophage(Cell):

    def __init__(self, x, y, color=arcade.color.AFRICAN_VIOLET, multiplier = 1, size=20):
        super().__init__(x, y, color, multiplier, size)
        self.vision = self.size + 40
        self.speed = .5 * multiplier
        self.hunting = False
    
    def spawn(self):
        super().spawn()
        self.draw_create_vision_circle()

    def draw_create_vision_circle(self):
        arcade.draw_circle_outline(self.x, self.y, self.vision, arcade.color.RED)

    def check_if_cell_can_see_cell(self,cell_list):
        for cell_index in range(len(cell_list)):
            cell = cell_list[cell_index]
            if Macrophage in cell.__class__.__mro__ or CivilianCell in cell.__class__.__mro__:
                continue
            if collision_detection(self.x, self.y, cell.x, cell.y, self.vision, cell.size):
                # collision_detection(self.x + vision, self.y + vision, cell.x, cell.y, self.vision, cell.size):
                self.hunting = True
                if self.hunt_down_cell(cell):
                    del cell_list[cell_index]
                    self.hunting = False
                return True
        self.hunting = False
        return False
    
    def hunt_down_cell(self, enemy_cell):
        if collision_detection(self.x+10, self.y+10, enemy_cell.x, enemy_cell.y, self.vision, enemy_cell.size):
            if self.x > enemy_cell.x:
                self.x -= self.speed
            else:
                self.x += self.speed
            if self.y > enemy_cell.y:
                self.y -= self.speed
            else:
                self.y += self.speed
        if collision_detection(self.x+10, self.y+10, enemy_cell.x, enemy_cell.y, self.size, enemy_cell.size):
            return True
    