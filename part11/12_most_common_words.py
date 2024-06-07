import string 


def most_common_words(filename: str, lower_limit: int):
    data = open(filename).read().replace('\n', ' ').replace('.', '').replace(',', ' ').replace('  ', ' ')

    words = data.split(' ')

    return {word : words.count(word) for word in words if words.count(word) >= lower_limit}


if __name__ == '__main__':
    print(most_common_words('programming.txt', 4))