from components.search_data import search_data

def request_search(database):
    try:
        search_options = int(input("Enter one of the search options below:\n1) Name\n2) Surname\n"))
        
        if search_options == 1:
            name = input("Enter the name to be searched: ")
            result = search_data(database, name)
            if result == None:
                print(f"No information with data {name} has been found.")
            else:
                return result
            
        elif search_options == 2:
            surname = input("Enter the surname to be searched: ")
            result = search_data(database, surname, True)
            if result == None:
                print(f"No information with data {surname} has been found.")
            else:
                return result
        else:
            print("The selected option is not valid.")
        
    except ValueError:
        print("Please enter one of the valid options.")