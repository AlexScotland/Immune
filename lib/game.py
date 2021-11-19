import arcade, random, time
from pathogen import Pathogen
from macrophage import Macrophage
from neutrophil import Neutrophil
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Simulation"
SIMULATION_SPEED = 1
MAX_NUM_OF_MACROPHAGES = random.randint(1,5)
MAX_NUM_OF_NEUTROPHILS = random.randint(1,3)
MAX_NUM_OF_PATHOGENS = random.randint(0,500)
TIMER_SECONDS = 60 / SIMULATION_SPEED

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
            elif Macrophage in cell.__class__.__mro__:
                cell.check_if_cell_can_see_cell(self.all_cells)
                if not cell.hunting:
                    ## Macrophage acts normal cause he aint a hunter yet
                    cell.move_direction()
                    wall_hit = out_of_screen_calculator(cell)
                    if wall_hit:
                        cell.move_opposite_direction_of_current_direction(wall_hit)
                if Neutrophil in cell.__class__.__mro__:
                    if cell.check_for_self_destruct():
                        cell.convert_to_net()
                    if cell.converted_to_net:
                        cell.check_collision_from_cell_in_net(self.all_cells)
            cell.spawn()

    def start_infection(self):
        for number in range(1,MAX_NUM_OF_PATHOGENS):
            cur_pathogen  = Pathogen(random.randint(1,SCREEN_WIDTH),random.randint(1,SCREEN_HEIGHT), SIMULATION_SPEED)
            cur_pathogen.spawn()
            self.all_cells.append(cur_pathogen)

    def generate_good_guys(self):
        """
        Function spawns Macrophage warriors
        """
        for number in range(1,5):
            current_good_guy  = Macrophage(random.randint(1,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT), SIMULATION_SPEED, 20)
            current_good_guy.spawn()
            self.all_cells.append(current_good_guy)
    
    def send_in_backup(self):
        """
        Function spawns backup (Neutrophils)
        """
        for number in range(1,5):
            current_good_guy  = Neutrophil(random.randint(1,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT), SIMULATION_SPEED, 5)
            current_good_guy.spawn()
            self.all_cells.append(current_good_guy)
