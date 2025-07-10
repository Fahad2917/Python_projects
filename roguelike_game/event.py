import random
from item import Item  # Import the Item class

class Event:
    EVENT_TYPES = [
        {"name": "Treasure Chest", "effect": "gold", "value": random.randint(10, 50)},
        {"name": "Riddle Challenge", "effect": "puzzle", "riddle": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
        {"name": "Mysterious Merchant", "effect": "shop", "offer": {"item": "Strength Potion", "price": 10}}
    ]
    
    def __init__(self, name, effect, value=None, riddle=None, answer=None, offer=None):
        """Initialize an event with a name, effect, and optional attributes."""
        self.name = name
        self.effect = effect
        self.value = value
        self.riddle = riddle
        self.answer = answer
        self.offer = offer
    
    @classmethod
    def random_event(cls):
        """Generate a random event from the predefined types."""
        event_data = random.choice(cls.EVENT_TYPES)
        return cls(
            event_data["name"],
            event_data["effect"],
            event_data.get("value"),
            event_data.get("riddle"),
            event_data.get("answer"),
            event_data.get("offer")
        )
    
    def trigger(self, player):
        """Trigger the event and apply its effect."""
        print(f"Event triggered: {self.name}")
        
        if self.effect == "gold":
            print(f"You found a treasure chest with {self.value} gold!")
            player.gold += self.value
        elif self.effect == "puzzle":
            print(f"Riddle: {self.riddle}")
            answer = input("Your answer: ").lower()
            if answer == self.answer:
                print("Correct! You receive a bonus item.")
                player.pick_up_item(Item.random_item())  # Now `Item` is defined
            else:
                print("Wrong answer! The door remains locked.")
        elif self.effect == "shop":
            print(f"A merchant offers a {self.offer['item']} for {self.offer['price']} gold.")
            choice = input("Do you want to buy it? (yes/no): ").lower()
            if choice == "yes" and player.gold >= self.offer["price"]:
                print("You bought the item!")
                player.gold -= self.offer["price"]
                player.pick_up_item(Item(self.offer["item"], "potion", {"heal": 20}))
            else:
                print("You decline the offer.")
