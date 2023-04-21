"""
Developer: Alex Scotland
Proj: Immune - Spread of Viral Infections
"""

from lib.game import Sim
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
