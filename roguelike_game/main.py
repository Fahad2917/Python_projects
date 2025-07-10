import json
import os
from player import Player
from dungeon import Dungeon
from battle import Battle
from save_system import SaveSystem

def main():
    print("Welcome to the Roguelike Dungeon Adventure!")
    save_system = SaveSystem()
    
    # Step 1: Check for existing save file
    if os.path.exists("save.json"):
        choice = input("A save file was found. Do you want to continue? (yes/no): ").lower()
        if choice == "yes":
            player, dungeon = save_system.load_game()
        else:
            player = create_new_player()
            dungeon = Dungeon()
    else:
        player = create_new_player()
        dungeon = Dungeon()
    
    # Step 2: Game Loop
    for room in dungeon:
        if player.hp <= 0:
            print("Game Over! You have been defeated.")
            break
        
        print(f"\nYou have entered {room.name}.")
        room.describe()
        
        # Handle enemies
        if room.enemy:
            battle = Battle(player, room.enemy)
            battle.start_combat()
            if player.hp <= 0:
                print("You have died in battle! Game Over.")
                break
        
        # Handle items
        if room.item:
            choice = input(f"You found {room.item.name}. Pick it up? (yes/no): ").lower()
            if choice == "yes":
                player.pick_up_item(room.item)
        
        # Handle special events
        if room.event:
            room.event.trigger(player)
        
        # Save progress after every action
        save_system.save_game(player, dungeon)
        
        if dungeon.is_exit(room):
            print("Congratulations! You have reached the dungeon exit and won the game!")
            break

def create_new_player():
    name = input("Enter your character's name: ")
    return Player(name)

if __name__ == "__main__":
    main()
