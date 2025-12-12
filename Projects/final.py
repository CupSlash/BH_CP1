#BH 2nd final.py
#import random
import random
#Player_won = False
player_won = False

# def use_item(player, item):
def use_item(player, item):
#     player.warmth += item.warmth
    player["warmth"] += item["warmth"]
#     player.sanity += item.sanity
    player["sanity"] += item["sanity"]
#     player.health += item.health
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

    # Find first item in inventory with matching name
    item = next((item for item in player["inventory"] if item['name'] == item_choice), None)

#         if item_choice not in player.inventory:
    if item is None:
#             print("That item is not in your inventory.")
        print("That item is not in your inventory.")
#         else:
    else:
#             use_item(player, item_choice)
        use_item(player, item)

# def prompt_use_item_or_continue(player):
def prompt_use_item_or_continue(player):
#     player_choice = input("Would you like to use an item (i), or continue looking for Jack (c)")
    player_choice = input("Would you like to use an item (i), or continue looking for Jack (c)?")
#     if player_choice == "i":
    if player_choice == "i":
#         prompt_use_item(player)
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
            print("You evaded the enemy's attack!")
        else:
            player["health"]-= enemy_move
            print(f"The enemy did {enemy_move} damage to you.")
        if player["health"] <= 0:
            return False
        if enemy["health"] <= 0:
            print(f"You have defeated the {enemy['name']}!")
            return True

         
# def fight_bosses(player):
def fight_bosses(player, cubs, mother, father):
#     print("Wild cubs appear from behind some rocks and you must enter combat!")
    print("Wild cubs appear from behind some rocks and you must enter combat!")
#     player_won = combat(player, cubs)
    player_won = combat(player, cubs)
#     if (player_won):
    if (player_won):
#         prompt_use_item_or_continue(player)
        prompt_use_item_or_continue(player)
#     else:
    else:
#         return player_won
        return player_won
#
#     print("You continue on your journey and reach a cave. As you approach, a mother bear appears and you must enter combat!")
    print("You continue on your journey and reach a cave. As you approach, a mother bear appears and you must enter combat!")
#     player_won = combat(player, mother)
    player_won = combat(player, mother)
#     if (player_won):
    if (player_won):
#         prompt_use_item_or_continue(player)
        prompt_use_item_or_continue(player)
#     else:
    else:
#         return player_won
        return player_won
#
#     print("You walk into the cave, searching for Jack. You find him! This gives your sanity a slight boost! A final enemy appears from around the corner and you enter combat!")
    print("You walk into the cave, searching for Jack. You find him! A final enemy appears from around the corner and you enter combat!")
#     player_won = combat(player, father)
    player_won = combat(player, father)
#     return player_won
    return player_won


#items = {
items = [
#   Planar_ARCTIC_4D-12: {warmth: 25, sanity: 0, health: 0},
    {
        "name":"Planar ARCTIC 4D-12",
        "description":"a diesel heater that provides warmth in cold environments",
        "warmth": 25,
        "sanity": 0,
        "health": 0
    },
#   Radio: {warmth: 0, sanity: 25, health: 0}, 
    {
        "name":"Radio",
        "description":"a radio that allows you to contact others and boost your sanity temporarily",
        "warmth": 0, 
        "sanity": 25, 
        "health": 0
    },
#   Medkit: {warmth: 0, sanity: 0, health: 25}
    {
        "name":"Medkit",
        "description":"a first aid kit that restores health when used",
        "warmth": 0, 
        "sanity": 0, 
        "health": 25
    }
#}
]

#regular_enemies = {
regular_enemies = [
    #Fox = {
    {
        "name":"Fox",
    #   Health:31,
        "health":31,
    #   Attack:5
        "attack":5
    #}
    },
    #Musk_Ox = {
    {
        "name":"Musk Ox",
    #   Health:50,
        "health":50,
    #   Attack:15
        "attack":15
    #}
    },
    #Walrus = {
    {
        "name":"Walrus",
    #   Health:80,
        "health":80,
    #   Attack:30
        "attack":30
    #}
    },
#}
]

