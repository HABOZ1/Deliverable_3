from dice import Dice

class Weapon:
    """Represents a weapon"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Initialise the Weapon"""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the damage dice to determine damage"""
        return self.damage_dice.roll()
