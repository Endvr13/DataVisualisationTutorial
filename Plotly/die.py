from random import randint


class Die:
    """Class to represent a single die"""

    def __init__(self, num_sides=6):
        """Assume 6-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the nbumber of sides"""
        return randint(1, self.num_sides)
