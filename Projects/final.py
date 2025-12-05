#BH 2nd final.py
#import random
import random
health = 100
warmth = 100
sanity = 100
inventory = []
location = locations.City
#cubs_alive = True
cubs_alive = True
#mother_alive = True
mother_alive = True
#father_alive = True
father_alive = True
#Game = True
game = True
#Combat = False
combat = False
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

# def prompt_use_item_or_continue(player):
def prompt_use_item_or_continue(player):
#     user_choice = input("Would you like to use an item (i), or continue looking for Jack (c)")
    user_choice = input("would you like to use an item (i), or continue looking for Jack (c)?")
#     if user_choice == "i":
    if user_choice == "i":
#         item_choice = input("Your items are", player.inventory, "What would you like to use?")
        item_choice = input("Your items are", player.inventory, "What would you like to use?")
#         if item_choice not in player.inventory:
        if item_choice not in player.inventory:
#             print("That item is not in your inventory.")
            print("That item is not in your inventory.")
#         else:
        else:
#             use_item(player, item_choice)
            use_item(player, item_choice)

# def fight_cubs():
def fight_cubs():
    #     evade_chance = 3
    evade_chance = 3
    #     enemy_health = cub_health
    enemy_health = cubs.health
    #     While true:
    while True:
    #       print("You think you hear Jack in a cave, but suddenly, a group of small polar bears come running at you!")
        print("You think you hear Jack in a cave, but suddenly, a group of small polar bears come running at you!")
    #       enemy_move = random.randint(0, 5) + cub attack
        enemy_move = random.randint(0, 5) + cubs.attack
    #       user_move = input("your stats are", stats, ". Your available moves are stab, defend, and evade. What would you like to do?")
        user_move = input("your stats are", player, ". Your available moves are stab, defend, and evade. What would you like to do?")
    #       If user_move == stab
        if user_move == "stab": 
    #           enemy_health -= 30
            enemy_health -= 30
    #       Elif user_move == defend
        elif user_move == "defend":
    #           enemy_move -= attack boost and enemy_health -= random.randint(0, 3)
            enemy_move -= cubs.attack
            enemy_health -= random.randint(0, 3)
    #       Elif user_move == evade 
        elif user_move == "evade":
    #           evade_chance = random.randint(1, 2)
            evade_chance = random.randint(1, 2)
    #       Else:
        else:
    #           print("That isn't an option")
            print("That isn't an option")
    #       If evade chance != 1:
        if evade_chance != 1:
    #           user_health -= enemy_move
            user_health -= enemy_move
    #       If user_health <= 0:
            if user_health <= 0:
    #           return False
                return False
    #       If enemy_health <= 0:
            if enemy_health <= 0:
    #           print("You have defeated the cubs!")
                print("You have defeated the cubs!")
    #           return True
                return True

# def fight_mother():
def fight_mother():
#       While True:
    while True:
#           print("Before you can enter the cave you hear a loud rumbling and the mother bear appears! Get ready for combat!")
        print("Before you can enter the cave you hear a loud rumbling and the mother bear appears! Get ready for combat!")
#           evade_chance = 3
        evade_chance = 3
    #       enemy_health = mother_health
        enemy_health = mother.health
    #       enemy_move = random.randint(0, 5) + mother attack
        enemy_move = random.randint(0, 5) + mother.attack
    #       user_move = input("your stats are", stats, ". Your available moves are stab, defend, and evade. What would you like to do?")
        user_move = input("your stats are", stats, ". Your available moves are stab, defend, and evade. What would you like to do?")
    #       If user_move == stab 
        if user_move == "stab":
    #           enemy_health -= 30
                enemy_health -= 30
    #       Elif user_move == defend
        elif 
    #           enemy_move -= attack boost and enemy_health -= random.randint(0, 3)
    #       Elif user_move == evade 
    #           evade_chance = random.randint(1, 2)
    #       Else:
    #           print("That isn't an option")
    #       If evade chance != 1 
    #           user_health -= enemy_move
    #       If user_health <= 0:
    #           return False
    #       If enemy_health <= 0:
    #           print("You have defeated the mother bear!")
    #           return True

# def fight_father():
#       While True:
#           print("You walk into the cave, searching for Jack. You find him! This gives your sanity a slight boost! A final enemy appears from around the corner and you enter combat!")
    #       sanity += 5
    #       evade_chance = 3
    #       enemy_health = cub_health
    #       enemy_move = random.randint(0, 5) + cub attack
    #       user_move = input("your stats are", stats, ". Your available moves are stab, defend, and evade. What would you like to do?")
    #       If user_move == stab 
    #           enemy_health -= 30
    #       Elif user_move == defend
    #           enemy_move -= attack boost and enemy_health -= random.randint(0, 3)
    #       Elif user_move == evade 
    #           evade_chance = random.randint(1, 2)
    #       Else:
    #           print("That isn't an option")
    #       If evade chance != 1 
    #           user_health -= enemy_move
    #       If user_health <= 0:
    #           return False
    #       If enemy_health <= 0:
    #           return True

