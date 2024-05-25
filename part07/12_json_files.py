import json


def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()
    
    persons = json.loads(data)
    
    for person in persons:
        print(person['name'], end=' ')
        print(f"{person['age']} years", end=' ')
        h = ''
        for hobby in person['hobbies']:
            h += f'{hobby}, '
        print(f'({h[:-2]})')


if __name__  == '__main__':
    print_persons('file1.json')

