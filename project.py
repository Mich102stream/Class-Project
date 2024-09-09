# Author: Done Entertainment
# Description: An abandoned space station RPG by Done Entertainment.

# Importing Libraries
import random
import time
import sys

# Game Variables

current_room = "Airlock"

Wrench = False
Helmet = False
Laser_Pistol = False
Armoured_Vest = False
Flashlight = False

# Player Stats

Player = {
    "Name": "Player",
    "Health": 100,
    "Attack": 50,
    "Defence": 20,
    "Inventory": []
}

# Character Stats

Character_1 = {
    "Name": "Ronan",
    "Health": 120,
    "Attack": 165,
    "Defence": 25,
    "Inventory": ["Laser Pistol", "Ammo", "Rations", "Credit Chip", "Wrench"],
    "Description": """a seasoned space marine, with a rugged, weathered face and a steely gaze"""
}

Character_2 = {
    "Name": "Julia",
    "Health": 120,
    "Attack": 60,
    "Defence": 25,
    "Inventory": ["Medpack", "Rations", "Wrench"],
    "Description": """a skilled engineer, with a sharp mind and a quick wit"""
}


Character_3 = {
    "Name": "Lee",
    "Health": 120,
    "Attack": 70,
    "Defence": 30,
    "Inventory": ["Laser Pistol", "Rations", "Helmet"],
    "Description": """a former soldier, with a strong build and a no-nonsense attitude"""
}


# Enemy Stats

Enemy_1 = {  
    "Name": "Patrick",
    "Health": 150,
    "Attack": 70,
    "Defence": 30,
    "Inventory": ["Keycard Fragment A", "Medpack"],
    "Description": """Patrick is a fearsome alien creature with sharp claws and a menacing presence."""
}

Enemy_2 = {
    "Name": "Tristan",
    "Health": 150,
    "Attack": 70,
    "Defence": 30,
    "Inventory": ["Keycard Fragment B", "Ammo", "Medpack"],
    "Description": """Tristan is a cunning alien with a slimy exterior and a venomous bite."""
}

Enemy_3 = {
    "Name": "Kyle",
    "Health": 150,
    "Attack": 70,
    "Defence": 30,
    "Inventory": ["Keycard Fragment C", "Medpack", "Rations"],
    "Description": """Kyle is a massive alien brute with thick armor and incredible strength."""
}

Enemy_Boss = {
    "Name": "Michael",
    "Health": 300,
    "Attack": 100,
    "Defence": 50,
    "Inventory": ["Alien Egg"],
    "Description": """Michael is the leader of the alien horde, towering over the others with a menacing presence."""
}

