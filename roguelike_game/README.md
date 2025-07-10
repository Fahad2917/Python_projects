# Roguelike Dungeon Adventure Game

## 📜 Overview
This is a **text-based Roguelike Dungeon Adventure Game** where players navigate a randomly generated dungeon, encountering enemies, treasures, and special events. The goal is to reach the **dungeon exit** without dying.

## 🛠 Features
- **Object-Oriented Design**: Modular class-based implementation.
- **Turn-based Combat**: Attack enemies or use items strategically.
- **Inventory System**: Collect and use items like weapons, armor, and potions.
- **Randomized Events**: Encounter treasure chests, merchants, and puzzles.
- **Save & Load System**: Progress is automatically saved and can be resumed.
- **Dungeon Exploration**: Navigate through randomly generated rooms.

---
## 🎮 How to Play

### **1️⃣ Running the Game**
1. Open a terminal and navigate to the project folder:
   ```sh
   cd roguelike_game
   ```
2. Run the game using Python:
   ```sh
   python main.py
   ```

### **2️⃣ Game Flow**
- If a **saved game** exists, choose to continue or start fresh.
- Enter rooms, where you may encounter **enemies, items, or events**.
- Use the command prompts to **attack, use items, or flee**.
- Progress through the dungeon until you reach the **exit or die**.

### **3️⃣ Controls**
| Action       | Command |
|-------------|---------|
| Attack      | `1`     |
| Use Item    | `2`     |
| Flee Battle | `3`     |
| Pick Up Item | `yes` / `no` |
| Answer Riddle | Type answer |
| Buy from Merchant | `yes` / `no` |

---
## 🏰 Game Components
### **1️⃣ Player (`player.py`)**
- Tracks **HP, attack power, inventory, and gold**.
- Can **attack enemies, take damage, and use items**.

### **2️⃣ Dungeon (`dungeon.py`)**
- Generates **random rooms**.
- Allows players to **progress room by room**.

### **3️⃣ Enemy (`enemy.py`)**
- Randomly assigned **Goblin, Skeleton, Orc, or Dark Mage**.
- Has **HP and attack power**.

### **4️⃣ Item System (`item.py`)**
- Includes **Weapons, Armor, and Potions**.
- Items can **boost stats or heal HP**.

### **5️⃣ Events (`event.py`)**
- **Treasure chests** (gold, items, or traps)
- **Riddles** (correct answers give rewards)
- **Merchants** (buy items with gold)

### **6️⃣ Battle System (`battle.py`)**
- **Turn-based combat**.
- Player chooses to **attack, use an item, or flee**.

### **7️⃣ Save System (`save_system.py`)**
- **Automatically saves** game progress.
- Loads from the last save if available.

---
## 🔧 Requirements
- Python 3.x

---
## 🎯 Credits
- Developed by **[Your Name]** as part of a Python project.

---
### 🎮 Have fun exploring the dungeon! 🏹🔥

