#BH 2nd Factorials
#While True:
while True:
#Make variable user_num based off of user_input
    user_num = input("Which number would you like the factorial of?")
#Check if user_num is a number
#if usernum is not int
    if not user_num.isnumeric():
#print that isn't a valid option
        print("That is not a valid option")
#else:
    else:
#break
        user_num = int(user_num)
        break
#Define factorial(num):
def factorial(user_num):
#make variable org_num = num
    org_num = user_num
#make multi_num = num - 1
    multi_num = user_num - 1
#make for loop for length of multi_num
#for i in range(multi_num):
    for i in range(multi_num):
#num *= multi_num
        user_num *= multi_num
#multi_num - 1 #Subtract one each loop from multi_num return original number org_num factorial: num
        multi_num - 1
    return f"Original number: {org_num}, Factorial: {user_num}"
#call function
#print(factorial(user_num))
print(factorial(user_num))