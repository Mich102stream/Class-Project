import random
import time
import sys


# Game Variables

current_room = "Airlock"

# Player Stats

Player = {
    "Name": "Player",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}

Character_1 = {
    "Name": "Ronan",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}

Character_2 = {
    "Name": "Julia",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}


Character_3 = {
    "Name": "Lee",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}


# Enemy Stats

Enemy_1 = {
    "Name": "Patrick",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}

Enemy_2 = {
    "Name": "Tristan",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}

Enemy_3 = {
    "Name": "Kyle",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}

Enemy_Boss = {
    "Name": "Michael",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}

Space_station = {
    "Airlock": {
        "Description": "The airlock consists of two heavy, reinforced doors, each a solid slab of metal with a network of deep rivets and reinforced joints. The outer door is slightly ajar, creaking as it swings on its rusted hinges. The inner door of the airlock is slightly closed, but its seals are visibly worn and cracked. A large control panel is mounted beside the inner door, its once-digital display now shattered, the buttons and switches all unresponsive.",
        "items": ["test_item", "medpack"],
        "enemies": [Enemy_1],
        "connections": ["Hallway", "Cargohold"]
    },
    "Hallway": {
        "Description": "The hallway of the abandoned space station stretches out in eerie silence Cables and wires hang loosely from open panels in the ceiling. The walls, once pristine and white, are now stained with patches of blood and peeling paint.",
        "items": ["test_item"],
        "enemies": [],
        "connections": ["Armoury", "Medbay", "Airlock","Canteen/Crew Quarters", "Control Room"]
    },
    "Cargohold": {
        "Description": "The cargohold is dimly lit chamber that feels both vast and claustrophobic. The space is filled with towering stacks of metal crates and containers, some secured with rusting chains, while others have toppled over, spilling their contents across the floor. The crates are marked with faded labels and symbols from various worlds and corporations, now unreadable through layers of dust.",
        "items": ["test_item", "Keycard"],
        "enemies": [],
        "connections": ["Airlock", "Armoury"]
    },
    "Armoury": {
        "Description": "The armoury of the abandoned space station is lined with rows of weapon racks, now mostly empty. The walls are reinforced with thick, riveted steel plates, designed to contain any accidents or breaches.",
        "items": ["test_item"],
        "enemies": [Enemy_2],
        "connections": ["Cargohold", "Hallway"]
    },
    "Medbay": {
        "Description": "The medbay The once-sterile environment is now tainted by decay and neglect. rows of medical beds line the room, their sheets torn and discoloured, some with ancient bloodstains that have darkened to a rusty brown. the air is thick with the smell of antiseptic mixed with the musty odour of decay.",
        "items": ["test_item"],
        "enemies": [],
        "connections": ["Hallway"]
    },
    "Canteen/Crew Quarters": {
        "Description": "The canteen, once bustling with life, is now eerily silent. Metal tables and chairs are scattered haphazardly, some overturned as if left in a hurry. The once-bright LED lights flicker weakly, casting long, eerie shadows across the room.",
        "items": ["test_item"],
        "enemies": [Enemy_3],
        "connections": ["Hallway"]
    },
    "Control Room": {
        "Description": "The control room is large, circular, and filled with rows of consoles and control panels that once managed the entire stations operations. Now, these consoles are lifeless, their screens cracked or completely dark, covered in a thick layer of dust.",
        "items": ["test_item"],
        "enemies": [Enemy_Boss],
        "connections": ["Hallway"],
        "Requied Keycard": True
    }

}

def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 


def main_menu():
    type_out("Welcome to the Abandoned.")
    type_out("An abandoned space station RPG by Done Entertainment.")
    type_out("1. Start Game")
    type_out("2. Exit Game")
    choice = input("Enter choice (1, 2): ")
    if choice == "1":
        start_game()
    elif choice == "2":
        type_out("Goodbye!")
    else:
        type_out("Invalid choice.")
        main_menu()
        
def choose_character():
    global Player
    type_out("Choose a character:")
    type_out("1. " + Character_1["Name"])
    type_out("2. " + Character_2["Name"])
    type_out("3. " + Character_3["Name"])
    choice = input("Enter choice (1, 2, 3): ")
    if choice == "1":
        Player = Character_1
    elif choice == "2":
        Player = Character_2
    elif choice == "3":
        Player = Character_3
    else:
        type_out("Invalid choice.")
        choose_character()
        
    type_out("You have chosen " + Player["Name"] + ".")
    type_out("\n")
    time.sleep(1)
    
    return Player

def display_player_stats():
    global Player
    type_out("Player Stats:")
    type_out("Name: " + Player["Name"])
    type_out("Health: " + str(Player["Health"]))
    type_out("Attack: " + str(Player["Attack"]))
    type_out("Defence: " + str(Player["Defence"]))
    type_out("Inventory: " + str(Player["Inventory"]))
    
    
def display_enemy_stats():
    type_out("Enemy Stats:")
    type_out("Name: " + Enemy_1["Name"])
    type_out("Health: " + str(Enemy_1["Health"]))
    type_out("Attack: " + str(Enemy_1["Attack"]))
    type_out("Defence: " + str(Enemy_1["Defence"]))
    type_out("Inventory: " + str(Enemy_1["Inventory"]))
    
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
    type_out("Player attacks enemy for " + str(Player_attack) + " damage.")
    type_out("\n")
    time.sleep(1)
    
