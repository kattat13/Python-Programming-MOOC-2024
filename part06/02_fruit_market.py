def read_fruits():
    fruits_dict = dict()
    with open('fruits.csv') as file:
        for line in file:
            line = line.replace('\n', '')
            fruit, price = line.split(';')
            fruits_dict[fruit] = float(price)
    return fruits_dict