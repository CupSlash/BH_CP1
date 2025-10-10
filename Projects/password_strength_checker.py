#BH 2nd Password Strength Checker

# total = 0
total = 0
# password = user's input after asking password
password = input("What is your password? :")
# if len(password) == 8:
if len(password) == 8:
    #total = total + 1
    total = total + 1
#else:
else:
    #break
#check to see if the user has one or more uppercase and lowercase letter with .upper and .lower [add point tp total]

#check for special character with .alnum[add point to total]

#check for any number with .isdigit[add point to total]

#print the total out of 5 for the user and how stron it is