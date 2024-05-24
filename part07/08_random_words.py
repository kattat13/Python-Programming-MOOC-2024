from random import sample


def words(n: int, beginning: str):
    source_file = open('words.txt').read().split()
    source_filered = [word for word in source_file if word.startswith(beginning)]
    result = sample(source_filered, n)

    if len(result) < n:
        raise ValueError("Not enough suitable words can be found!")

    return result



if __name__ == '__main__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)