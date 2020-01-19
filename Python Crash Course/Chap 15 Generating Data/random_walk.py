from random import choice            # choice() decides which move to make on each step

class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):        # default number of points
        """Initialize attributes of a walk"""
        self.num_points = num_points
        # All walk start at (0,0)
        self.x_values = [0]                     # list to hold x- and y-values
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how to far to go in that direction
            # x_direction = choice([1, -1])
            # x_distance = choice([0,1,2,3,4])
            # x_step = x_direction * x_distance
            x_step = self.get_step()

            # y_direction = choice([1, -1])
            # y_distance = choice([0, 1, 2, 3, 4])
            # y_step = y_direction * y_distance
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    # 15-5 Refactoring fill_walk() to get rid of duplicate code
    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        return direction * distance

