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