from cell import Cell
from pathogen import Pathogen
import random, arcade

def collision_detection(x1, y1, x2, y2, r1, r2):
    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radSumSq = (r1 + r2) * (r1 + r2)
    if (distSq == radSumSq):
        return True
    elif (distSq > radSumSq):
        return False
    else:
        return True
class Macrophage(Cell):

    def __init__(self, x, y, multiplier = 1):
        super().__init__(x, y, arcade.color.WHITE, multiplier, 10)
        self.vision = self.size + 20
        self.speed = 1.5 * multiplier
        self.hunting = False
    
    def spawn(self):
        super().spawn()
        self.draw_create_vision_circle()

    def draw_create_vision_circle(self):
        arcade.draw_circle_outline(self.x, self.y, self.vision, arcade.color.RED)

    def check_if_cell_can_see_cell(self,cell_list):
        for cell_index in range(len(cell_list)):
            cell = cell_list[cell_index]
            if type(cell) is Macrophage:
                continue
            if collision_detection(self.x + self.vision, self.y + self.vision, cell.x, cell.y, self.vision, cell.size):
                # collision_detection(self.x + vision, self.y + vision, cell.x, cell.y, self.vision, cell.size):
                self.hunting = True
                if self.hunt_down_cell(cell):
                    del cell_list[cell_index]
                    self.hunting = False
                return True
        self.hunting = False
        return False
    
    def hunt_down_cell(self, enemy_cell):
        if not collision_detection(self.x, self.y, enemy_cell.x, enemy_cell.y, self.size, enemy_cell.size):
            if self.x > enemy_cell.x:
                self.x -= self.speed
            else:
                self.x += self.speed
            if self.y > enemy_cell.y:
                self.y -= self.speed
            else:
                self.y += self.speed
        else:
            return True
    