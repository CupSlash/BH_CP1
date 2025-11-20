#BH 2nd Flexible Calc.
#imports
import math 
import statistics
#functions
def get_operation():
    while True:
        operation = input("Which operation would you like to perform? sum, average, max, min, product: ")
        if operation in ["sum", "average", "max", "min", "product"]:
            return operation
        else:
            print("That is not an option. Please try again.")
def get_numbers():
    nums = []
    while True:
        number = input("What numbers would you like to use? (type done when done): ")
        if number != "done":
            number = float(number)
            nums.append(number)
        else:
            break 
    return nums
def calculate(nums, operation):
        #sum
    if operation == "sum": 
        print(sum(nums))
        #average
    elif operation == "average":
        print(statistics.mean(nums))
        #max
    elif operation == "max":
        print(max(nums))
        #min
    elif operation == "min":
        print(min(nums))
        #product
    elif operation == "product":
        print(math.prod(nums))
    else:
        pass
#introduce user
print("Welcome to the flexible calculator!")
#THE ACTUAL PROGRAM
operation = get_operation()
nums = get_numbers()
calculate(nums, operation)
