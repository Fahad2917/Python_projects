class Player:
    def __init__(self, name, hp=100, attack_power=10, gold=0):
        """Initialize the player with a name, health points, attack power, gold, and an empty inventory."""
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.inventory = []
        self.gold = gold  # Added gold attribute
    
    def pick_up_item(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}!")
    
    def use_item(self, item_name):
        """Use an item from the inventory if available."""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.apply(self)
                self.inventory.remove(item)
                print(f"{self.name} used {item_name}.")
                return
        print(f"{item_name} is not in your inventory.")
    
    def attack(self, enemy):
        """Attack an enemy, reducing their HP."""
        enemy.hp -= self.attack_power
        print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")
    
    def take_damage(self, damage):
        """Reduce player's HP when attacked."""
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! HP left: {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
    
    def show_inventory(self):
        """Display the player's inventory."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name}")
    
    def is_alive(self):
        """Check if the player is still alive."""
        return self.hp > 0
