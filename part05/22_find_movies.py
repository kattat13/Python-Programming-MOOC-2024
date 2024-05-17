def find_movies(database: list, search_term: str):
    titles = []
    for row in database:
        if search_term in row['name'].lower():
            titles.append(row)
    return titles