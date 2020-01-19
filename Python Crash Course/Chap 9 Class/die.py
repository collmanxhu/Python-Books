from random import randint

"""class to simulate a Die"""
class Die:
    """Die with 6 sides"""
    def __init__(self, sides=6, roll_times=1):
        self.sides = sides
        self.roll_times = roll_times

    """roll a die to show side"""
    def roll_die(self):
        # for roll_time in self.roll_times:
        for roll_time in range(self.roll_times):
            print(f"roll times: {roll_time}")
            print(f"The die rolls number {randint(1, self.sides)}.")

my_roll = Die(10,10)
my_roll.roll_die()