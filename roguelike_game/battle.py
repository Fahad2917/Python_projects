class Battle:
    def __init__(self, player, enemy):
        """Initialize a battle between the player and an enemy."""
        self.player = player
        self.enemy = enemy
    
    def start_combat(self):
        """Start the turn-based combat loop until one is defeated."""
        print(f"A wild {self.enemy.name} appears!")
        
        while self.player.is_alive() and self.enemy.is_alive():
            print("\nYour Turn:")
            print("1. Attack")
            print("2. Use Item")
            print("3. Flee")
            choice = input("Choose an action: ")
            
            if choice == "1":
                self.player.attack(self.enemy)
            elif choice == "2":
                item_name = input("Enter the item name to use: ")
                self.player.use_item(item_name)
            elif choice == "3":
                print("You fled from the battle!")
                return
            else:
                print("Invalid choice. Try again.")
                continue
            
            # Enemy's turn
            if self.enemy.is_alive():
                print(f"\n{self.enemy.name}'s Turn:")
                self.enemy.attack(self.player)
        
        if not self.player.is_alive():
            print("You have been defeated!")
        else:
            print(f"You defeated {self.enemy.name}!")