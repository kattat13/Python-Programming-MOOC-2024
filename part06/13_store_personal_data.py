def store_personal_data(person: tuple):
    name, age, height = person
    with open('people.csv', 'a') as file:
        file.write(f'{name};{age};{height}')