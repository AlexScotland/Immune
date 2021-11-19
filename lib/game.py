import arcade, random
from datetime import *
from pathogen import Pathogen
from macrophage import Macrophage
from neutrophil import Neutrophil
from civilian import CivilianCell
from helper_functions import *
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Simulation"
SIMULATION_SPEED = 4
MAX_NUM_OF_MACROPHAGES = random.randint(1,5)
MAX_NUM_OF_NEUTROPHILS = random.randint(1,10)
MAX_NUM_OF_PATHOGENS = random.randint(1,20)
MAX_NUM_OF_CIVILIANS = random.randint(1,300)


def out_of_screen_calculator(cell_obj):
    cell = cell_obj
    if cell.x < 0:
        return "left"
    elif cell.x > SCREEN_WIDTH-10:
        return "right"
    elif cell.y < 0:
        return "top"
    elif cell.y > SCREEN_HEIGHT-10:
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
        self.START_TIME = datetime.now()
        self.TIMER_SECONDS = 10 / SIMULATION_SPEED
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.scene = arcade.Scene()
        self.spawn_innocent()
        self.generate_good_guys()
        self.start_infection()

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        # Draw our Scene
        self.scene.draw()
        self.draw_all_cells()

        if has_time_passed(self.START_TIME,self.TIMER_SECONDS):
            for cell in self.all_cells:
                if Pathogen in cell.__class__.__mro__:
                    self.send_in_backup()
                    self.START_TIME = datetime.now()
                    break


        # Code to draw the screen goes here
    
    def draw_all_cells(self):
        for cell in self.all_cells:
            if cell.x > SCREEN_WIDTH+100 or cell.x < -100 or cell.y > SCREEN_HEIGHT+100 or cell.y < -100:
                cell.x = 100
                cell.y = 100
            ## Moves the pathogen throughout randomly
            if CivilianCell in cell.__class__.__mro__:
                cell.move_direction()
                wall_hit = out_of_screen_calculator(cell)
                if wall_hit:
                    cell.move_opposite_direction_of_current_direction(wall_hit)
            if Pathogen in cell.__class__.__mro__:
                cell.check_if_cell_can_see_cell(self.all_cells)
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
                        if cell.check_collision_from_cell_in_net(self.all_cells):
                            self.all_cells.remove(cell)

            cell.spawn()

    def start_infection(self):
        for number in range(0,MAX_NUM_OF_PATHOGENS):
            cur_pathogen  = Pathogen(random.randint(1,SCREEN_WIDTH),random.randint(1,SCREEN_HEIGHT), multiplier = SIMULATION_SPEED, size = random.randint(0,5))
            cur_pathogen.spawn()
            self.all_cells.append(cur_pathogen)

    def generate_good_guys(self):
        """
        Function spawns Macrophage warriors
        """
        for number in range(0,MAX_NUM_OF_MACROPHAGES):
            current_good_guy  = Macrophage(random.randint(1,SCREEN_WIDTH),random.randint(1,SCREEN_HEIGHT), multiplier = SIMULATION_SPEED, size=20)
            current_good_guy.spawn()
            self.all_cells.append(current_good_guy)
    
    def send_in_backup(self):
        """
        Function spawns backup (Neutrophils)
        """
        for number in range(0,MAX_NUM_OF_NEUTROPHILS):
            current_good_guy = Neutrophil(random.randint(1,SCREEN_WIDTH),random.randint(1,SCREEN_HEIGHT), SIMULATION_SPEED, size=  5)
            current_good_guy.spawn()
            self.all_cells.append(current_good_guy)

    def spawn_innocent(self):
        for number in range(0,MAX_NUM_OF_CIVILIANS):
            joe_blow = CivilianCell(random.randint(1,SCREEN_WIDTH),random.randint(1,SCREEN_HEIGHT), SIMULATION_SPEED)
            joe_blow.spawn()
            self.all_cells.append(joe_blow)