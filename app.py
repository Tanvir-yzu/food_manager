from icecream import ic

like_food = []

while True:
    ic(" Welcome to Like Food Manager")
    ic("0. - Exit -")
    ic("1. - Add Food")
    ic("2. - Remove Food")
    ic("3. - View All Liked Foods")

    option = input("Select Option: ")

    if option == "0":
        print("Exiting program...")
        break  # Exit the loop

    elif option == "1":
        food = input("Enter food to add: ")
        like_food.append(food)
        print(f"{food} added to liked foods list.")

    elif option == "2":
        food = input("Enter food to remove: ")
        if food in like_food:
            like_food.remove(food)
            print(f"{food} removed from liked foods list.")
        else:
            print(f"{food} not found in liked foods list.")

    elif option == "3":
        print("Liked Foods:")
        if like_food:
            for i, food in enumerate(like_food, start=1):
                print(f"{i}. {food}")
        else:
            print("No foods in the liked foods list yet.")

    else:
        print("Invalid option. Please try again.")
