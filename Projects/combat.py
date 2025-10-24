#BH 2nd Combat Code
import random
user_first = False
battling = True
#USER STATS STAGE
mon_health = 100
health = 0
defense = 0

print("Welcome player_1")
choice = input("which class do you choose? \n press 1 for unemployed \n 2 for sales wizard \n 3 for HR guy")

if choice == "1":
    health = 1
    defense = 3
    print("You're cooked! You're stats are Health:", health, " Defense", defense)
elif choice == "2":
    health = 80
    defense = 200
    print("Great choice! You're stats are, Health:", health, " Defense", defense)
elif choice == "3":
    health = 150
    defense = 100
    print("Great choice! You're stats are Health:", health, " Defense:", defense)
else:
    print("That is not an option, please choose 1, 2, or 3.")
#COMBAT SITUATION
print("You've come across a wild job application.")
#COMBAT INTSTRUCTION AND WHO GOES FIRST
While battling = True:
    attack = random.randint(1,20) + 3
    damage = random.randint(1,8) + 4
    turn = random.randint(1,2)
    if turn == 1:
        print("You go first! You will begin your turn now. Here are your attack and damage stats", attack, damage)
        user_first = True
        print("Normal Attack, Wild Attack (you can double the damage but you will also take damage), Drink a healing potion (regain 9 health), Flee (You may or may not get away)")
    else:
        print("The Monster starts the battle. It's turn is starting now.")
    if user_first = True:
        user_attack = input("Your choices are, 1 for Normal Attack, 2 for Wild Attack (you can double the damage but you will also take damage), 3 for Drink a healing potion (regain 9 health), and 4 for Flee (You may or may not get away)")
            if user_attack = "Normal"