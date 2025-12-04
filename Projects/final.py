#BH 2nd final.py
#cubs_alive = True
#mother_alive = True
#father_alive = True
#import random
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
#   Planar_ARCTIC_4D-12:warmth += 25,
#   Radio:sanity +=25, 
#   Medkit:health +=25
#}
#Locations = {
#   Cove = {
#       enemies:random.random_enemies(),
#       items:random.items(),
#       Jack: False
#   }
#   Island = {
#       enemies:random.random_enemies(),
#       items:random.items(),
#       Jack: False
#   }
#   Beach = {
#       enemies:random.random_enemies(),
#       items:ramdom.items(),
#       Jack: False
#   }
#   Mines = {
#       enemies:random.random_enemies(),
#       items:random.items(),
#       Jack: False
#   }
#   Basin = {
#       enemies:random.random_enemies(),
#       items:random.items(),
#       Jack: False
#   }
#   Lake = {
#       enemies:random.random_enemies(),
#       items:random.items,
#       Jack: False
#   }
#   Mountain = {
#       enemies:random.random_enemies(),
#       items:random.items,
#       Jack: False
#   }
#   Peninsula = {
#       enemies:random.random_enemies(),
#       items:random.items(),
#       Jack: False
#   }
#   City = {
#       items:random.items,
#       Jack: False
#   }
#}
#Jack_location = random.locations(Cove, Island, Beach, Mines, Basin, Lake, Mountain, Peninsula)
#If Jack_location == Cove:
#   Jack = True
#elif Jack_location == Island:
#   Jack = True
#elif Jack_location == Beach:
#   Jack = True
#elif Jack_location == Mines:
#   Jack = True
#elif Jack_location == Basin:
#   Jack = True
#elif Jack_location == Lake:
#   Jack = True
#elif Jack_location == Mountain:
#   Jack = True
#else:
#   Jack = True
#user_location = City
#inventory = []
#health = 100
#warmth = 100
#sanity = 100
#Game = True
#Combat = False
#Player_win = False
#print("Welcome to 'The Final Project: RPG' Your name is John, and you're on a vacation to Baffin Island, Canada with your best friend Jack. Unfortunately you lost sight of Jack and must find him. The 9 locations you may enter are The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")




#While game == True:
#   turn_choice = input("You are currently in", location, "your stats are", health, warmth, sanity, ".\n You can choose to leave (l), explore for Jack (e), or use an item (i)")
#   if turn choice == "l" 
#       location_choice = input(locations, "Where would you like to go?")
#       if location_choice != locations:
#           print(That is not a location)
#       else: 
#           user_location = location_choice
#           combat = True
#   elif turn choice == "e":
#       if Jack in user_location = True:
#           Boss_fight = True
#       else:
#           print("Jack is not here.")
#   elif turn choice == "i" 
#       item_choice = input("Your items are", inventory, "What would you like to use?")
#       if item_choice != inventory 
#           print("That item is not in your inventory.")
#       else: 
#           use item
#   else:
#       print("That is not an option.")

#   While Boss_fight == True:
#       While cubs_alive == True:
    #       print("You think you hear Jack in a cave, but suddenly, a group of small polar bears come running at you!")
    #       evade_chance = 3
    #       enemy_health = cub_health
    #       enemy_move = random.randint(0, 5) + cub attack
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
    #           Boss_fight = False
    #           game = False 
    #       If enemy_health = 0:
    #           cubs_alive = False
#       user_choice = ("You've defeated the cubs! Your stats are", stats, "Would you like to use an item (i), or continue looking for Jack (c)")
#       if user_choice = "i":
#           item_choice = input("Your items are", inventory, "What would you like to use?")
#           if item_choice != inventory 
#               print("That item is not in your inventory.")
#           else: 
#               use item
#       else:
#           continue
#       While mother_alive == True:
#           print("Before you can enter the cave you hear a loud rumbling and the mother bear appears! Get ready for combat!")
#           evade_chance = 3
    #       enemy_health = mother_health
    #       enemy_move = random.randint(0, 5) + mother attack
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
    #           Boss_fight = False
    #           game = False 
    #       If enemy_health = 0:
    #           mother_alive = False
#       user_choice = ("You've defeated the mother bear! Your stats are", stats, "Would you like to use an item (i), or continue looking for Jack (c)")
#       if user_choice = "i":
#           item_choice = input("Your items are", inventory, "What would you like to use?")
#           if item_choice != inventory 
#               print("That item is not in your inventory.")
#           else: 
#               use item
#       else:
#           continue
#       While father_alive == True:
    #       print("You walk into the cave, searching for Jack. You find him! This gives your sanity a slight boost! A final enemy appears from around the corner and you enter combat!")
    #       sanity += 5
    #       evade_chance = 3
    #       enemy_health = cub_health
    #       enemy_move = random.randint(0, 5) + cub attack
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
    #           Boss_fight = False
    #           game = False 
    #       If enemy_health = 0:
    #           cubs_alive = False

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

#   If polar bears are dead, Game is false and Player Win is True
#   Elif user health hits zero then game is false
#   Else continue     




#If player_win = False:
#   print("You Died!")
#Else:
#   print("You beat the game! Congratulations!")