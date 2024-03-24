from components.register_user import register_user
from components.request_search import request_search

def menu(database):
    while True:
        try:
            option = int(input("""\nPlease, enter the number of one of the options below:
1) Add User
2) Seach User
3) Exit\n"""))
            
            if option == 1:
                database = register_user(database)
                print(database)
            elif option == 2:
                request_search(database)
            elif option == 3:
                print("Exiting...")
                break
            else:
                print("\nThe selected option is not valid.\n")
            
        except ValueError:
            print("\nPlease enter one of the valid options.\n")