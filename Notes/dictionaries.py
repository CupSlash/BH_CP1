#BH 2nd dictionary notes

person = {
    #key: value,
    "name": "Katie",
    "age": 37,
    "job": "coordinator",
    "siblings": ["Alex", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake"]
}

print(person["name"])
print(person.keys())
for key in person.keys():
    if key == "siblings":
        for sib in person[key]:
            print(f"{person['name']} has a sibling named {sib}")
    else:
        print(f"{key} is {person[key]}")
print(person.values())
person["age"] += 1
print(person["age"])
person["birthday"] = "June 8"
print(person.items())
person["birthday"] = "October 27"
print(person.items())