import random
import time



# Player Stats

Player = {
    "Name": "Player",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}

Character_1 = {
    "Name": "Player",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}

Character_2 = {
    "Name": "Player",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}


Character_3 = {
    "Name": "Player",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}


# Enemy Stats

Enemy_1 = {
    "Name": "Enemy",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}

Enemy_2 = {
    "Name": "Enemy",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}

Enemy_3 = {
    "Name": "Enemy",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}

Enemy_Boss = {
    "Name": "Enemy Boss",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Coins": 0,
    "Inventory": []
}


Space_station = {
    "Airlock": {
        "Description": "You are in the airlock. You can go to the hallway or the cargohold.",
        "items": [""],
        "enemies": [""],
        "connections": ["Hallway", "Cargohold"]
    },
    "Hallway": {
        "Description": "You are in the hallway. You can go to the control room, medbay or the airlock.",
        "items": [""],
        "enemies": [""],
        "connections": ["Armoury", "Medbay", "Airlock","Canteen/Crew Quarters", "Control Room"]
    },
    "Cargohold": {
        "Description": "You are in the cargohold. You can go to the airlock or the armoury.",
        "items": [""],
        "enemies": [""],
        "connections": ["Airlock", "Armoury"]
    },
    "Armoury": {
        "Description": "You are in the armoury. You can go to the cargohold or the hallway.",
        "items": [""],
        "enemies": [""],
        "connections": ["Cargohold", "Hallway"]
    },
    "Medbay": {
        "Description": "You are in the medbay. You can go to the hallway.",
        "items": [""],
        "enemies": [""],
        "connections": ["Hallway"]
    },
    "Canteen/Crew Quarters": {
        "Description": "You are in the canteen/crew quarters. You can go to the hallway.",
        "items": [""],
        "enemies": [""],
        "connections": ["Hallway"]
    },
    "Control Room": {
        "Description": "You are in the control room. You can go to the hallway.",
        "items": [""],
        "enemies": [""],
        "connections": ["Hallway"],
        "Requied Keycard": True
    }

}

current_room = "Airlock"

def display_player_stats():
    print("Player Stats:")
    print("Name: " + Player["Name"])
    print("Health: " + str(Player["Health"]))
    print("Attack: " + str(Player["Attack"]))
    print("Defence: " + str(Player["Defence"]))
    print("Coins: " + str(Player["Coins"]))
    print("Inventory: " + str(Player["Inventory"]))
    
    
def display_enemy_stats():
    print("Enemy Stats:")
    print("Name: " + Enemy_1["Name"])
    print("Health: " + str(Enemy_1["Health"]))
    print("Attack: " + str(Enemy_1["Attack"]))
    print("Defence: " + str(Enemy_1["Defence"]))
    print("Coins: " + str(Enemy_1["Coins"]))
    print("Inventory: " + str(Enemy_1["Inventory"]))
    
def display_current_map():
    print("Current Room: " + current_room)
    print(Space_station[current_room]["Description"])


def attack_enemy():
    Player_attack = Player["Attack"] - Enemy_1["Defence"]
    if Player_attack < 0:
        Player_attack = 0
    Enemy_1["Health"] -= Player_attack
    print("Player attacks enemy for " + str(Player_attack) + " damage.")
    print("\n")
    time.sleep(1)
    
def attack_player():
    Enemy_attack = Enemy_1["Attack"] - Player["Defence"]
    if Enemy_attack < 0:
        Enemy_attack = 0
    Player["Health"] -= Enemy_attack
    print("Enemy attacks player for " + str(Enemy_attack) + " damage.")
    print("\n")
    time.sleep(1)

    
def is_player_dead():
    if Player["health"] <= 0:
        print("You are dead")
        return True
    else:
        return False
    
def is_enemy_dead():
    if Enemy_1["health"] or Enemy_2["health"] or Enemy_3["health"] <= 0:
        print("Enemy is dead")
        return True
    else:
        return False
    

