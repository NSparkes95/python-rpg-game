# Description: A simple text-based RPG game
# Name: Nicole Sparkes
# Date: 2025-01-09

import random
import json

# Player class
class Player:
    def __init__(self, name, health=100, attack=10, defense=5 ):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = {"Potion": 3} # Player starts with 3 potions

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - random.randint(-2,3) - enemy.defense) # Randomize damage
        enemy.health -= damage
        print(f"You attacked {enemy.name} and dealt {damage} damage!")

    def heal(self):
        if self.inventory["Potion"] > 0:
            self.health =min(100, self.health + 30)
            self.inventory["Potion"] -= 1
            print("You used a Potion and restored 30 health!")
        else:
            print("You have no Potions left!")
        
# Enemy Class
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def attack_enemy(self, enemy):
        damage = max(0, self.attack + random.randinit(-2, 3) - enemy.defense)
        enemy.health -= damage
        print(f"You attacked {enemy.name} and dealt {damage} damage!")
    
    def attack_player(self, player):
        damage = max(0, self.attack + random.randint(-2, 3) - player.defense)
        player.health -= damage
        print(f"{self.name} attacked you and dealt {damage} damage!")
    
# Game functions
def create_enemy():
    enemy_names = ["Goblin", "Orc", "Troll, Skeleton", "Witch"]
    name = random.choice(enemy_names)
    health = random.randint(30, 70)
    attack = random.randint(5, 10)
    defense = random.randint(3, 8)
    return Enemy(name,health, attack, defense)
    
def save_game(player):
    with open("save_file.json", "w") as file:
        json.dump(player.__dict__, file)
    print("Game saved!")
    
def load_game():
    try:
        with open("save_file.json", "r") as file:
            data = json.load(file)
            player = Player(
                name=data["name"],
                health=data["health"],
                attack=data["attack"],
                defense=data["defense"],
            )
            player.inventory = data["inventory"]
            print("Game loaded!")
            return player
    except FileNotFoundError:
        print("No saved game found.")
        return None
    
# Main Game Loop
def main():
    print("Welcome to the RPG Adventure Game!")

    # Load or Create New Game
    choice = input("Do you want to (1) Start a New Game or (2) Load Game?")
    if choice =="2":
        player - load_game()
        if not player:
            print("Starting a new game instead.")
            player_name = input("Enter your character's name: ")
            player = Player(player_name)
        else:
            player_name = input("Enter your character's name: ")
            player = Player(player_name)
            
    else:
        player_name = input("Enter your character's name: ")
        player = Player(player_name)
        
    # Game Begins
    while True:
        if player.health <= 0:
            print("You have been defeated!")
            break

        print("\nYour Stats:")
        print(f"Health: {player.health}")
        print(f"Invenotry: {player.inventory}")

        print("\nAn enemy approaches!")
        enemy= create_enemy()
        print(f"Enemy: {enemy.name} | Health: {enemy.health} | Attack: {enemy.attack} | Defense: {enemy.defense}")

        while enemy.health > 0:
            print("\nActions:")
            print("1. Attack")
            print("2. Heal")
            print("3. Check Health")
            print("4. Save and Quit")
            action = input("Choose an action: ")

            if action =="1":
                player.attack_enemy(enemy)
                if enemy.health > 0:
                    enemy.attack_player(player)
            elif action =="2":
                player.heal()
                if enemy.health > 0:
                    enemy.attack_player(player)
            elif action =="3":
                print(f"Your health: {player.health}")
                print(f"Enemy health: {enemy.health}")
            elif action =="4":
                save_game(player)
                print("Thanks for playing! Goodbye!")
                return
            else: 
                print("Invalid action. Try again.")
                
            if player.health <= 0:
                print("You have been defeated!")
                return
            
        print(f"You defeated the {enemy.name}!")

if __name__ == "__main__":
    main()