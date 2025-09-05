#BH 2nd idiot_proof.py
name = input("What is your first and last name: ").strip().capitalize()

number = input("Please input your phone number ").strip()
word = "-"

gpa = float(input("What's your GPA: "))
gpa = round(gpa, 1)

print("\n", name)

print("\n", number.replace(word, " "))

print("\n", gpa)