#BH 2nd Caesar Cypher
#You will need inputs for the operation choice, message, and shift value
#Your program should handle both uppercase and lowercase letters
#The output should change based on user input and chosen operation
#Outputs need to be easy to read and understand
code = []
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
if encode == True:
    new_item = input("What item would would you like to encode?")
    shift_number = int(input("How much would you like to shift your input?"))
    for char in new_item:
        if char.isalpha:
            new_item = ord(f"{char}") + shift_number
            code_item = chr(new_item)
            code.append(code_item)

join = ''.join(code)


#if input is John it would be Kpio with a shift of 1


#DECODING
if decode == True:
    print(join)
    decode_item = input("Which item would you like to decode?")
    if decode_item not in join:
        print("That item is not in the list, please choose one of the following items.", join)
    elif decode_item in join:
        print("Here is the decoded word.")
   
print(join)