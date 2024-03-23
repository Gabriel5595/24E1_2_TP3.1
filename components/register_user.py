from components.request_name_and_surname import request_name_and_surname
from components.request_email import request_email

def register_user(database):
    name_and_surname = request_name_and_surname()
    email = request_email()
    
    if email == False:
        print("Not possible to finalize user registration since no valid email has been entered.")
    else:
        name_and_surname.append(email)
        print(name_and_surname)
        database.append(name_and_surname)
        return database