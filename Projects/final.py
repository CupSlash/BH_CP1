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
    player["sanity"] += items["sanity"]
#     player.health += item.health
    player["health"] += item["health"]

def prompt_use_item(player):
    item_choice = input(f"Your items are {player['inventory']}. What would you like to use?")
#         if item_choice not in player.inventory:
    if item_choice not in player["inventory"]:
#             print("That item is not in your inventory.")
        print("That item is not in your inventory.")
#         else:
    else:
#             use_item(player, item_choice)
        use_item(player, item_choice)

# def prompt_use_item_or_continue(player):
def prompt_use_item_or_continue(player):
#     player_choice = input("Would you like to use an item (i), or continue looking for Jack (c)")
    player_choice = input("would you like to use an item (i), or continue looking for Jack (c)?")
#     if player_choice == "i":
    if player_choice == "i":
#         prompt_use_item(player)
        prompt_use_item(player)

def combat(player, enemy):
    evade_chance = 3
    enemy_health = enemy["health"]
    while True:
        enemy_move = random.randint(0, 5) + enemy["attack"]
        player_move = input("your stats are", player, ". Your available moves are stab, defend, and evade. What would you like to do?")
        if player_move == "stab": 
            enemy_health -= 30
        elif player_move == "defend":
            enemy_move -= enemy.attack
            enemy_health -= random.randint(0, 3)
        elif player_move == "evade":
            evade_chance = random.randint(1, 2)
        else:
            print("That isn't an option")
        if evade_chance != 1:
            player["health"]-= enemy_move
        if player["health"] <= 0:
            return False
        if enemy_health <= 0:
            print("You have defeated the", enemy["name"], "!")
            return True

         
# def fight_bosses(player):
def fight_bosses(player):
#     print("Wild cubs appear from behind some rocks and you must enter combat!")
    print("Wild cubs appear from behind some rocks and you must enter combat!")
#     player_won = combat(player, cubs)
    player_won = combat(player, ["cubs"])
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
    player_won = combat(player, ["mother"])
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
    player_won = combat(player, ["father"])
#     return player_won
    return player_won


#items = {
items = {
#   Planar_ARCTIC_4D-12: {warmth: 25, sanity: 0, health: 0},
    "Planar_ARCTIC_4D-12": {"warmth": 25, "sanity": 0, "health": 0},
#   Radio: {warmth: 0, sanity: 25, health: 0}, 
    "Radio": {"warmth": 0, "sanity": 25, "health": 0},
#   Medkit: {warmth: 0, sanity: 0, health: 25}
    "Medkit": {"warmth": 0, "sanity": 0, "health": 25}
#}
}

#regular_enemies = {
regular_enemies = {
    #Fox = {
    "fox":{
    #   Health:31,
        "health":31,
    #   Attack:5
        "attack":5
    #}
    },
    #Musk_Ox = {
    "musk_ox":{
    #   Health:50,
        "health":50,
    #   Attack:15
        "attack":15
    #}
    },
    #Walrus = {
    "walrus":{
    #   Health:80,
        "health":80,
    #   Attack:30
        "attack":30
    #}
    },
#}
}

#boss_enemies = {
boss_enemies = {
    #Cubs = {
    "cubs":{
    #   Health:50,
    "health":50,
    #   Attack:15
    "attack":15
    #}
    },
    #Mother = {
    "mother":{
    #   Health:80,
    "health":80,
    #   Attack:30
    "attack":30
    #}
    },
    #Father = {
    "father":{
    #   Health:120,
    "health":120,
    #   Attack:50}
    "attack":50
#}
    }
}
#Locations = {
locations = {
#   Cove = {
    "cove":{
#       enemy: random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:random.items(),
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   Island = {
    "island":{
#       enemy: random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:random.items(),
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   Beach = {
    "beach":{
#       enemy: random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:ramdom.items(),
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   Mines = {
    "mines":{
#       enemy:random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:random.items(),
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   Basin = {
    "basin":{
#       enemy:random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:random.items(),
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   Lake = {
    "lake":{
#       enemy:random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:random.items,
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   Mountain = {
    "mountain":{
#       enemy:random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:random.items,
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   Peninsula = {
    "peninsula":{
#       enemy:random regular enemy,
        "enemy":random.choice(list(regular_enemies.keys())),
#       item:random.items(),
        "item":random.choice(list(items.keys())),
#       Jack: False
        "jack":False
#   }
    },
#   City = {
    "city":{
#       enemy: None,
        "enemy":None,
#       item:random.items,
        "item":random.choice(list(items.keys())),
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
    "location": "city"
#}
}



#print("Welcome to 'The Final Project: RPG'. Your name is John, and you're on a vacation to Baffin Island, Canada, with your best friend Jack. Unfortunately, you lost sight of Jack and must find him. The nine locations you may enter are The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")
print("Welcome to 'The Final Project: RPG'. Your name is John, and you're on a vacation to Baffin Island, Canada, with your best friend Jack. Unfortunately, you lost sight of Jack and must find him. The nine locations you may enter The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")
#While True:
while True:
#   turn_choice = input("You are currently in", location, "your stats are", health, warmth, sanity, ".\n You can choose to leave (l), explore for Jack (e), or use an item (i)")
    turn_choice = input(f"You are currently in the {player['location']} your stats are health:{player['health']}, warmth:{player['warmth']}, sanity:{player['sanity']}. \n You can choose to leave (l), explore (e), or use an item (i):")
#   if turn choice == "l":
    if turn_choice == "l":
#       location_choice = input(locations, "Where would you like to go?")
        location_choice = input(f"The available locations are cove, island, beach, mines, basin, lake, mountain, peninsula, and city. Where would you like to go?")
        if location_choice == "cove":
#           player_location = selected location dictionary
            player["location"] = location_choice
            if ["enemy"] in "cove":
                combat(player, "location"["enemy"])
                del "location"["enemy"]
            if ["location"]("item") != None:---
                ["inventory"].append("item"["location"])
                del "location"["item"]
        elif location_choice == "island":
            player["location"] = location_choice
        elif location_choice == "beach":
            player["location"] = location_choice
        elif location_choice == "mines":
            player["location"] = location_choice
        elif location_choice == "basin":
            player["location"] = location_choice
        elif location_choice == "lake":
            player["location"] = location_choice
        elif location_choice == "mountain":
            player["location"] = location_choice
        elif location_choice == "peninsula":
            player["location"] = location_choice
        elif location_choice == "city":
            player["location"] = location_choice
        else:
            print("that is not an existing location.")


#           if player_location.enemy != None:
#              player_won_combat = combat(player, player_location.enemy)
#              if (!player_won_combat):
#                  break
#   elif turn choice == "e":
    elif turn_choice == "e":
#       if player_location.Jack:
        if "location" == jack_location:
#           player_won = fight_bosses()
            player_won = fight_bosses()
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
