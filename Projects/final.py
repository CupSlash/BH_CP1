#BH 2nd final.py
import random
player_won = False
def use_item(player, item):
    player["warmth"] += item["warmth"]
    player["sanity"] += item["sanity"]
    player["health"] += item["health"]
    player["inventory"].remove(item)
def prompt_use_item(player):
    if player["inventory"] == []:
        print("You have no items in your inventory.")
        return
    item_names = []
    for item in player["inventory"]:
        item_names.append(item['name'])
    item_choice = input(f"Your items are {', '.join(item_names)}. What would you like to use?")
    item = next((item for item in player["inventory"] if item['name'] == item_choice), None)
    if item is None:
        print("That item is not in your inventory.")
    else:
        use_item(player, item)
def prompt_use_item_or_continue(player):
    player_choice = input("Would you like to use an item (i), or continue looking for Jack (c)?")
    if player_choice == "i":
        prompt_use_item(player)
def combat(player, enemy):
    while True:   
        evade_chance = False
        enemy_move = random.randint(0, 5) + enemy["attack"]
        player_move = input(f"Your health is {player['health']} and the enemy's health is {enemy['health']}. Your available moves are stab, defend, and evade. What would you like to do?")
        if player_move == "stab": 
            enemy["health"] -= 30
            print("You stabbed the enemy and did 30 damage!")
        elif player_move == "defend":
            enemy_move -= enemy["attack"]
            enemy["health"] -= random.randint(0, 5)
            print("You defended against the enemy's attack and did some damage back!")
        elif player_move == "evade":
            evade_chance = random.choice([True, False])
        else:
            print("That isn't an option")
            continue
        if evade_chance:
            enemy_health -= random.randint(0,3)
            print("You evaded the enemy's attack and did some damage back!")
        else:
            player["health"]-= enemy_move
            print(f"The enemy did {enemy_move} damage to you.")
        if player["health"] <= 0:
            return False
        if enemy["health"] <= 0:
            print(f"You have defeated the {enemy['name']}!")
            return True
def fight_bosses(player, cubs, mother, father):
    print("Wild cubs appear from behind some rocks and you must enter combat!")
    player_won = combat(player, cubs)
    if (player_won):
        prompt_use_item_or_continue(player)
    else:
        return player_won
    print("You continue on your journey and reach a cave. As you approach, a mother bear appears and you must enter combat!")

    player_won = combat(player, mother)
    if (player_won):
        prompt_use_item_or_continue(player)

    else:
        return player_won
    print("You walk into the cave, searching for Jack. You find him! A final enemy appears from around the corner and you enter combat!")
    player_won = combat(player, father)
    return player_won
items = [
    {
        "name":"heater",
        "description":"a diesel heater that provides warmth in cold environments",
        "warmth": 30,
        "sanity": 2,
        "health": 2
    },
    {
        "name":"radio",
        "description":"a radio that allows you to contact others and boost your sanity temporarily",
        "warmth": 2, 
        "sanity": 30, 
        "health": 2
    },
    {
        "name":"medkit",
        "description":"a first aid kit that restores health when used",
        "warmth": 2, 
        "sanity": 2, 
        "health": 30
    }
]
regular_enemies = [
    {
        "name":"Fox",
        "health":31,
        "attack":5
    },
    {
        "name":"Musk Ox",
        "health":50,
        "attack":15
    },
    {
        "name":"Walrus",
        "health":80,
        "attack":30
    },
]
boss_enemies = [
    {
        "name": "Cubs",
        "health":50,
        "attack":15
    },
    {
        "name":"Mother",
        "health":80,
        "attack":30
    },
    {
        "name":"Father",
        "health":120,
        "attack":50
    }
]
locations = {
    "cove":{
        "name":"Cove",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "island":{
        "name":"Island",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "beach":{
        "name":"Beach",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "mines":{
        "name":"Mines",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "basin":{
        "name":"Basin",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "lake":{
        "name":"Lake",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "mountain":{
        "name":"Mountain",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "peninsula":{
        "name":"Peninsula",
        "enemy":random.choice(regular_enemies).copy(),
        "item":random.choice(items),
        "jack":False
    },
    "city":{
        "name":"City",
        "enemy":None,
        "item":random.choice(items),
        "jack":False
    }
}
location_dicts_without_city = list(locations.values())
location_dicts_without_city.remove(locations["city"])
jack_location = random.choice(location_dicts_without_city)
jack_location["jack"] = True
player = {
    "health": 100,
    "warmth": 100,
    "sanity": 100,
    "inventory": [],
    "location": locations["city"]
}
print(f"Welcome to 'The Final Project: RPG'. Your name is John, and you're on a vacation to Baffin Island, Canada, with your best friend Jack. Unfortunately, you lost sight of Jack and must find him. The nine locations you may enter are the City, Basin, Mines, Beach, Island, Cove, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies!")
while True:
    turn_choice = input(f"You are currently in the {player['location']['name']}. Your stats are health:{player['health']}, warmth:{player['warmth']}, sanity:{player['sanity']}. \n You can choose to leave (l), explore (e), or use an item (i):")
    if turn_choice == "l":
        location_choice = input(f"The available locations are {', '.join(locations.keys())}. Where would you like to go?")

        if location_choice not in locations:
            print("That is not an existing location.")
            continue
        new_location = locations[location_choice]
        player["location"] = new_location
        if new_location["enemy"] != None:
            new_location_enemy = new_location["enemy"]
            print(f"A wild {new_location_enemy['name']} appears!")
            player_won_combat = combat(player, new_location_enemy)
            if player_won_combat:
                new_location["enemy"] = None
            else:
                break
        if new_location["item"] != None:
            player["inventory"].append(new_location["item"])
            print(f"You found a {new_location['item']['name']} which is a {new_location['item']['description']}. It has been added to your inventory.")
            new_location["item"] = None
    elif turn_choice == "e":
        if player["location"] == jack_location:
            player_won = fight_bosses(player, boss_enemies[0], boss_enemies[1], boss_enemies[2])
            break
        else:
            print("Jack is not here.")
    elif turn_choice == "i":
        prompt_use_item(player)
    else:
        print("That is not an option")
    player["warmth"] -= 3
    player["sanity"] -= 2
    if player["health"] <= 90:
        player["health"] += 3
    if player["warmth"] <= 20:
        player["sanity"] -= 2
        player["health"] -= 1
    if player["health"] <= 20:
        player["sanity"] -= 2
    if player["warmth"] >= 20:
        player["sanity"] += 1
        player["health"] += 2
    if player["health"] >= 20:
        player["sanity"] += 2
        player["warmth"] += 1
    if player["warmth"] <= 0:
        player["health"] -= 3
        player["sanity"] -= 3
    if player["sanity"] <= 0:
        player["health"] -= 4
    if player["health"] == 0:
        break
if player_won:
    print("You beat the game! Congratulations!")
else:
    print("You died!")