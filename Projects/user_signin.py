#BH 2nd User Sign In

user = input("Hello user, what's your name?: ")
password = input("What's your password?: ")

reuser = input("Please re-enter your username: ")
repassword = input("Please re-enter your password: ")



if reuser == user: 
    if repassword == password:
        print("Welcome", user)
    else:
        print("the username or password is incorrect.")
else:
    print("the username or password is incorrect.")