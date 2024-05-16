def first_word(sentence):
    space_index = sentence.find(' ')
    return sentence[:space_index]


def second_word(sentence):
    space_index = sentence.find(' ')
    new_sentence = sentence[space_index+1:]
    second_space = new_sentence.find(' ')
    if second_space == -1:
        return new_sentence
    return new_sentence[:second_space]


def last_word(sentence):
    last_space_index = sentence.rfind(' ')
    return sentence[last_space_index+1:]



# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))