#BH 2nd Rock Paper Scissors

import random

Begin = input("Welcome to Rock, Paper, Scissors! Would you like to begin? y/n:")
if Begin == "y":
    game = True
elif Begin == "n":
    game = False
else:
    print('That is not an option, please type either "y" of "n"')

Bot = 0
User = 0
score = (Bot "-" User)

while game == True:
    print("The next round has started, rock, paper, or scissors")
    print(score)
elif game == False: 
    print("Okay, goodbye!")
else:
    print("Not an option.")