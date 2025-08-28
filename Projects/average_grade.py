# BH 2nd average_grade
English = float(input("what is your English grade"))
CS = float(input("What is your CS grade"))
World_Civilizations = float(input("What is your World Civ. grade"))
Advisory = float(input("What is your Advisory grade"))
Drawing = float(input("What is your Drawing grade"))
Math = float(input("What is your Math grade"))
Biology = float(input("What is your biology grade"))

total = English + CS + World_Civilizations + Advisory + Drawing + Math + Biology
average = total / 7
print("The average grade of all your classes is", average, "%")