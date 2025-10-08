#BH 2nd Rock Paper Scissors

import random
choices = ["rock", "paper", "scissors"]

Begin = input("Welcome to Rock, Paper, Scissors! Would you like to begin? y/n:")
if Begin == "y":
    game = True
elif Begin == "n":
    game = False
else:
    print('That is not an option, please type either "y" or "n"')

if game == False:
    print("Okay, goodbye!")

Bot_score = 0
User_score = 0
score = (Bot_score, User_score)

while game:
    score = (Bot_score, User_score)
    print("The score is now", score)
    User = input("The next round has started! Do you choose rock, paper, or scissors?")
    Bot = random.choice(choices)
    print("I chose", Bot)
    if User == "rock":
        if Bot == "paper":
            print("Paper beats rock! I win!")
            Bot_score = Bot_score + 1
        elif Bot == "rock":
            print("I guess it's a tie.")
        else:
            print("Rock beats scissors, I lost.")
            User_score = User_score + 1
    elif User == "paper":
        if Bot == "paper":
            print("We have a tie!")
        elif Bot == "rock":
            print("Paper covers rock, you won that round.")
            User_score = User_score + 1
        else:
            print("Scissor cuts paper, I won!")
            Bot_score = Bot_score + 1
    elif User == "scissors":
        if Bot == "paper":
            print("Scissors cuts paper, I lost.")
            User_score = User_score + 1
        elif Bot == "rock":
            print("My rock smashes your scissors, victory!")
            Bot_score = Bot_score + 1
        else:
            print("We both chose scissors! We tied!")
    else:
        print("That was not an option, please fix it.")