Space_station = {   # Space Station Layout
    "Airlock": {
        "Description": """The airlock consists of two heavy, reinforced doors, each a solid slab of metal with a network of deep rivets and reinforced joints. 
        The outer door is slightly ajar, creaking as it swings on its rusted hinges. 
        The inner door of the airlock is slightly closed, but its seals are visibly worn and cracked. 
        A large control panel is mounted beside the inner door, its once-digital display now shattered, the buttons and switches all unresponsive.""",
        "items": ["Helmet", "Medpack"],
        "enemies": [],
        "connections": ["Hallway", "Cargohold"]
    },
    "Hallway": {
        "Description": """The hallway of the abandoned space station stretches out in eerie silence. 
        Cables and wires hang loosely from open panels in the ceiling. 
        The walls, once pristine and white, are now stained with patches of blood and peeling paint.""",
        "items": ["Flashlight"],
        "enemies": [],
        "connections": ["Armoury", "Medbay", "Airlock","Canteen/Crew Quarters", "Control Room"]
    },
    "Cargohold": {
        "Description": """The cargohold is a dimly lit chamber that feels both vast and claustrophobic. 
        The space is filled with towering stacks of metal crates and containers, some secured with rusting chains, while others have toppled over, spilling their contents across the floor. 
        The crates are marked with faded labels and symbols from various worlds and corporations, now unreadable through layers of dust.""",
        "items": ["Wrench","Rations","Ammo","Armoured Vest"],
        "enemies": [Enemy_1],
        "connections": ["Airlock", "Armoury"]
    },
    "Armoury": {
        "Description": """The armoury of the abandoned space station is lined with rows of weapon racks, now mostly empty. 
        The walls are reinforced with thick, riveted steel plates, designed to contain any accidents or breaches.""",
        "items": ["Laser pistol", "Armoured Vest", "Helmet"],
        "enemies": [Enemy_2],
        "connections": ["Cargohold", "Hallway"]
    },
    "Medbay": {
        "Description": """The medbay, once a sterile environment, is now tainted by decay and neglect. 
        Rows of medical beds line the room, their sheets torn and discoloured, some with ancient bloodstains that have darkened to a rusty brown. 
        The air is thick with the smell of antiseptic mixed with the musty odour of decay.""",
        "items": ["Medpack", "Credit Chip"],
        "enemies": [],
        "connections": ["Hallway"]
    },
    "Canteen/Crew Quarters": {
        "Description": """The canteen, once bustling with life, is now eerily silent. 
        Metal tables and chairs are scattered haphazardly, some overturned as if left in a hurry. 
        The once-bright LED lights flicker weakly, casting long, eerie shadows across the room.""",
        "items": ["Rations", "Data Pad"],
        "enemies": [Enemy_3],
        "connections": ["Hallway"]
    },
    "Control Room": {
        "Description": """The control room is large, circular, and filled with rows of consoles and control panels that once managed the entire station's operations. 
        Now, these consoles are lifeless, their screens cracked or completely dark, covered in a thick layer of dust.""",
        "items": ["Alien Egg", "Golden Card"],
        "enemies": [Enemy_Boss],
        "connections": ["Hallway"],
        "Required Keycard": True
    }

}

def type_out(text, delay=0.01):  # types out the text
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 


def main_menu():  # main menu
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
        
def choose_character():  # choose a character
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
    print("\n")
    time.sleep(1)
    
    return Player

def display_player_stats():  # displays the player stats
    global Player
    type_out("Player Stats:")
    type_out("Name: " + Player["Name"])
    type_out("Health: " + str(Player["Health"]))
    type_out("Attack: " + str(Player["Attack"]))
    type_out("Defence: " + str(Player["Defence"]))
    type_out("Inventory: " + str(Player["Inventory"]))
    
    
def display_enemy_stats():  # displays the enemy stats
    global current_room
    if "enemies" in Space_station[current_room] and Space_station[current_room]["enemies"]:
        type_out("Enemies in the room:")
        for enemy in Space_station[current_room]["enemies"]:
            type_out("Name: " + enemy["Name"])
            type_out("Health: " + str(enemy["Health"]))
            type_out("Attack: " + str(enemy["Attack"]))
            type_out("Defence: " + str(enemy["Defence"]))
            type_out("Inventory: " + str(enemy["Inventory"]))
            print("\n")
    else:
        type_out("There are no enemies in this room.")
    
def display_current_map():  # displays the map of the space station
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

def reset_enemies():  # resets the enemies in the room
    if Enemy_1["Health"] == 150:
        Space_station["Airlock"]["enemies"].append(Enemy_1)
    else:
        pass
    if Enemy_2["Health"] == 150:
        Space_station["Armoury"]["enemies"].append(Enemy_2)
    else:
        pass
    if Enemy_3["Health"] == 150:
        Space_station["Canteen/Crew Quarters"]["enemies"].append(Enemy_3)
    else:
        pass
    if Enemy_Boss["Health"] == 300:
        Space_station["Control Room"]["enemies"].append(Enemy_Boss)
    else:
        pass


def is_player_dead():  # checks if the player is dead
    if Player["Health"] <= 0:
        type_out("You are dead.")
        return True
    else:
        return False

enemy_found = False

