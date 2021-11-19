import arcade, random

class Cell():
    """
    main cell class
    """
    def __init__(self,x, y, color, multiplier = 1):
        self.x, self.y = x, y
        self.size = self.__set_size_of_cell()
        self.color = color
        self.speed = multiplier # pixel
        self.directions = None
        self.x_axis = ""
        self.y_axis = ""
        self.current_direction = self.determine_direction()
    
    def move_opposite_direction_of_current_direction(self, wall_hit):
        selected_direction = self.current_direction
        if wall_hit == 'right' and 'right' in selected_direction:
            if selected_direction == 'down_right':
                selected_direction ='down_left'
            elif selected_direction == 'up_right':
                selected_direction ='up_left'
            else:
                selected_direction = selected_direction.replace("right","left")
        elif wall_hit == 'left' and 'left' in selected_direction:
            if selected_direction == 'down_left':
                selected_direction ='down_right'
            elif selected_direction == 'up_left':
                selected_direction ='up_right'
            else:
                selected_direction = selected_direction.replace("left","right")
        elif wall_hit == 'top' and 'up' in selected_direction:
            selected_direction = selected_direction.replace("up","down")
        elif wall_hit == 'bottom' and 'down' in selected_direction:
            selected_direction = selected_direction.replace("down","up")
        self.current_direction = selected_direction

    def __set_size_of_cell(self):
        return random.randint(0,10)

    def spawn(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def move_direction(self):
        self.__init_directions()
        direction_key = self.directions[self.current_direction]
        self.x = direction_key['direction_math'][0]
        self.y = direction_key['direction_math'][1]
    
    def __init_directions(self):
            self.directions = {
                'left' : {
                    'direction_math':[self.x - self.speed, self.y],
                    'opposite_direction_key':'right',
                },
                'up_' : {
                    'direction_math':[self.x, self.y - self.speed],
                    'opposite_direction_key':'down_',
                },
                'right' : {
                    'direction_math':[self.x + self.speed, self.y],
                    'opposite_direction_key':'left',
                },
                'down_' : {
                    'direction_math':[self.x, self.y + self.speed],
                    'opposite_direction_key':'up_',
                    },
                'up_left' : {
                    'direction_math':[self.x - self.speed, self.y - self.speed],
                    'opposite_direction_key':'down_left',
                    },
                'up_right' : {
                    'direction_math':[self.x + self.speed, self.y - self.speed],
                    'opposite_direction_key':'down_right',
                    },
                'down_right' : {
                    'direction_math':[self.x + self.speed, self.y + self.speed],
                    'opposite_direction_key':'up_right',
                    },
                'down_left' : {
                    'direction_math':[self.x - self.speed, self.y + self.speed],
                    'opposite_direction_key':'up_left',
                    }
            }

    def determine_direction(self):
        self.__init_directions()
        direction = random.sample(self.directions.keys(), 1)[0]
        return direction