import random

class Enemy:
    ENEMY_TYPES = [
        {"name": "Goblin", "hp": 30, "attack_power": 5},
        {"name": "Skeleton", "hp": 40, "attack_power": 7},
        {"name": "Orc", "hp": 50, "attack_power": 10},
        {"name": "Dark Mage", "hp": 35, "attack_power": 12}
    ]
    
    def __init__(self, name, hp, attack_power):
        """Initialize an enemy with a name, health points, and attack power."""
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    @classmethod
    def random_enemy(cls):
        """Generate a random enemy from the predefined types."""
        enemy_data = random.choice(cls.ENEMY_TYPES)
        return cls(enemy_data["name"], enemy_data["hp"], enemy_data["attack_power"])
    
    def attack(self, player):
        """Enemy attacks the player."""
        player.take_damage(self.attack_power)
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")
    
    def take_damage(self, damage):
        """Reduce enemy HP when attacked."""
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! HP left: {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
    
    def is_alive(self):
        """Check if the enemy is still alive."""
        return self.hp > 0