def is_enemy_dead():   # checks if the enemy is dead
    global enemy_found 
    if Enemy_1["Health"] <= 0 and Enemy_1 in Space_station[current_room]["enemies"]:  
        Player["Inventory"].extend(Enemy_1["Inventory"])
        Space_station[current_room]["enemies"].remove(Enemy_1)
        print(f"{Enemy_1['Name']} is dead and removed from the room.")
        enemy_found = False  
    elif Enemy_2["Health"] <= 0 and Enemy_2 in Space_station[current_room]["enemies"]:
        Player["Inventory"].extend(Enemy_2["Inventory"])
        Space_station[current_room]["enemies"].remove(Enemy_2)
        print(f"{Enemy_2['Name']} is dead and removed from the room.") 
        enemy_found = False  
    elif Enemy_3["Health"] <= 0 and Enemy_3 in Space_station[current_room]["enemies"]:
        Player["Inventory"].extend(Enemy_3["Inventory"])
        Space_station[current_room]["enemies"].remove(Enemy_3)
        print(f"{Enemy_3['Name']} is dead and removed from the room.")
        enemy_found = False  
    elif Enemy_Boss["Health"] <= 0 and Enemy_Boss in Space_station[current_room]["enemies"]:
        Player["Inventory"].extend(Enemy_Boss["Inventory"])
        Space_station[current_room]["enemies"].remove(Enemy_Boss)
        print(f"{Enemy_Boss['Name']} is dead and removed from the room.") 
        enemy_found = False  

def attack_enemy():
    enemy = Space_station[current_room]["enemies"]
    if not enemy:
        type_out("You need to search the room and find the enemy before attacking.")
        print("\n")
        return
    else: 
        for enemy in enemy:
            Player_attack = Player["Attack"] - enemy["Defence"]
            if Player_attack < 0:
                Player_attack = 0
            crit_chance = random.randint(1, 10)
            if crit_chance <= 3:  
                Player_attack *= 2  
                type_out("Player lands a critical hit!")
            enemy["Health"] -= Player_attack
            if enemy["Health"] < 0:
                enemy["Health"] = 0  # enemy health does not go below zero
            type_out("Player attacks enemy for " + str(Player_attack) + " damage.")
            is_enemy_dead()
            time.sleep(1)

def attack_player():   # enemy attacks player
    enemies = Space_station[current_room]["enemies"]
    if enemies and enemies[0]["Health"] > 0:  
        for enemy in enemies:
            Enemy_attack = enemy["Attack"] - Player["Defence"]
            if Enemy_attack < 0:
                Enemy_attack = 0
            Player["Health"] -= Enemy_attack
            type_out("Enemy " + enemy["Name"] + " attacks player for " + str(Enemy_attack) + " damage.")
            print("\n")
    else:
        is_enemy_dead()
    if is_player_dead():
        return
    time.sleep(1)

def search_room():   # search the room for items or enemies
    global current_room
    global enemy_found
    type_out("You search the room...")
    print("\n")
    search_result = random.randint(1, 10)
    if search_result <= 5:  
        if "enemies" in Space_station[current_room] and Space_station[current_room]["enemies"]:
            enemy_found = True
            type_out("You found an enemy!")
            print("\n")
            display_enemy_stats()
        else:
            type_out("There are no enemies here.")
            print("\n")
            return
    else:  
        if "items" in Space_station[current_room] and Space_station[current_room]["items"]:
            item = random.choice(Space_station[current_room]["items"])
            type_out("You found a " + item + ".")
            print("\n")
            Player["Inventory"].append(item)
            Space_station[current_room]["items"].remove(item)
        else:
            type_out("There are no items here.")
            print("\n")
            return


