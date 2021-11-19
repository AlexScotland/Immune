import arcade, random
from pathogen import Pathogen
from Macrophage import Macrophage
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Simulation"
SIMULATION_SPEED = 4

def out_of_screen_calculator(cell_obj):
    cell = cell_obj
    if cell.x < 0:
        return "left"
        return True
    elif cell.x > SCREEN_WIDTH:
        return "right"
    elif cell.y < 0:
        return "top"
    elif cell.y > SCREEN_HEIGHT:
        return "bottom"
    return False

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
        self.generate_good_guys()
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
            ## Moves the pathogen throughout randomly
            if type(cell) is Pathogen:
                cell.move_direction()
                wall_hit = out_of_screen_calculator(cell)
                if wall_hit:
                    cell.move_opposite_direction_of_current_direction(wall_hit)
            ## Moves the Macrophage
            if type(cell) is Macrophage:
                cell.check_if_cell_can_see_cell(self.all_cells)
                if not cell.hunting:
                    ## Macrophage acts normal cause he aint a hunter yet
                    cell.move_direction()
                    wall_hit = out_of_screen_calculator(cell)
                    if wall_hit:
                        cell.move_opposite_direction_of_current_direction(wall_hit)
            cell.spawn()

    def start_infection(self):
        num_of_infected = random.randint(1,200)
        for number in range(0,num_of_infected):
            cur_pathogen  = Pathogen(random.randint(1,SCREEN_WIDTH),random.randint(1,SCREEN_HEIGHT), SIMULATION_SPEED)
            cur_pathogen.spawn()
            self.all_cells.append(cur_pathogen)

    def generate_good_guys(self):
        for number in range(1,5):
            current_good_guy  = Macrophage(random.randint(1,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT), SIMULATION_SPEED)
            current_good_guy.spawn()
            self.all_cells.append(current_good_guy)