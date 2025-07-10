import random
from enemy import Enemy
from item import Item
from event import Event

class Room:
    def __init__(self, room_id):
        """Initialize a room with potential enemies, items, and events."""
        self.room_id = room_id
        self.name = f"Room {room_id}"
        self.enemy = self.generate_enemy()
        self.item = self.generate_item()
        self.event = self.generate_event()
    
    def generate_enemy(self):
        """Randomly assign an enemy to the room or leave it empty."""
        return Enemy.random_enemy() if random.random() < 0.5 else None
    
    def generate_item(self):
        """Randomly assign an item to the room or leave it empty."""
        return Item.random_item() if random.random() < 0.4 else None
    
    def generate_event(self):
        """Randomly assign an event to the room or leave it empty."""
        return Event.random_event() if random.random() < 0.3 else None
    
    def describe(self):
        """Describe the contents of the room."""
        print(f"You are in {self.name}.")
        if self.enemy:
            print(f"An enemy is here: {self.enemy.name}!")
        if self.item:
            print(f"You see an item: {self.item.name}.")
        if self.event:
            print("Something strange is happening in this room...")