def move_to_room(new_room):  # move to a new room
    global current_room
    global Space_station
    
    room_aliases = {"crew": "Canteen/Crew Quarters"}
    new_room = room_aliases.get(new_room.lower(), new_room.title())
    
    # Debugging: Print the current room and its connections
    print(f"Current Room: {current_room}")
    print(f"Connections from {current_room}: {Space_station[current_room]['connections']}")
    
    if new_room in Space_station[current_room]["connections"]:
        current_room = new_room
        # reset_enemies()
        display_current_map()
        type_out("You move to " + new_room + ".")
        print("\n")
        type_out(Space_station[new_room]["Description"])
        print("\n")
    else:
        type_out("You can't move to " + new_room)
        print("\n")
        
    if current_room == "Control Room":
        # Debugging: Print the current inventory
        print("Current Inventory: " + str(Player["Inventory"]))
        
        has_keycard = "Control Room Keycard" in Player["Inventory"]
        
        # Debugging: Print the status of the keycard check
        print(f"Has Control Room Keycard: {has_keycard}")
        
        if has_keycard:   # checks if you have the keycard to enter the control room
            type_out("You enter the control room and find the enemy boss.")
            print("\n")
            time.sleep(1)
            display_enemy_stats()
        else:
            type_out("You need a keycard to enter the control room.")
            print("\n")

def you_win():          # win the game
    type_out("Congratulations! You have defeated the alien horde and saved the space station.")
    type_out("Credits: Done Entertainment - Michael Kay, Ronan Aked, Julia Nyobe, Lee Brown, Patrick Payne, Tristan Haydon and Kyle Middleton.")
    type_out("Thanks for playing!")
    sys.exit()
       