#boss_enemies = {
boss_enemies = [
    #Cubs = {
    {
        "name": "Cubs",
        #   Health:50,
        "health":50,
        #   Attack:15
        "attack":15
        #}
    },
    #Mother = {
    {
        "name":"Mother",
        #   Health:80,
        "health":80,
        #   Attack:30
        "attack":30
        #}
    },
    #Father = {
    {
        "name":"Father",
        #   Health:120,
        "health":120,
        #   Attack:50}
        "attack":50
    #}
    }
]
#Locations = {
locations = {
#   Cove = {
    "cove":{
        "name":"Cove",
#       enemy: random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:random.items(),
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   Island = {
    "island":{
        "name":"Island",
#       enemy: random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:random.items(),
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   Beach = {
    "beach":{
        "name":"Beach",
#       enemy: random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:ramdom.items(),
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   Mines = {
    "mines":{
        "name":"Mines",
#       enemy:random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:random.items(),
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   Basin = {
    "basin":{
        "name":"Basin",
#       enemy:random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:random.items(),
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   Lake = {
    "lake":{
        "name":"Lake",
#       enemy:random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:random.items,
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   Mountain = {
    "mountain":{
        "name":"Mountain",
#       enemy:random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:random.items,
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   Peninsula = {
    "peninsula":{
        "name":"Peninsula",
#       enemy:random regular enemy,
        "enemy":random.choice(regular_enemies).copy(),
#       item:random.items(),
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    },
#   City = {
    "city":{
        "name":"City",
#       enemy: None,
        "enemy":None,
#       item:random.items,
        "item":random.choice(items),
#       Jack: False
        "jack":False
#   }
    }
#}
}
#Jack_location = random.choice([locations.Cove, locations.Island, locations.Beach, locations.Mines, locations.Basin, locations.Lake, locations.Mountain, locations.Peninsula])
location_dicts_without_city = list(locations.values())
location_dicts_without_city.remove(locations["city"])
jack_location = random.choice(location_dicts_without_city)
jack_location["jack"] = True

#player = {
player = {
#   health: 100,
    "health": 100,
#   warmth: 100,
    "warmth": 100,
#   sanity: 100
    "sanity": 100,
#   inventory: []
    "inventory": [],
#   location: locations.City
    "location": locations["city"]
#}
}



#print("Welcome to 'The Final Project: RPG'. Your name is John, and you're on a vacation to Baffin Island, Canada, with your best friend Jack. Unfortunately, you lost sight of Jack and must find him. The nine locations you may enter are The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")
print(f"Welcome to 'The Final Project: RPG'. Your name is John, and you're on a vacation to Baffin Island, Canada, with your best friend Jack. Unfortunately, you lost sight of Jack and must find him. The nine locations you may enter are the City, Basin, Mines, Beach, Island, Cove, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies!")
#While True:
while True:
#   turn_choice = input("You are currently in", location, "your stats are", health, warmth, sanity, ".\n You can choose to leave (l), explore for Jack (e), or use an item (i)")
    turn_choice = input(f"You are currently in the {player['location']['name']}. Your stats are health:{player['health']}, warmth:{player['warmth']}, sanity:{player['sanity']}. \n You can choose to leave (l), explore (e), or use an item (i):")
#   if turn choice == "l":
    if turn_choice == "l":
#       location_choice = input(locations, "Where would you like to go?")
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
            if not player_won_combat:
                break
        if new_location["item"] != None:
            player["inventory"].append(new_location["item"])
            print(f"You found a {new_location['item']['name']} which is a {new_location['item']['description']}. It has been added to your inventory.")
            new_location["item"] = None


#           if player_location.enemy != None:
#              player_won_combat = combat(player, player_location.enemy)
#              if (!player_won_combat):
#                  break
#   elif turn choice == "e":
    elif turn_choice == "e":
#       if player_location.Jack:
        if player["location"] == jack_location:
#           player_won = fight_bosses()
            player_won = fight_bosses(player, boss_enemies[0], boss_enemies[1], boss_enemies[2])
#           break
            break
#       else:
        else:
#           print("Jack is not here.")
            print("Jack is not here.")
#   elif turn choice == "i" 
    elif turn_choice == "i":
#       prompt_use_item(player)
        prompt_use_item(player)
#   else:
    else:
#       print("That is not an option.")
        print("That is not an option")
#   health += 5
    player["health"] += 5
#   Warmth -= 1
    player["warmth"] -= 1
#   If Warmth <= 20, Sanity -= 1
    if player["warmth"] <= 20:
        player["sanity"] -= 1
#   If Health <= 20, Sanity -= 1
    if player["health"] <= 20:
        player["sanity"] -= 1
#   If Warmth >= 20, Sanity += 1
    if player["warmth"] >= 20:
        player["sanity"] += 1
#   If Health >= 20, Sanity += 1
    if player["health"] >= 20:
        player["sanity"] += 1
#   If Warmth <= 0, Health -= 1
    if player["warmth"] <= 0:
        player["health"] -= 1
#   If Sanity <= 0, Health -= 1
    if player["sanity"] <= 0:
        player["health"] -= 1
#   If Health == 0, break
    if player["health"] == 0:
        break



# If player_won:
if player_won:
#   print("You beat the game! Congratulations!")
    print("You beat the game! Congratulations!")
# else
else:
#   print("You Died!")
    print("You died!")
