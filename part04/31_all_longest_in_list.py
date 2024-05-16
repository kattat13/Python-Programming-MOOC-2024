def all_the_longest(names: list):

    result = []

 

    for name in names:

        if result == [] or len(name) > len(result[0]):

            result = [name]

        elif len(name) == len(result[0]):

            result.append(name)

 

    return result