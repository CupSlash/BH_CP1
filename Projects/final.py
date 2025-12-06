#BH 2nd final.py
#import random
import random
#Player_won = False
player_won = False

# def use_item(player, item):
def use_item(player, item):
#     player.warmth += item.warmth
    player.warmth += item.warmth
#     player.sanity += item.sanity
    player.sanity += item.sanity
#     player.health += item.health
    player.health += item.health

def prompt_use_item(player):
    item_choice = input("Your items are", player.inventory, "What would you like to use?")
#         if item_choice not in player.inventory:
    if item_choice not in player.inventory:
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
    enemy_health = enemy.health
    while True:
        enemy_move = random.randint(0, 5) + enemy.attack
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
            player.health -= enemy_move
        if player.health <= 0:
            return False
        if enemy_health <= 0:
            print("You have defeated the", enemy.name, "!")
            return True

         
# def fight_bosses(player):
#     print("Wild cubs appear from behind some rocks and you must enter combat!")
#     player_won = combat(player, cubs)
#     if (player_won):
#         prompt_use_item_or_continue(player)
#     else:
#         return player_won
#
#     print("You continue on your journey and reach a cave. As you approach, a mother bear appears and you must enter combat!")
#     player_won = combat(player, mother)
#     if (player_won):
#         prompt_use_item_or_continue(player)
#     else:
#         return player_won
#
#     print("You walk into the cave, searching for Jack. You find him! This gives your sanity a slight boost! A final enemy appears from around the corner and you enter combat!")
#     player.sanity += 5
#     player_won = combat(player, father)
#     return player_won


#items = {
#   Planar_ARCTIC_4D-12: {warmth: 25, sanity: 0, health: 0},
#   Radio: {warmth: 0, sanity: 25, health: 0}, 
#   Medkit: {warmth: 0, sanity: 0, health: 25}
#}

#Locations = {
#   Cove = {
#       enemy: random regular enemy,
#       item:random.items(),
#       Jack: False
#   }
#   Island = {
#       enemy: random regular enemy,
#       item:random.items(),
#       Jack: False
#   }
#   Beach = {
#       enemy: random regular enemy,
#       item:ramdom.items(),
#       Jack: False
#   }
#   Mines = {
#       enemy:random regular enemy,
#       item:random.items(),
#       Jack: False
#   }
#   Basin = {
#       enemy:random regular enemy,
#       item:random.items(),
#       Jack: False
#   }
#   Lake = {
#       enemy:random regular enemy,
#       item:random.items,
#       Jack: False
#   }
#   Mountain = {
#       enemy:random regular enemy,
#       item:random.items,
#       Jack: False
#   }
#   Peninsula = {
#       enemy:random regular enemy,
#       item:random.items(),
#       Jack: False
#   }
#   City = {
#       enemy: None,
#       item:random.items,
#       Jack: False
#   }
#}
#Jack_location = random.choice([locations.Cove, locations.Island, locations.Beach, locations.Mines, locations.Basin, locations.Lake, locations.Mountain, locations.Peninsula])
#Jack_location.Jack = True

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
    location: locations.City
#}
}

#regular_enemies = {
    #Fox = {
    #   Health:31,
    #   Attack:5
    #}
    #Musk_Ox = {
    #   Health:50,
    #   Attack:15
    #}
    #Walrus = {
    #   Health:80,
    #   Attack:30
    #}
#}

#boss_enemies = {
    #Cubs = {
    #   Health:50,
    #   Attack:15
    #}
    #Mother = {
    #   Health:80,
    #   Attack:30
    #}
    #Father = {
    #   Health:120,
    #   Attack:50}
#}



#print("Welcome to 'The Final Project: RPG'. Your name is John, and you're on a vacation to Baffin Island, Canada, with your best friend Jack. Unfortunately, you lost sight of Jack and must find him. The nine locations you may enter are The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")
#While True:
#   turn_choice = input("You are currently in", location, "your stats are", health, warmth, sanity, ".\n You can choose to leave (l), explore for Jack (e), or use an item (i)")
#   if turn choice == "l" 
#       location_choice = input(locations, "Where would you like to go?")
#       if location_choice != locations: 
#           print("That is not a location")
#       else: 
#           get location dictionary from locations
#           player_location = selected location dictionary
#           if player_location.enemy != None:
#              player_won_combat = combat(player, player_location.enemy)
#              if (!player_won_combat):
#                  break
#   elif turn choice == "e":
#       if player_location.Jack:
#           player_won = fight_bosses()
#           break
#       else:
#           print("Jack is not here.")
#   elif turn choice == "i" 
#       prompt_use_item(player)
#   else:
#       print("That is not an option.")
#   health += 5
#   Warmth -= 1
#   If Warmth <= 20, Sanity -= 1
#   If Health <= 20, Sanity -= 1
#   If Warmth >= 20, Sanity += 1
#   If Health >= 20, Sanity += 1
#   If Warmth <= 0, Health -= 1
#   If Sanity <= 0, Health -= 1
#   If Health == 0, break



# If player_won:
#   print("You beat the game! Congratulations!")
# else
#   print("You Died!")