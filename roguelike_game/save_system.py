import json

class SaveSystem:
    SAVE_FILE = "save.json"
    
    def save_game(self, player, dungeon):
        """Save the player's progress and dungeon state to a JSON file."""
        data = {
            "player": {
                "name": player.name,
                "hp": player.hp,
                "attack_power": player.attack_power,
                "inventory": [item.name for item in player.inventory],
                "gold": player.gold
            },
            "dungeon": {
                "rooms": [room.room_id for room in dungeon.rooms],
                "current_room_index": dungeon.current_room_index
            }
        }
        with open(self.SAVE_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print("Game progress saved!")
    
    def load_game(self):
        """Load the player's progress and dungeon state from a JSON file."""
        try:
            with open(self.SAVE_FILE, "r") as file:
                data = json.load(file)
            
            from player import Player
            from dungeon import Dungeon
            from item import Item
            
            player = Player(
                name=data["player"]["name"],
                hp=data["player"]["hp"],
                attack_power=data["player"]["attack_power"]
            )
            player.gold = data["player"].get("gold", 0)
            player.inventory = [Item(item_name, "potion", {"heal": 20}) for item_name in data["player"]["inventory"]]
            
            dungeon = Dungeon()
            dungeon.current_room_index = data["dungeon"]["current_room_index"]
            
            print("Game loaded successfully!")
            return player, dungeon
        except (FileNotFoundError, json.JSONDecodeError):
            print("No valid save file found. Starting a new game.")
            return None, None
