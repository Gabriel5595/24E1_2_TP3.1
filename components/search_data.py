def search_data(database, search_value, surname=False):
    if surname:
        for person in database:
            if person[1] == search_value:
                return person
        return False
    else:
        for person in database:
            if person[0] == search_value:
                return person
        return False