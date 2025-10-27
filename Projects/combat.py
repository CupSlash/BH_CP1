#BH 2nd Combat Code
import random
user_first = False
battling = True
mon_win = False
#USER STATS STAGE
mon_health = 100
health = 0
defense = 0

print("Welcome player_1")
choice = input("which class do you choose? \n press 1 for unemployed \n 2 for sales wizard \n 3 for HR guy \n")

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
print("You've come across a wild job application!")
#COMBAT INTSTRUCTION AND WHO GOES FIRST
while battling == True:
    attack = random.randint(1,20) + 3
    damage = random.randint(1,8) + 4
    turn = random.randint(1,2)
    if turn == 1:
        print("Your turn! Here are your attack and damage stats. Attack:", attack, "Damage:", damage)
        user_first = True
        user_attack = input("Your attack options are: 1 for Normal Attack, 2 for Wild Attack (you can double the damage but you will also take damage), 3 to Drink a healing potion (regain 9 health), and 4 to Flee (You may or may not get away)")
        if user_attack == "1":
            mon_health -= damage
            print("The monster's health is now", mon_health)
        elif user_attack == "2":
            damage *= 2
            mon_health -= damage
            print("The monster's health is now", mon_health) 
            health -= damage / 4
            print("You're health is now", health)
            if mon_health <= 0 and health >= 1:
                mon_win = False
                battling = False
            elif mon_health <= 0 and health <= 0:
                print("Both you and the monster are dead! Nobody wins!")
                battling = False
                break
            elif mon_health >= 1 and health <= 0:
                mon_win = True
                battling = False
            else:
                continue
        elif user_attack == "3":
            health += 9
            print("You're health is now", health)
        elif user_attack == "4":
            flee = random.randint(1,2)
            if flee == 1:
                print("You have sucessfully fled!")
                battling == False
            if flee == 2:
                print("You are still in battle.")
        else:
            print("That is not an option, please choose 1, 2, 3, or 4.")
    else:
        print("It is not the monster's turn.")
        health -= damage
        print("This monster has done", damage, "damage. You're health is now", health)
        continue

if mon_win == True:
    print("The job application has won! Try again and see if you win!")
else:
    print("You've beat the job application! Your journey continues.")