#BH 2nd Order Up!
#Create categories
order = []
total = 0.00
#define the menu using a dictionary
drinks = {
    "Soda": 3.00,
    "Water": 1.00,
    "Wine": 5.00,
    "The special secret serum": 100.00,
}
mains = {
    "Hamburger": 3.00,
    "Cheeseburger": 2.50,
    "Nothingburger": 0.00,
    "Skibidiburger": 6.70,
}
sides = {
    "Chicken nuggets": 1.50,
    "Fries": 1.00,
    "Soup": 1.50,
    "Plain chips": 0.50,
    "Chips & salsa": 1.00,
    "Chips & guac": 1.00
}
#Get the main course that the user wants
def ordering_mains(order, total):
    print('Welcome to "Order Up!" Time to choose your main course.')
    main_choice = input(f"main course:, {mains}")
    #see if it exists
    if main_choice in mains:
        #add it to the recepit if it is on the menu
        order.append(main_choice)
        #person["age"] += 1
        total += mains[f"{main_choice}"]
    else:
        #tell them if it isn't on the menu
        print("Please choose from the menu.")
#repeat the process for drinks
def ordering_drinks(order, total):
    drink_choice = input(f"What would you like to drink?, {drinks}")
    if drink_choice in drinks:
        order.append(drink_choice)
        total += drinks[f"{drink_choice}"]
    else:
        print("Please choose from the menu.")
#repeat again for sides
def ordering_sides(order, total):
    side_choice1 = input(f"What would you like for your first side dish?, {sides}")
    if side_choice1 in sides:
        order.append(side_choice1)
        total += sides[f"{side_choice1}"]
    else:
        print("Please choose from the menu.")
    side_choice2 = input(f"And your second?, {sides}")
    if side_choice2 in sides:
        order.append(side_choice2)
        total += sides[f"{side_choice2}"]
    else:
        print("Please choose from the menu.")
#print the final order
ordering_mains()
ordering_drinks()
ordering_sides()
print("Here is your receipt:", order, total)