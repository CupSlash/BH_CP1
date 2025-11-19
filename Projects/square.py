#BH 2nd Squared numbers      #Copy paste from Mapping notes and make necessary changes 
numbers = [651, 94, 5619, 135, 4, 6501, 68, 7, 123, 54, 6, 4, 1, 13, 15, 11, 67, 18, 167, 267]
exponent = list(map(lambda num: num ** 2, numbers))
print(exponent)
for i, num in enumerate(numbers):
    print(f"{num} to the power of 2 is {exponent[i]}")