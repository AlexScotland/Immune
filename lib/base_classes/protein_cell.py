from lib.base_classes.cell import Cell
import random, arcade
from lib.helper_functions import get_center_coordinates_of_cirle

class ProteinCell(Cell):
    
    def __init__(self, x, y, color, multiplier = 1, size = None, protein = None):
        super().__init__(x, y, color, multiplier, size)
        if not protein:
            protein = self._determine_protein()
        self.protein = protein

    def _determine_protein(self):
        """
        very simplistic generation of compatible protein
        """
        first_char = ord("A")
        last_char = ord("z")
        return chr(random.randint(first_char, last_char))

    def spawn(self):
        coords_for_text = get_center_coordinates_of_cirle(self.x, self.y, self.size)
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)
        arcade.draw_text(self.protein, coords_for_text[0], coords_for_text[1], arcade.color.BLACK, 10, 5, "center")
    
    