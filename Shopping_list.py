print("Welcome to online shopping...")
shopping_list = []

while True:
    choice = int(input("Please select any option below \n1.Add item \n2.Remove item \n3.Display items \n4.Exit \n"))
    if choice == 4:
        print("Thanks for shopping...")
        break
    if choice == 1:
        item = input("Enter the item you want to add : ")
        shopping_list.append(item)
        print("Item added...")
    elif choice == 2:
        if len(shopping_list) == 0:
            print("There are no items in the cart to remove. Please add any item")
        else:
            item = input("Enter the item you want to remove : ")
            if item in shopping_list:
                shopping_list.remove(item)
                print("Item removed...")
            else:
                print("The item is not present in the cart")
    elif choice == 3:
        if len(shopping_list) == 0:
            print("There are no items in the cart")
        else:
            print("Items present in the cart are ")
            for i in shopping_list:
                print(i)

        