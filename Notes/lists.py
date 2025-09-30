#BH 2nd Lists Notes
import random

names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Eric", 5, 3.14, False]

print(names)
print(names[3])
print(names[random.randint(1,len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names += ["Joseph", "Israel", "Zee"]
names.remove(3.14)
x = names.index(5)
names.pop(x)
print(names)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

board[1][1] = "X"

print(board)
# List 
# Tuple
classes = ("Bard", "Monk", "Barbarian", "Paladen")

# Set
fruit = {"Apple", "Orange", "Strawberry", "Kiwi"}
print(fruit)