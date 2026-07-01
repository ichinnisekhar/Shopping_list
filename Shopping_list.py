print("Welcome to online shopping...")
shopping_list = []

while True:
    choice = int(input("Please select any option below \n1.Add item \n2.Remove item \n3.Display items \n4.Exit \n\n"))
    if choice == 4:
        print("Thanks for shopping...")
        break
    if choice == 1:
        item = input("Enter the item you want to add : ")
        shopping_list.append(item)
        print(f"{item} is added to shopping cart\n")
    elif choice == 2:
        if len(shopping_list) == 0:
            print("There are no items in the cart to remove. Please add any item\n")
        else:
            item = input("Enter the item you want to remove : ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} is removed from the shopping cart")
            else:
                print(f"{item} is not present in the cart\n")
    elif choice == 3:
        if len(shopping_list) == 0:
            print("There are no items in the cart\n")
        else:
            print(f"Items in the cart ({len(shopping_list)}): ")
            for ind,x in enumerate(shopping_list):
                print(f"{ind+1}.{x}")
        print("\n")