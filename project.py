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
    map_layout = ["Airlock", "Cargohold", "Armoury", "Hallway", "Medbay", "Canteen/Crew Quarters", "Control Room"]
    map = [" ", " ", " ", " ", " ", " ", " "]
    
    for i, room in enumerate(map_layout):
        if current_room == room:
            map[i] = "x"
    
    print("                ")
    print("                        Cargohold                                                                          ")
    print("                     ..:::::::::::::::         Airlock                                                      ")
    print("                     .-              -      -.........:                                              ")
    print("                     .-    " + map[1] + "          -......-   " + map[0] + "      :                                              ")
    print("                     .-              -      -:-::::::::       Medbay                                      ")
    print("                     .......:-::......       .+     .      =************=                            ")
    print("                            ::..             .+     .      .            =                            ")
    print("                            ::..             .+     .......:    " + map[4] + "        =                            ")
    print("                       .+---=++=----         .+     ........            =                            ")
    print("                       .-          :::::::::::+     .      .:::::::::::::                            ")
    print("                       .-   " + map[2] + "       :----------+     .                                                ")
    print("                       .------------       H .+ " + map[3] + "    .      .............:                            ")
    print("                        Armoury            A .+     .      -            +                            ")
    print("                                           L .+     :::::::*.      " + map[5] + "     +                            ")
    print("                                           L .+     :......-.           +                            ")
    print("                                           W .+     .      -            +                            ")
    print("                                           A .+     .      .............:                            ")
    print("                                           Y .-:+:-::     Canteen/Crew Quarters                                      ")
    print("                                                + :                                                  ")
    print("                                                + :                                                  ")
    print("                                          -.....-::.....-.                                           ")
    print("                                          =             =.                                           ")
    print("                                          =     " + map[6] + "        =.                                           ")
    print("                                          =             =.                                           ")
    print("                                          -.............-.                                           ")
    print("                                            Control Room")                                                  


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
    

def search_room():
    print("You search the room.")
    print("\n")
    time.sleep(1)
    items = {
        "Airlock": ["Keycard"],
        "Cargohold": ["Weapon"],
        "Armoury": ["Weapon"],
        "Medbay": ["Health Pack"],
        "Canteen/Crew Quarters": ["Health Pack"],
        "Control Room": ["Weapon"],
    }
    if current_room in items:
        found_items = items[current_room]
        for item in found_items:
            print("You find a " + item + ".")
            print("\n")
            Player["Inventory"].append(item)
    else:
        print("You find nothing.")
        print("\n")


def move_to_room(new_room):
    global current_room
    if new_room in Space_station[current_room]["connections"]:
        current_room = new_room
        display_current_map()
    else:
        print("You can't move to " + new_room)
        print("\n")
        
    if current_room == "Control Room":
        if "Keycard" in Player["Inventory"]:
            print("You enter the control room and find the enemy boss.")
            print("\n")
            time.sleep(1)
            while True:
                command = input("What would you like to do? ")
                if command == "attack":
                    attack_enemy()
                    if is_enemy_dead():
                        break
                    attack_player()
                    if is_player_dead():
                        break
                elif command == "use":
                    item = input("Enter the item to use: ").strip()
                    if item in Player["Inventory"]:
                        print("You use the " + item + ".")
                        Player["Inventory"].remove(item)
                        if item == "medpack":
                            Player["Health"] = 100
                        elif item == "weapon":
                            Player["Attack"] = +20
                        else:
                            print("You can't use that item.")
                    else:
                        print("You don't have a " + item + ".")
                    print("\n")
                else:
                    print("Invalid command.")
                    print("\n")
        else:
            print("You need a keycard to enter the control room.")
            print("\n")
        
def start_game():     # start the game
    print("Welcome to Game")  # welcome message
    print("\n")
    display_current_map()   # prints the map of the space station X marking spot of player.
    display_player_stats()  # displays the player stats
    time.sleep(1)
    while True:
        command = input("What would you like to do? ")
        if command == "move":                                           # move to a new room command but checks which room you are in and connects too
            if current_room == "Airlock":
                new_room = input("Enter the room to move to (Cargohold, Hallway): ").strip()
                move_to_room(new_room)
            elif current_room == "Cargohold":
                new_room = input("Enter the room to move to (Airlock, Armoury): ").strip()
                move_to_room(new_room)
            elif current_room == "Armoury":
                new_room = input("Enter the room to move to (Cargohold, Hallway): ").strip()
                move_to_room(new_room)
            elif current_room == "Hallway":
                new_room = input("Enter the room to move to (Armoury, Medbay, Airlock, Canteen/Crew Quarters, Control Room): ").strip()
                move_to_room(new_room)
            elif current_room == "Medbay":
                new_room = input("Enter the room to move to (Hallway): ").strip()
                move_to_room(new_room)
            elif current_room == "Canteen/Crew Quarters":
                new_room = input("Enter the room to move to (Hallway): ").strip()
                move_to_room(new_room)
            elif current_room == "Control Room":
                new_room = input("Enter the room to move to (Hallway): ").strip()
                move_to_room(new_room)
        elif command == "stats":  # display player stats
            display_player_stats()
        elif command == "quit":    # quit the game
            print("Thanks for playing!")
            break
        elif command == "search":  # search the room for items
            search_room()
        elif command == "use":    # allows you to use a item in inventory
            print(f"Inventory: {Player['Inventory']}")
            item = input("Enter the item to use: ").strip()
            if item in Player["Inventory"]:    # checks if item is in inventory
                print("You use the " + item + ".")
                Player["Inventory"].remove(item)
                if item == "medpack":
                    Player["Health"] = 100
                    print("You have used the medpack.")
                elif item == "weapon":
                    Player["Attack"] = +20
                    print("You have equipped the weapon.")
                else:
                    print("You can't use that item.")
            else:
                print("You don't have a " + item + ".")
            print("\n")
        else:
            print("Invalid command.")
            print("\n")       
        

# runs the game    
start_game()        

# End of project.py
