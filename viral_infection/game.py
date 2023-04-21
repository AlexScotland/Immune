import arcade, random
from datetime import *
from lib.models.host import Host
from lib.helper_functions import *
from lib.models.viruses.influenza import Influenza
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Simulation"
SIMULATION_SPEED = 20
MAX_NUM_OF_CIVILIANS = 200 #random.randint(20,50)
MAX_NUM_OF_OUTBREAK = 1


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
        self.list_of_hosts=[]
        self.list_of_virus=[]
        self.TIMER_SECONDS = 10 / SIMULATION_SPEED
        self.healthy = 0
        self.spreaders = 0
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.scene = arcade.Scene()
        self.start_virus_outbreak()
        self.create_all_hosts()
    
    def create_all_hosts(self):
        for iteration in range(0, MAX_NUM_OF_CIVILIANS):
            current_host = Host(
                random.randint(1,SCREEN_WIDTH),
                random.randint(1,SCREEN_HEIGHT), 
                color = (random.randint(50,255), random.randint(50,255), random.randint(50,255)),
                multiplier = SIMULATION_SPEED, 
                size = 10
            )
            if virus:= check_if_host_infected(current_host, self.list_of_virus):
                current_host._infect(virus)
            current_host.spawn()
            self.list_of_hosts.append(current_host)

    def start_virus_outbreak(self):
        for iteration in range(0, MAX_NUM_OF_OUTBREAK):
            self.list_of_virus.append(
                Influenza(
                    0,
                    0,
                    color = arcade.csscolor.CORNFLOWER_BLUE,
                    override=True
                )
            )


    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        # Draw our Scene
        self.scene.draw()
        self.draw()

    def draw(self):
        self.healthy = 0
        self.spreaders = 0
        infect_touching_hosts(self.list_of_hosts)

        for host in self.list_of_hosts:
            if host.sick:
                self.spreaders +=1
            else:
                self.healthy +=1
            host.move_direction()
            wall_hit = out_of_screen_calculator(host)
            if wall_hit:
                host.move_opposite_direction_of_current_direction(wall_hit)

            host.spawn()
        display = f"Healthy: {self.healthy}, Sick: {self.spreaders}.  Sick % {self.spreaders/len(self.list_of_hosts)*100}"
        arcade.draw_text(str(display),10,20,arcade.color.GREEN,20,180,'left')