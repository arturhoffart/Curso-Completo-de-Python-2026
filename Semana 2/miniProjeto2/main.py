from users import add_user, list_users, list_user_18, search_user


# create the menu
def menu():
    print("\n1 - Add user")
    print("2 - List all users")
    print("3 - List only 18+ users")
    print("4 - Search user by name")
    print("5 - Exit")


while True:
    menu()
    option = input("Choose an option: ")

    if option == "1":
        name = input("Enter user name: ")
        age = int(input("Enter user age: "))
        mail = input("Enter user mail: ")
        add_user(name, age, mail)

    elif option == "2":
        list_users()

    elif option == "3":
        list_user_18()

    elif option == "4":
        name = input("Enter name to search: ")
        search_user(name)

    elif option == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid option, try again.")
