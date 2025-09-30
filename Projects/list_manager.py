#BH 2nd Shopping List Manager

list = []

while True:
    action = input("What do you want to do? Your options are, 'print list', 'exit', 'add item' 'remove item'")
    if action == "add item":
        new_item = input("What item would you like to add?").strip()
        list.append(new_item)
        print(f"Here is your new Shopping list:{list}")
    elif action == "print list":
        print(f"Here is your Shopping list {list}")
    elif action == "remove item":
        print(list)
        removed_item = input("What item would you like to remove?").strip()
        if removed_item not in list:
            print("This item is not in the shopping list, maybe you spelled something wrong?")
        elif removed_item in list:
            list.remove(removed_item)
            print(f"Here is your new Shopping list: {list}")
        else:
            print("Error 404")
    elif action == "exit":
        break
    else:
        print("That is not a given action. Please enter one of the possible choices below.")