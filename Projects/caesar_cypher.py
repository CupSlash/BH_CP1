#BH 2nd Caesar Cypher
#You will need inputs for the operation choice, message, and shift value
#Your program should handle both uppercase and lowercase letters
#The output should change based on user input and chosen operation
#Outputs need to be easy to read and understand

ord('A')  #65
ord('Z')  #90
ord('a')  #97
ord('z')  #122

#Define functions

#Encode
def encode(item_2encode, shift_number):
    encoded_item = ""
    for char_2encode in item_2encode:
        if char_2encode.isalpha():
            if char_2encode.isupper():
                base = ord('A')    
            else:
                base = ord('a')
            char_2encode_point = ord(char_2encode)
            # Subtract base to make A=0, B=1, ..., Z=25
            encoded_char_point_based = char_2encode_point - base
            # Shift the character point
            candidate_char_point_based = encoded_char_point_based + shift_number
            # Wrap around using modulo 26
            corrected_char_point_based = candidate_char_point_based % 26
            # Add base back to get the final encoded character point
            char_2encode_point = corrected_char_point_based + base
            encoded_char = chr(char_2encode_point)
            encoded_item += encoded_char
        else:
            encoded_item += char_2encode
    return encoded_item

#Decode
def decode(item_2decode, shift_number):
    decoded_item = ""
    for char_2decode in item_2decode:
        if char_2decode.isalpha():
            if char_2decode.isupper():
                base = ord('A')    
            else:
                base = ord('a')
            char_2decode_point = ord(char_2decode)
            # Subtract base to make A=0, B=1, ..., Z=25
            decoded_char_point_based = char_2decode_point - base
            # Shift the character point backwards
            candidate_char_point_based = decoded_char_point_based - shift_number
            # Wrap around using modulo 26
            corrected_char_point_based = candidate_char_point_based % 26
            # Add base back to get the final decoded character point
            char_2decode_point = corrected_char_point_based + base
            decoded_char = chr(char_2decode_point)
            decoded_item += decoded_char
        else:
            decoded_item += char_2decode
    return decoded_item
#Start program
while True:
    choice = input("Hello, would you like to encode a message or decode a message?")
    if choice == "encode":
        item_2encode = input("What item would would you like to encode?")
        shift_number = int(input("How much would you like to shift your input?"))
        encoded_item = encode(item_2encode, shift_number)
        print("Here is your encoded item:", encoded_item)
    elif choice == "decode":
        item_2decode = input("What item would you like to decode?")
        shift_number = int(input("What shift number was used to encode this item?"))
        decoded_item = decode(item_2decode, shift_number)
        print("Here is your decoded item:", decoded_item)
    else:
        print("That isn't an option. Please type either 'encode' or 'decode'")
    