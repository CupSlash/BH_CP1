#BH 2nd Combat Code
import random

#USER STATS STAGE
mon_health = 100
mon_defense = random.randint(1, 100)
mon_damage = random.randint(1,20) + 2
mon_attack = random.randint(1,100) + 3

health = 0
defense = 0
damage = 0
attack = random.randint(1,20) + 3

def run_player_turn(health, attack, damage, mon_defense, mon_health):
    user_attack = input("Your turn! Your attack options are: 1 for Normal Attack, 2 for Wild Attack (you can double the damage but you will also take damage), 3 to Drink a healing potion (regain 9 health), and 4 to Dodge (You may or may not successfully dodge)")
    if user_attack == "1":
        if attack >= mon_defense:
            print("You did", damage, "damage!")
            mon_health -= damage
        else:
            print("You did no damage!")
            pass
    elif user_attack == "2":
        mon_health -= damage * 2
        health -= damage / 2
        print("You did", damage * 2, "damage and received", damage / 2, "damage!")
    elif user_attack == "3":
        health += 9
        print("Your received 9 health!")
    elif user_attack == "4":
        dodge = random.randint(1,2)
        if dodge == 1:
            print("You have successfully dodged!")
        else:
            health -= damage / 2
            print("You failed to dodge. You received", damage / 2, "damage!")
    else:
        print("That is not an option, please choose 1, 2, 3, or 4.")

    return health, mon_health

def run_monster_turn(mon_attack, mon_damage, defense, health):
    print("It is the monster's turn.")
    if (mon_attack >= defense):
        health -= mon_damage
        print("The monster has done", mon_damage, "damage.")
    else:
        print("The monster did no damage.")
    
    return health

print("Welcome player_1")
choice = input("Which class do you choose? \n press 1 for unemployed \n 2 for sales wizard \n 3 for HR guy \n")

if choice == "1":
    health = 1
    defense = 3
    damage = 2
    print("You're cooked!")
elif choice == "2":
    health = 80
    defense = 200
    damage = 90
    print("Great choice!")
elif choice == "3":
    health = 150
    defense = 100
    damage = 80
    print("Great choice!")
else:
    print("That is not an option, please choose 1, 2, or 3.")

print("Here are your stats. Health:", health, "Defense:", defense, "Attack:", attack, "Damage:", damage)

#COMBAT SITUATION
print("You've come across a wild job application!")

#COMBAT INTSTRUCTION AND WHO GOES FIRST
while True:
    turn = random.randint(1,2)

    if turn == 1:
        updated_stats = run_player_turn(health, attack, damage, mon_defense, mon_health)
        health = updated_stats[0]
        mon_health = updated_stats[1]
    else:
        health = run_monster_turn(mon_attack, mon_damage, defense, health)

    print("Your health is now:", health, "The monster's health is now:", mon_health)

    if mon_health <= 0 and health >= 1:
        print("You've beat the job application! Your journey continues.")
        break
    elif mon_health <= 0 and health <= 0:
        print("Both you and the monster are dead! Nobody wins!")
        break
    elif mon_health >= 1 and health <= 0:
        print("The job application has won! Try again and see if you win!")
        break
    else:
        pass