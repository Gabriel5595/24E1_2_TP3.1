import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    ["Mia", "Torres", "mia@server.com"],
    ["Elias", "Torres", "elias@server.com"]
]
    
    menu(database)

main()