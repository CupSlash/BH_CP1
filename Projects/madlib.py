#BH 2nd madlib_py
#Madlib: This morning, my (adjective) alarm clock didn't go off, so I rushed out the door wearing (plural noun) on my feet. At school, my (noun) exploded during chemistry class, which caused a (adjective) mess. During lunch, someone traded me their (plural noun) for my mystery meat. In gym, we had to do (number) laps around the track, and I almost passed out. By the end of the day, I felt like a (noun) that had been run over by a bus.
adjective1 = input("Give me an adjective: ")
plural_noun1 = input("What's an example of a plural noun: ")
noun1 = input("I need a noun: ")
plural_noun2 = input("Sorry, but I also need a new plural noun: ")
number = input("Give me a number, 1-100: ")

sentence1 = "\nThis morning, my " + adjective1 + " alarm clock didn't go off, so I rushed out the door wearing " + plural_noun1 + " on my feet."
sentence2 = " At school my " + noun1 + " exploded during chemistry class, which caused a " + adjective1 + " mess."
sentence3 = " During lunch, someone traded me their " + plural_noun2 + " for my mystery meat."
sentence4 = " In gym, we had to do " + number + " laps around the track, and I almost passed out."
sentence5 = " By the end of the day, I felt like a " + noun1 + " that had been run over by a bus."
story = sentence1 + sentence2 + sentence3 + sentence4 + sentence5
print(story)