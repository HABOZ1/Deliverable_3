from character import Character


class Battle:
    """Represents a battle between two characters"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Initialise the Battle"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play a round of the battle"""

        print(f"Start: {self.hero.name} (HP: {self.hero.hp}) vs {self.enemy.name} (HP: {self.enemy.hp})")

        self.hero.attack(self.enemy)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

        print(f"End: {self.hero.name} (HP: {self.hero.hp}) vs {self.enemy.name} (HP: {self.enemy.hp})")

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is defeated"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.hero.is_alive:
            return self.hero
        elif self.enemy.is_alive:
            return self.enemy