def start_game():     # start the game
    global Wrench, Helmet, Laser_Pistol, Armoured_Vest, Flashlight
    choose_character()  # choose a character
    display_current_map()   # type_outs the map of the space station X marking spot of player.
    display_player_stats()  # displays the player stats
    print("\n")
    type_out(f"""You are {Player["Name"]}  {Player["Description"]}, Your mission: uncover the truth behind the eerie silence and unravel the dark secrets that lie within. 
                 As you step into the station, a sense of foreboding fills the air, and you realize that you are not alone. 
                 Unknown dangers lurk around every corner, and the fate of the station, and perhaps even the entire galaxy, rests in your hands.""")  # Introduction / Mission Statement
    print("\n")
    print("\n")
    type_out("You Enter the Airlock.")
    print("\n")
    type_out(Space_station[current_room]["Description"])
    print("\n")
    time.sleep(1) # pauses for 1 second
    while True:  # game loop
        command = input("What would you like to do? (""move"", ""stats"", ""search"", ""use"", ""attack"", ""reload"", ""combine fragments"", ""quit"", ""help""): ").strip()  # command input
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
                new_room = input("Enter the room to move to (Armoury, Medbay, Airlock, Crew (Canteen / Crew Quarters), Control Room): ")
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
        elif command == "use":    # use an item from your inventory
            type_out("Inventory:")
            for i, item in enumerate(Player['Inventory'], 1):
                type_out(f"{i}. {item}")
            item_number = input("Enter the number of the item to use: ")
            item_number = int(item_number)
            if item_number > 0 and item_number <= len(Player['Inventory']):  # checks if the item number is valid
                    item = Player['Inventory'][item_number - 1]
                    Player['Inventory'].remove(item)
                    if item == "Medpack":
                        Player["Health"] += 100
                        type_out("You have used the medpack.")
                    elif item == "Laser Pistol (Loaded)" and Laser_Pistol == False:
                        Player["Attack"] += 20
                        Laser_Pistol = True
                        type_out("You have equipped the weapon.")
                    elif item == "Armoured Vest" and Armoured_Vest == False:
                        Player["Defence"] += 20
                        Armoured_Vest = True
                        type_out("You have equipped the armour.")
                    elif item == "Helmet" and Helmet == False:
                        Player["Defence"] += 5
                        Helmet = True
                        type_out("You have equipped the helmet.")
                    elif item == "Rations":
                        Player["Health"] += 20
                        type_out("You have eaten the rations.")
                    elif item == "Wrench" and Wrench == False:
                        Player["Attack"] += 10
                        Wrench = True
                        type_out("You have equipped the wrench.")
                    elif item == "Flashlight" and Flashlight == False:
                        type_out("The flashlight flickers to life, casting a beam of light into the darkness.")
                        Flashlight = True
                    elif item == "Key Fragment A":
                        type_out("Key Fragment A is a small, metallic shard with a series of intricate symbols etched into its surface.")
                    elif item == "Key Fragment B":
                        type_out("Key Fragment B is a small, metallic shard with a series of intricate symbols etched into its surface.")
                    elif item == "Key Fragment C":
                        type_out("Key Fragment C is a small, metallic shard with a series of intricate symbols etched into its surface.")
                    elif item == "Control Room Keycard":
                        type_out("You have used the keycard to enter the control room.")
                    elif item == "Ammo":
                        type_out("Try using the reload command to reload your weapon.")
                    elif item == "Credit Chip":
                        type_out("The credit chip is a small, metallic disc with a series of numbers etched into its surface.")
                    elif item == "Golden Card":
                        type_out("The golden card is a small, metallic disc with a series of numbers etched into its surface, and a golden sheen.")
                    elif item == "Data Pad":
                        type_out("The data pad is a small, handheld device with a touch screen display and a series of buttons.")
                        type_out("The screen flickers to life, displaying a series of symbols and numbers.")
                    elif item == "Alien Egg":
                        type_out("Alien Egg shakes and cracks open, revealing a strange creature that runs away.")
                        you_win()
                    else:
                        type_out("You can't use that item.")
            else:
                    type_out("Invalid item number.")
            print("\n")
        elif command == "attack":   # attack the enemy
            attack_enemy()
            if is_enemy_dead():
                type_out("Enemy is dead.")
            else:
                attack_player()
                if is_player_dead():
                    type_out("You are dead.")
                    break
        elif command == "reload":   # reload the weapon
            if "Ammo" in Player["Inventory"]:
                Player["Inventory"].remove("Ammo")
                if "Laser Pistol" in Player["Inventory"]:
                    Player["Inventory"].remove("Laser Pistol")
                else:
                    type_out("You don't have a Laser Pistol in your inventory.")
                Player["Inventory"].append("Laser Pistol (Loaded)")
                type_out("You have reloaded your weapon.")
            else:
                type_out("You don't have any ammo.")
        elif command == "combine": # combine keycard fragments
            print("Current Inventory: " + str(Player["Inventory"]))
            
            has_fragment_a = "Key Fragment A" in Player["Inventory"]  # checks if you have the keycard fragments
            has_fragment_b = "Key Fragment B" in Player["Inventory"]
            has_fragment_c = "Key Fragment C" in Player["Inventory"]
            
            print(f"Has Key Fragment A: {has_fragment_a}")  # Debugging: Print the status of the key fragments
            print(f"Has Key Fragment B: {has_fragment_b}")
            print(f"Has Key Fragment C: {has_fragment_c}")
            
            if has_fragment_a and has_fragment_b and has_fragment_c:   # checks if you have all keycard fragments
                type_out("You combine Key Fragment A, Key Fragment B, and Key Fragment C.")
                Player["Inventory"].remove("Key Fragment A")
                Player["Inventory"].remove("Key Fragment B")
                Player["Inventory"].remove("Key Fragment C")
                Player["Inventory"].append("Control Room Keycard")
            else:
                type_out("One or more items are not in your inventory.")
        elif command == "help":   # help command
            type_out("Commands:")
            type_out("move - Move to a new room.") 
            type_out("stats - Display player stats.")
            type_out("search - Search the room for items or enemies.")
            type_out("use - Use an item from your inventory.")
            type_out("attack - Attack the enemy.")
            type_out("reload - Reload your weapon.")
            type_out("combine fragments - Combine keycard fragments.")
            type_out("quit - Quit the game.")
            type_out("help - Display this help message.")
            print("\n")
        elif command == "check":   # check command
            display_enemy_stats()
        else:
            print("Invalid command.") # invalid command
            print("\n")
        

# runs the game    
main_menu()      # Starts the game with the main menu

# End of project.py

