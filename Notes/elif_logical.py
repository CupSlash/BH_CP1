#BH 2nd elif and Logical operators notes

homework = False
chores = True
room = True
if homework and chores and room:
    print("You can go to your friends house.")
elif not chores or not room:
    print("Do your chores and clean your room!")
else:
    print("Go do your homework")

username = input("Enter your username")
password = input("Enter your password")

if username == "MsLaRose":
    if password == "1234":
        print("Welcome Ms. Larose")
    else:
        print("Incorrect password")
elif username == "Tia" and password == "password":
    pass
elif username == "Andrew" and password == "orange":
    print("Welcome Andrew")
else: 
    print("That is not a valid sign in.")