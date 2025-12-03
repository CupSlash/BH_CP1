#BH 2nd final.py
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
#items = [Planar ARCTIC 4D-12, Radio, Medkit]
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
#If Jack_location == Island:
#   Jack = True
#If Jack_location == Beach:
#   Jack = True
#If Jack_location == Mines:
#   Jack = True
#If Jack_location == Basin:
#   Jack = True
#If Jack_location == Lake:
#   Jack = True
#If Jack_location == Mountain:
#   Jack = True
#If Jack_location == Peninsula:
#   Jack = True
#location = City
#inventory = []
#health = 100
#warmth = 100
#sanity = 100
#Game = True
#Combat = False
#Player_win = False
#print("Welcome to 'The Final Project: RPG' Your name is John, and you're on a vacation to Baffin Island, Canada with your best friend Jack. Unfortunately you lost sight of Jack and must find him. The 9 locations you may enter are The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")




#While game == True
#   turn_choice = input("You are currently in", location, "your stats are", health, warmth, sanity, ".\n You can choose to leave (l) or use an item (i)")
#   if turn choice == "l" location_choice = input(locations, "Where would you like to go?")
#       if location_choice != locations print(That is not a location)
#       else: 
#           if enemies in location choice != None 
#   elif turn choice == "i" item_choice = input("Your items are", inventory, "What would you like to use?")
#       if item_choice != inventory print("That item is not in your inventory.")
#       else: use item
#   else print("That is not an option.")

#   While combat == True 
#       enemy_move = random.randint(0, 5) + attack
#       user_move = input("your stats are", stats, ". Your available moves are stab, defend, and evade. What would you like to do?")
#       If user_move is stab enemy_health -= 30
#       Elif user_move is defend enemy_move -= attack boost and enemy_health -= random.randint(0, 3)
#       Elif user_move is evade evade_chance is random.randint(1, 2)
#       Else
#       If evade chance not 1 user_health -= enemy_move
#       If user_health = 0 game is false and combat is false
#       If enemy_health = 0 combat is false

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






#EXAMPLE DICTIONARY \|/
#           cell = {
#               "visited": False,
#               "walls": {
#                   "top": True,
#                   "bottom": True,
#                   "left": True,
#                   "right": True
#               }
#           }