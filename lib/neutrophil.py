import arcade, random
from helper_functions import *
from macrophage import Macrophage
from civilian import CivilianCell
from pathogen import Pathogen

class Neutrophil(Macrophage):
    def __init__(self, x, y, multiplier = 1, size=5):
        super().__init__(x, y, arcade.color.AMARANTH_PURPLE, multiplier, size)
        self.speed = 2 * multiplier
        self.converted_to_net = False
        self.self_destruct_timer = random.randint(100,1000)/multiplier
    
    def spawn(self):
        if self.converted_to_net:
            arcade.draw_circle_outline(self.x, self.y, self.size, arcade.color.BLACK)
        else:
            super().spawn()
    
    def check_if_cell_can_see_cell(self,cell_list):
        for cell_index in range(len(cell_list)):
            cell = cell_list[cell_index]
            if Macrophage in cell.__class__.__mro__:
                continue

            if collision_detection(self.x + self.vision, self.y + self.vision, cell.x, cell.y, self.vision, cell.size) and not self.converted_to_net:
                self.hunting = True
                if self.hunt_down_cell(cell):
                    del cell_list[cell_index]
                    self.hunting = False
                return True
        self.hunting = False
        return False

    def convert_to_net(self):
        if not self.converted_to_net:
            self.speed = 0
            self.size += 5
            self.converted_to_net = True

    def move_direction(self):
        super().move_direction()
        self.self_destruct_timer -= 1
    
    def check_for_self_destruct(self):
        if self.self_destruct_timer <= 0:
            return True
        else: 
            return False

    def check_collision_from_cell_in_net(self, cell_list):
        for cell in cell_list:
            if collision_detection(self.x, self.y, cell.x, cell.y, self.size, cell.size):
                if Macrophage in cell.__class__.__mro__ or CivilianCell in cell.__class__.__mro__ :
                    return False
                else:
                    cell.speed = 0
        return True
    

