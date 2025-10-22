#BH 2nd Caesar Cypher
#You will need inputs for the operation choice, message, and shift value
#Your program should handle both uppercase and lowercase letters
#The output should change based on user input and chosen operation
#Outputs need to be easy to read and understand
code = []
game = False
encode = False
decode = False


start_game = input("Would you like to begin? y/n  ")
if start_game == "y":
    game = True
else: 
    pass

while game == True:
    choice = input("Hello, would you like to encode a message or decode a message?")
    if choice == "encode":
        encode = True
    elif choice == "decode":
        decode = True
    else:
        print("That isn't an option. Please type either 'encode' or 'decode'")
    #ENCODING
    while encode == True:
        new_item = input("What item would would you like to encode?")
        shift_number = int(input("How much would you like to shift your input?"))
        for char in new_item:
            if char.isalpha:
                new_item = ord(f"{char}") + shift_number
                code_item = chr(new_item)
                code.append(code_item)
                join = ''.join(code)
                list = [join]
        encode = False
    else:
        pass
    #if input is John it would be Kpio with a shift of 1
    #DECODING
    while decode == True:
        print(list)
        decode_item = input("Which item would you like to decode?")
        if decode_item not in join:
            print("That item is not in the list, please choose one of the following items.", list)
        elif decode_item in join:
            for char in decode_item:
                if char.isalpha:
                    item_2decode = ord(f"{char}") - shift_number
            print("Here is the decoded word.", item_2decode)
            list = list.remove(decode_item)
        print(list)
        decode = False
    else:
        pass