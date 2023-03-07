import database
import menu


if __name__ == '__main__':
    while (user_input := input(menu.main_menu)) != "4":
        print(user_input)
        if user_input == "1":
            print("You've selected 1")
        elif user_input == "2":
            print("You've selected 2")
        elif user_input == "3":
            print("You've selected 3")
        else:
            print("Invalid user_input!")
