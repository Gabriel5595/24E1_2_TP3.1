import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

def main():
    database = [
    ["Alice", "Johnson", "alice@server.com"],
    ["Bob", "Miller", "bob@server.com"],
    ["Carol", "Smith", "carol@server.com"],
    ["David", "Jones", "david@server.com"],
    ["Emma", "Williams", "emma@server.com"],
    ["Frank", "Brown", "frank@server.com"],
    ["Grace", "Davis", "grace@server.com"],
    ["Henry", "Wilson", "henry@server.com"],
    ["Ivy", "Moore", "ivy@server.com"],
    ["Jack", "Taylor", "jack@server.com"],
    ["Liam", "Anderson", "liam@server.com"],
    ["Olivia", "Martinez", "olivia@server.com"],
    ["Noah", "Hernandez", "noah@server.com"],
    ["Sophia", "Garcia", "sophia@server.com"],
    ["William", "Lopez", "william@server.com"],
    ["Ava", "Gonzalez", "ava@server.com"],
    ["James", "Perez", "james@server.com"],
    ["Isabella", "Sanchez", "isabella@server.com"],
    ["Benjamin", "Ramirez", "benjamin@server.com"],
    ["Mia", "Torres", "mia@server.com"]
]
    database = register_user(database)
    print(database)

main()