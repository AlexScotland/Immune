import arcade, random
from helper_functions import *
from macrophage import Macrophage

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

    def check_collision_from_cell_in_net(self, pathogen_list):
        for pathogen in pathogen_list:
            if collision_detection(self.x, self.y, pathogen.x, pathogen.y, self.size, pathogen.size):
                pathogen.speed = 0
    

