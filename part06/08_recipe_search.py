def search_by_ingredient(filename: str, ingredient: str):
    recipes_list = []
    f = open(filename)
    data = f.read().split('\n')

    for num, line in enumerate(data):
        if line == ingredient:
            for i in reversed(range(num)):
                if data[i].isdigit():
                    recipes_list.append(f'{data[i-1]}, preparation time {data[i]} min')
                    break
    return recipes_list



def search_by_name(filename: str, word: str):
    recipes_list = []
    with open(filename) as file:
        for line in file:
            if line[0].isupper():
                    if word.lower() in line.lower():
                        recipes_list.append(line.strip()) 
    
    return recipes_list


def search_by_time(filename: str, prep_time: int):
    recipes_list = []
    f = open(filename)
    data = f.read().split('\n')
    for num, line in enumerate(data):
        if line.isdigit():
            if prep_time > int(line):
                recipes_list.append(f'{data[num-1]}, preparation time {line} min')

    return recipes_list


if __name__ == "__main__":

    # found_recipes = search_by_name("recipes2.txt", "oat")
    # found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)