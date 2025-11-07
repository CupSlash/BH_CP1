#BH 2nd Order Up!
#define the menu using a dictionary
menu = {
    #Drinks
    "Soda": 3.00,
    "Water": 1.00,
    "Wine": 5.00,
    #Food items
    "Hamburger": 3.00,
    "Cheeseburger": 2.50,
    "Nothingburger": 0.00,
    #Side choices
    "Chicken nuggets": 1.50,
    "Fries": 1.00,
    "Soup": 1.50,
    "Plain chips": 0.50,
    "Chips & Salsa": 1.00,
    "Chips & Guac": 1.00
}
#Create categories
drinks = ["Soda", "Water", "Wine"]
mains = ["Hamburger, Cheeseburger, Nothingburger"]
sides = ["Chicken nuggets", "Fries", "Soup", "Plain chips", "Chips & Salsa", "Chips & Guac"]
order = []
#Add main course to order
print('Welcome to "Order Up!"')
main_choice = input("main course:", mains)
#Add sides
side_choice = input("side dishes:", sides)
#Add drinks
drink_choice = input("drink:", drinks)
#Create the total cost
total = 0.00
#print the final order
print("Here is your Receipt:", order, total)