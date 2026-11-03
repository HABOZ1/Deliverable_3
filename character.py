class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """Take damage and reduce HP"""
        self._hp -= amount
        self._hp = max(self._hp, 0)  # Ensure HP does not go below 0

    def heal(self, amount: int) -> None:
        """Heal and increase HP"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # Ensure HP does not go above max

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""

        if self.weapon is not None:
            damage = self.weapon.roll_damage()  # Roll damage based on weapon
        else:
            damage = self.damage  # Use character's base damage if no weapon

        target.take_damage(damage)  # Calls the target's take_damage() method

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        return self._hp > 0  # Returns True if hp is above 0, and False otherwise
