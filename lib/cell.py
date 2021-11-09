

import arcade

class Cell():
    """
    main cell class
    """
    def __init__(self, color):
        self.x, self.y = None, None
        self.size = 20
        self.color = color
    
    def spawn(self, x, y):
        self.x, self.y = x, y
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)


