def calc_average(person: dict):
    results = 0
    for key, value in person.items():
        if 'result' in key:
            results += value
    return results / 3


def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest_average = person1
    
    if calc_average(person2) < calc_average(smallest_average):
        smallest_average = person2

    if calc_average(person3) < calc_average(smallest_average):
        smallest_average = person3

    return smallest_average
        

if __name__ == '__main__':
    person1 = {"name": "Anna", "result1": 9, "result2": 9, "result3": 9}
    person2 = {"name": "Gary", "result1": 7, "result2": 7, "result3": 7}
    person3 = {"name": "Larry", "result1": 8, "result2": 8, "result3": 8}

    print(smallest_average(person1, person2, person3))