#BH 2nd calculator.py

number_1 = float(input("Input a full number: "))
number_2 = float(input("Input a second full number: "))





times = number_1 * number_2
add = number_1 + number_2
minus = number_1 - number_2
divide = number_1 / number_2
mod = number_1 % number_2
ex = number_1 ** number_2

print(number_1, "*", number_2, "=", times)
print(number_1, "+", number_2, "=", add)
print(number_1, "-", number_2, "=", minus)
print(number_1, "/", number_2, "=", divide)
print(number_1, "%", number_2, "=", mod)
print()


print(times, add, minus, divide, mod, ex)