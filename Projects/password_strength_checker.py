#BH 2nd Password Strength Checker

# total = 0
total = 1
# password = user's input after asking password
password = input("What is your password? :")
# if len(password) == 8:
if len(password) >= 8:
    #total = total + 1
    total = total + 1
else:
    pass
#check to see if the user has one or more uppercase and lowercase letter with .upper and .lower [add point to total]
if password.isupper() == True:
    total = total + 1
else:
    pass
if password.islower() == True:
    total = total + 1
else:
    pass
#check for special character with .alnum[add point to total]
if password.isalnum() == True:
    total = total - 1
else:
    pass
#check for any number with .isdigit[add point to total]
if password.isdigit() == True:
    total = total + 1
else:
    pass
#print the total out of 5 for the user and how strong it is
if password == "password":
    print("Ain't no way your password is password.")
else:
    print ("Your password strength is a", total, "out of 5")
#find out how good the total is with an if statement
if total <= 2:
    print("Your password is pretty weak.")
elif total == 3:
    print("I'd say your password is average.")
elif total == 4:
    print("That's a strong password!")
elif total == 5:
    print("That is an excellent password! Super strong!")
else: 
    print("HACKER! HACKER! HACKER!")