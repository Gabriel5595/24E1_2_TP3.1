def request_name_and_surname():
    name = input("Please enter a name: ")
    surname = input("Please enter a surname: ")
    name_and_surname = [name[0].upper(), surname[0].upper()]
    
    return name_and_surname