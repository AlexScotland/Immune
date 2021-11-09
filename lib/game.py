import arcade, random
from pathogen import Pathogen
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Simulation"


class Sim(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.scene = None
        self.all_cells=[]
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.scene = arcade.Scene()
        self.start_infection()

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        # Draw our Scene
        self.scene.draw()
        self.draw_all_cells()
        # Code to draw the screen goes here
    
    def draw_all_cells(self):
        for cell in self.all_cells:
            cell.move_direction()
            cell.spawn()

    def start_infection(self):
        num_of_infected = random.randint(1,100)
        for number in range(0,num_of_infected):
            cur_pathogen  = Pathogen(random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT))
            cur_pathogen.spawn()
            self.all_cells.append(cur_pathogen)

