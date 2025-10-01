#BH 2nd Loops Notes
import time

nums = [6, 51, 61, 94, 351, 946, 5489, 4, 651, 684]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num}. And it is still a larger nummber!")
    else:
        print(num)

print("We completed all the numbers!")

for x in range(1, 10):
    print(x)
time.sleep(3)


