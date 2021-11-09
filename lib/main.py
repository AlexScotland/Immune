"""
Developer: Alex Scotland
Proj: Immune

"""

from game import Sim
import arcade

def start():
    """
    main function that starts the game
    """
    window = Sim()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    start()
