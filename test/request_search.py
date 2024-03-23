import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    
    print(request_search(database))

main()