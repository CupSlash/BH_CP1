#args and kwargs notes 

#def hello(name = "Tia", age = 29):
    #return f"Hello {name}! You are {age}!"

#print(hello())
#print(hello("Xavier"))
#print(hello(age = 19, name = "Treyson"))

def hello(last, *names):
    print(type(names))
    for name in names:
        print(f"Hello {name} {last}")

hello("LaRose", "Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake")