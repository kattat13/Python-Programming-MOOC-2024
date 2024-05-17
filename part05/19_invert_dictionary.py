def invert(dictionary: dict):
    results = {}
    for key, value in dictionary.items():
        results[value] = key
    dictionary.clear()
    for new_key in results:
        dictionary[new_key] = results[new_key]
    