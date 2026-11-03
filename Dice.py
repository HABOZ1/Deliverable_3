import random


class Dice:
    """Represents a n-sided dice"""

    def __init__(self, sides: int = 6) -> None:
        """Initialise the Dice"""
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")

        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random number between 1 and the number of sides"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of Dice object"""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allows the Dice object to be called like a function to roll it"""
        return self.roll()

d20 = Dice(sides=20)  # Create a 20-sided dice
d20.roll()  # Roll the dice and get a random number between 1 and 20