def attack_player():
    Enemy_attack = Enemy_1["Attack"] - Player["Defence"]
    if Enemy_attack < 0:
        Enemy_attack = 0
    Player["Health"] -= Enemy_attack
    type_out("Enemy attacks player for " + str(Enemy_attack) + " damage.")
    type_out("\n")
    time.sleep(1)

    
def is_player_dead():
    if Player["Health"] <= 0:
        return True
    else:
        return False
    
def is_enemy_dead():
    if Enemy_1["Health"] or Enemy_2["Health"] or Enemy_3["Health"] <= 0:
        return True
    else:
        return False
    

def search_room():
    global current_room
    type_out("You search the room.")
    type_out("\n")
    time.sleep(1)
    items = Space_station[current_room]["items"]
    enemies = Space_station[current_room]["enemies"]
    
    if items:
        for item in items:
            type_out("You find a " + item + ".")
            type_out("\n")
            Player["Inventory"].append(item)
            items.remove(item)
            type_out("Could be more things to find, keep searching.")
    else:
        type_out("You find nothing.")
        type_out("\n")
    
    if enemies:
        for enemy in enemies:
            type_out("You encounter an enemy: " + enemy["Name"] + ".")
            type_out("\n")
            enemies.remove(enemy)


def move_to_room(new_room):
    global current_room
    global Space_station
    new_room = new_room.capitalize()
    if new_room in Space_station[current_room]["connections"]:
        current_room = new_room
        display_current_map()
        type_out("You move to " + new_room + ".")
        print("\n")
        type_out(Space_station[new_room]["Description"])
    else:
        type_out("You can't move to " + new_room)
        type_out("\n")
        
    if current_room == "Control Room":
        if "Keycard" in Player["Inventory"]:   # checks if you have the keycard to enter the control room
            type_out("You enter the control room and find the enemy boss.")
            type_out("\n")
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
                    item = input("Enter the item to use: ")
                    if item in Player["Inventory"]:
                        type_out("You use the " + item + ".")
                        Player["Inventory"].remove(item)
                        if item == "medpack":
                            Player["Health"] = 100
                        elif item == "weapon":
                            Player["Attack"] = +20
                        else:
                            type_out("You can't use that item.")
                    else:
                        type_out("You don't have a " + item + ".")
                    type_out("\n")
                else:
                    print("Invalid command.")
                    print("\n")
        else:
            type_out("You need a keycard to enter the control room.")
            print("\n")
        
def start_game():     # start the game
    type_out("Welcome to Game")  # welcome message
    print("\n")
    choose_character()  # choose a character
    display_current_map()   # type_outs the map of the space station X marking spot of player.
    display_player_stats()  # displays the player stats
    type_out("You Enter the Airlock.")
    type_out(Space_station[current_room]["Description"])
    time.sleep(1)
    while True:
        command = input("What would you like to do? ")
        if command == "move":                                           # move to a new room command but checks which room you are in and connects too
            if current_room == "Airlock":
                new_room = input("Enter the room to move to (Cargohold, Hallway): ")
                move_to_room(new_room)
            elif current_room == "Cargohold":
                new_room = input("Enter the room to move to (Airlock, Armoury): ")
                move_to_room(new_room)
            elif current_room == "Armoury":
                new_room = input("Enter the room to move to (Cargohold, Hallway): ")
                move_to_room(new_room)
            elif current_room == "Hallway":
                new_room = input("Enter the room to move to (Armoury, Medbay, Airlock, Canteen/Crew Quarters, Control Room): ")
                move_to_room(new_room)
            elif current_room == "Medbay":
                new_room = input("Enter the room to move to (Hallway): ")
                move_to_room(new_room)
            elif current_room == "Canteen/Crew Quarters":
                new_room = input("Enter the room to move to (Hallway): ")
                move_to_room(new_room)
            elif current_room == "Control Room":
                new_room = input("Enter the room to move to (Hallway): ")
                move_to_room(new_room)
        elif command == "stats":  # display player stats
            display_player_stats()
        elif command == "quit":    # quit the game
            type_out("Thanks for playing!")
            break
        elif command == "search":  # search the room for items
            search_room()
        elif command == "use":    
            type_out(f"Inventory: {Player['Inventory']}")
            item = input("Enter the item to use: ").strip()
            if item in Player["Inventory"]:    
                type_out("You use the " + item + ".")
                Player["Inventory"].remove(item)
                if item == "medpack":
                    Player["Health"] = 100
                    type_out("You have used the medpack.")
                elif item == "weapon":
                    Player["Attack"] = +20
                    type_out("You have equipped the weapon.")
                else:
                    type_out("You can't use that item.")
            else:
                type_out("You don't have a " + item + ".")
            type_out("\n")
        elif command == "attack":   # attack the enemy
            attack_enemy()
            if is_enemy_dead():
                type_out("Enemy is dead.")
            else:
                attack_player()
                if is_player_dead():
                    type_out("You are dead.")
                    break
        else:
            print("Invalid command.")
            print("\n")
        

# runs the game    
main_menu()       

# End of project.py

