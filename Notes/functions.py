#BH 2nd Function Notes
#imports
# set global variables
num = 0
player_hp = 100
monster_hp = 100

#write functions
def add(x,y):
    return x+y

def initials(name):
    names = name.split("  ")
    initial = " "
    for name in names:
        initial += name[0]
    return initial

def attack(dmg):
    return player_hp - dmg

#write the rest of code
while num < add(5,5):
    print("Duck")
    num += 1
print("Goose")
print(f"Results is: {add(-6519146,36516)}")
total = add(689461, 654894)
print(add(add(3.14, .85), 10))
add(42,7)



print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Xavier's initials are: {initials("Xavier LaRose")}")
print(f"You have been attacked! hp is now {attack(15)}")
print(f"Health: player_hp")
