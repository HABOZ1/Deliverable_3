from character import Character


class Battle:
    """Represents a battle between two characters"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Initialise the Battle"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play a round of the battle"""

        self.hero.attack(self.enemy)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is defeated"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")
