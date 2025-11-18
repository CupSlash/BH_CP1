#BH 2nd Flexible Calc.
import math 
nums = []
#introduce user
print("Welcome to the flexible calculator!")
#get their numbers and operation
operation = input("Which operation would you like to perform? sum, average, max, min, product: ")
number = input("What numbers would you like to use? (type done when done): ")
while number != "done":
    number = input("What numbers would you like to use? (type done when done): ")
    if number != int:
        break
    nums.append(number)
#If statements? For each operation 
while operation != "sum" or "average" or "max" or "min" or "product":
    if operation == "sum": 
        added_nums = 0
        for i in nums:
            added_nums += i
        print(added_nums)
    elif operation == "average":
        nums_unaveraged = 0
        num_of_nums = 0
        for i in nums:
            nums_unaveraged += i
            num_of_nums += 1
        nums_averaged = nums_unaveraged / num_of_nums
        print(nums_averaged)
    elif operation == "max":
        nums.sort()
        print(nums[-1])
    elif operation == "min":
        nums.sort()
        print(nums[0])
    elif operation == "product":
        multiplied_nums = 1
        for i in multiplied_nums:
            multiplied_nums *= i
        print(multiplied_nums)
    else:
        print("That is not an option")
        operation = input("Which operation would you like to perform? sum, average, max, min, product: ")