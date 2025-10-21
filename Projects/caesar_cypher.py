#BH 2nd Caesar Cypher
#You will need inputs for the operation choice, message, and shift value
#Your program should handle both uppercase and lowercase letters
#The output should change based on user input and chosen operation
#Outputs need to be easy to read and understand
encode = False
decode = False
choice = input("Hello, would you like to encode a message or decode a message?")
if choice == "encode":
    encode = True
elif choice == "decode":
    decode = True
else:
    print("That isn't an option. Please type either 'encode' or 'decode'")
#ENCODING


#if input is John it would be Kpio.


#DECODING