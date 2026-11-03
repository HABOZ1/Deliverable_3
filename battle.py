from character import Character
import random

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
        if random.randint(0, 5) == 1:
            self.hero.heal(20)
            print("Hero healed!")

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
            if random.randint(0, 5) == 2:
                self.enemy.heal(20)
                print("Enemy Healed!")

        print(f"End: {self.hero.name} (HP: {self.hero.hp}) vs {self.enemy.name} (HP: {self.enemy.hp})\n")

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is defeated"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.hero.is_alive:
            return self.hero
        
        return self.enemy
