import arcade, random

class Cell():
    """
    main cell class
    """
    def __init__(self,x, y, color):
        self.x, self.y = x, y
        self.size = self.__set_size_of_cell()
        self.color = color
        self.speed = 1 # pixel
        self.directions = None
        self.current_direction = self.determine_direction()
    
    def __set_size_of_cell(self):
        return random.randint(0,10)

    def spawn(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def move_direction(self):
        self.__init_directions()
        direction_key = self.directions[self.current_direction]
        self.x = direction_key[0]
        self.y = direction_key[1]
    
    def __init_directions(self):
            self.directions = {
                'left' : [self.x - self.speed, self.y] ,
                'up' : [self.x, self.y - self.speed],
                'right' : [self.x + self.speed, self.y],
                'down' : [self.x, self.y + self.speed],
                'up_left' : [self.x - self.speed, self.y - self.speed],
                'up_right' : [self.x + self.speed, self.y - self.speed],
                'down_right' : [self.x + self.speed, self.y + self.speed],
                'down_left' : [self.x - self.speed, self.y + self.speed]
            }

    def determine_direction(self):
        self.__init_directions()
        return random.sample(self.directions.keys(), 1)[0]