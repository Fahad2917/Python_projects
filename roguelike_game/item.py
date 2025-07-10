import random

class Item:
    ITEM_TYPES = [
        {"name": "Flaming Sword", "type": "weapon", "effect": {"attack_power": 5}},
        {"name": "Iron Shield", "type": "armor", "effect": {"damage_reduction": 3}},
        {"name": "Healing Potion", "type": "potion", "effect": {"heal": 20}},
        {"name": "Strength Elixir", "type": "potion", "effect": {"attack_boost": 5}}
    ]
    
    def __init__(self, name, item_type, effect):
        """Initialize an item with a name, type, and effect."""
        self.name = name
        self.item_type = item_type
        self.effect = effect
    
    @classmethod
    def random_item(cls):
        """Generate a random item from the predefined types."""
        item_data = random.choice(cls.ITEM_TYPES)
        return cls(item_data["name"], item_data["type"], item_data["effect"])
    
    def apply(self, player):
        """Apply the item's effect to the player."""
        if self.item_type == "weapon":
            player.attack_power += self.effect["attack_power"]
            print(f"{player.name} equips {self.name}! Attack power increased by {self.effect['attack_power']}.")
        elif self.item_type == "armor":
            player.armor = self.effect["damage_reduction"]
            print(f"{player.name} equips {self.name}! Damage reduction: {self.effect['damage_reduction']}.")
        elif self.item_type == "potion":
            if "heal" in self.effect:
                player.hp += self.effect["heal"]
                print(f"{player.name} drinks {self.name} and restores {self.effect['heal']} HP!")
            if "attack_boost" in self.effect:
                player.attack_power += self.effect["attack_boost"]
                print(f"{player.name} drinks {self.name}! Attack power increased by {self.effect['attack_boost']}.")