# def fight_bosses(player):
#     player_won = fight_cubs()
#     if (player_won):
#         prompt_use_item_or_continue(player)
#     else:
#         return player_won
#
#     player_won = fight_mother()
#     if (player_won):
#         prompt_use_item_or_continue(player)
#     else:
#         return player_won
#
#     player_won = fight_father()
#     return player_won


#player = {
player = {
#   health: 100,
    health: 100,
#   warmth: 100,
    warmth: 100,
#   sanity: 100
    sanity: 100,
#   inventory: []
    inventory: [],
#   location: locations.City
    location: locations.City
#}
}

#Random Enemies = {
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

#Final Bosses = {
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

#items = {
#   Planar_ARCTIC_4D-12: {warmth: 25, sanity: 0, health: 0},
#   Radio: {warmth: 0, sanity: 25, health: 0}, 
#   Medkit: {warmth: 0, sanity: 0, health: 25}
#}

#Locations = {
#   Cove = {
#       enemies:random.random_enemies(),
#       item:random.items(),
#       Jack: False
#   }
#   Island = {
#       enemies:random.random_enemies(),
#       item:random.items(),
#       Jack: False
#   }
#   Beach = {
#       enemies:random.random_enemies(),
#       item:ramdom.items(),
#       Jack: False
#   }
#   Mines = {
#       enemies:random.random_enemies(),
#       item:random.items(),
#       Jack: False
#   }
#   Basin = {
#       enemies:random.random_enemies(),
#       item:random.items(),
#       Jack: False
#   }
#   Lake = {
#       enemies:random.random_enemies(),
#       item:random.items,
#       Jack: False
#   }
#   Mountain = {
#       enemies:random.random_enemies(),
#       item:random.items,
#       Jack: False
#   }
#   Peninsula = {
#       enemies:random.random_enemies(),
#       item:random.items(),
#       Jack: False
#   }
#   City = {
#       item:random.items,
#       Jack: False
#   }
#}
#Jack_location = random.choice([locations.Cove, locations.Island, locations.Beach, locations.Mines, locations.Basin, locations.Lake, locations.Mountain, locations.Peninsula])
#Jack_location.Jack = True



#print("Welcome to 'The Final Project: RPG'. Your name is John, and you're on a vacation to Baffin Island, Canada, with your best friend Jack. Unfortunately, you lost sight of Jack and must find him. The nine locations you may enter are The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")
#While game:
#   turn_choice = input("You are currently in", location, "your stats are", health, warmth, sanity, ".\n You can choose to leave (l), explore for Jack (e), or use an item (i)")
#   if turn choice == "l" 
#       location_choice = input(locations, "Where would you like to go?")
#       if location_choice != locations: 
#           print("That is not a location")
#       else: 
#           user_location = location_choice
#           combat = True
#   elif turn choice == "e":
#       if user_location.Jack:
#           player_won = fight_bosses()
#           game = False
#       else:
#           print("Jack is not here.")
#   elif turn choice == "i" 
#       item_choice = input("Your items are", inventory, "What would you like to use?")
#       if item_choice != inventory 
#           print("That item is not in your inventory.")
#       else: 
#           use_item()
#   else:
#       print("That is not an option.")

#   While combat == True:
#       evade_chance = 3
#       enemy_health = enemy in user_location health
#       enemy_move = random.randint(0, 5) + enemy in user_location attack
#       user_move = input("your stats are", stats, ". Your available moves are stab, defend, and evade. What would you like to do?")
#       If user_move = stab 
#           enemy_health -= 30
#       Elif user_move = defend
#           enemy_move -= attack boost and enemy_health -= random.randint(0, 3)
#       Elif user_move is evade 
#           evade_chance = random.randint(1, 2)
#       Else:
#           print("That isn't an option")
#       If evade chance not 1 
#           user_health -= enemy_move
#       If user_health = 0:
#           combat = False
#           game = False 
#       If enemy_health = 0:
#           combat = False
#           enemy in user_location = False

#   Warmth -= 1
#   If Warmth <= 20, Sanity -= 1
#   If Health <= 20, Sanity -= 1
#   If Warmth >= 20, Sanity += 1
#   If Health >= 20, Sanity += 1
#   If Warmth <= 0, Health -= 1
#   If Sanity <= 0, Health -= 1
#   If Health == 0, Game = False



#If player_win == False:
#   print("You Died!")
#Elif player_wine == True:
#   print("You beat the game! Congratulations!")
#Else:
#   break