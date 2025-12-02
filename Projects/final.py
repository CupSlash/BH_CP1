#BH 2nd final.py
#import random
#Define Fox
#Define Musk Ox
#Define Walrus
#Define Cubs
#Define Mother
#Define Father
#Define Enemy Factor
#Define Planar ARCTIC 4D-12
#Define Radio
#Define Medkit
#Define Item Factor
#Define Jack Location
#Locations = {
#   "Cove" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "Island" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "Beach" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "Mines" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "Basin" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "Lake" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "Mountain" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "Peninsula" = {
#       "enemies": Enemy Factor,
#       "items": Item Factor,
#       Jack: False
#   }
#   "City" = {
#       "items": Item Factor
#   }
#}
#Set player location to city
#Set player items list
#Set user health to 100, warmth to 100, and sanity to 100.
#Game is True, Player win is False, Combat is False,
#print("Welcome to 'The Final Project: RPG' Your name is John, and you're on a vacation to Baffin Island, Canada with your best friend Jack. Unfortunately you lost sight of Jack and must find him. The 9 locations you may enter are The City, Basin, Mines, Beach, Island, Cover, Bay, Lake, Mountain, and Peninsula. On your journey you must manage sanity, warmth, and health in order to survive. Enjoy the adventure and watch out for enemies! + 1 Knife")



#While game is true
#   turn_choice = input("You are currently in", location, "your stats are", health, warmth, sanity, ".\n You can choose to leave (l) or use an item (i)")
#   if turn choice == "l" location_choice = input(locations, "Where would you like to go?")
#       if location_choice != locations print(That is not a location)
#       else: 
#           if "enemies" in location choice != None 
#   elif turn choice == "i" item_choice = input("Your items are", inventory, "What would you like to use?")
#       if item_choice != inventory print("That item is not in your inventory.")
#       else: use item
#   else print("That is not an option.")

#   While combat is true
#       enemy_move = random.randint(0, 5) + attack boost
#       user_move = input("your stats are", stats, ". Your available moves are stab, defend, and evade. What would you like to do?")
#       If user_move is stab enemy_health -= 20
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



#If player win is False
#   print("You Died!")
#Else
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