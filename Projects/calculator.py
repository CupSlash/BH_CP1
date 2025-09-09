#BH 2nd calculator.py

num_1 = float(input("Input a number: "))
num_2 = float(input("Input a second number: "))

number_1 = round(num_1, 2)
number_2 = round(num_2, 2)



Int_times = number_1 * number_2
Int_add = number_1 + number_2
Int_minus = number_1 - number_2
Int_divide = number_1 / number_2
Int_mod = number_1 % number_2
Int_ex = number_1 ** number_2

times = round(Int_times, 2)
add = round(Int_add, 2)
minus = round(Int_minus, 2)
divide = round(Int_divide, 2)
mod = round(Int_mod, 2)
ex = round(Int_ex, 2)

print(number_1, "*", number_2, "=", times)
print(number_1, "+", number_2, "=", add)
print(number_1, "-", number_2, "=", minus)
print(number_1, "/", number_2, "=", divide)
print(number_1, "%", number_2, "=", mod)
print(number_1, "**", number_2, "=", ex)