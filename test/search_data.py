def search_data(database, search_value, surname=False):
    result = []
    if surname:
        for person in database:
            if person[1] == search_value:
                result.append(person)
    else:
        for person in database:
            if person[0] == search_value:
                result.append(person)
    return result

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

    print(search_data(database, "Torres", True))

main()