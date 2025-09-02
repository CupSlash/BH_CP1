# BH 2nd Strings Notes

#Example
sentence = "The quick brown fox jumps over the lazy dog!"
first_name = 'Xavier'
month = 'September'
food = "chocolate"
last_name = "LaRose"

#If I need to use ' or "
name = "La'Rose"
best = '"The return of the king" is the best book ever!'

funny = 'The dog jumped into the lake'

#The length of strings
length = len(month)
print("September has", length, "letters")

# Escape Character
print('\tWill said\n\t\t\t\t\t\t"Don\'t die"')

#Concatenate
full_name = first_name + " " + last_name

print(full_name)

#Slice
string[startindex:endindex]
print (last_name[2:6])