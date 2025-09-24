# BH 2nd What is my Grade?

grade = float(input("What's your grade percentage?: "))

if grade >= 90:
    if grade >= 97:
        print("Great job! You have an A+")
    elif grade <= 92:
        print("You have an A-! That's really good!")
    else:
        print("You have an A! Keep going!")
elif grade >= 80:
    if grade >= 87:
        print("B+! Almost an A!")
    elif grade <= 82:
        print("B-! That's alright")
    else:
        print("Perfect B! That's an average grade!")
elif grade >= 70:
    if grade >= 77:
        print("C+! Almost a B!")
    elif grade <= 72:
        print("C-! That's not the best, try to increase it.")
    else:
        print("Perfect C! That's slightly below the average.")
elif grade >= 60:
    if grade >= 67:
        print("D+! It's not good, but you can still improve.")
    elif grade <= 62:
        print("D-! Well, it's not an F.")
    else:
        print("You have a D, it's not the worst, but it definitely not the best.")    
else:
    print("You have an F! :[")