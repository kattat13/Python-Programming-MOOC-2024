from string import ascii_letters, digits

def change_case(orig_string: str):
    new_str = ''
    for letter in orig_string:
        if letter.isupper():
            new_str = new_str + letter.lower()
        else:
            new_str = new_str + letter.upper()
    return new_str


def split_in_half(orig_string: str):
    half_index = int(len(orig_string) / 2)
    return orig_string[:half_index], orig_string[half_index:]


def remove_special_characters(orig_string: str):
    allowed = ascii_letters + digits + ' '
    new_str = ''
    for letter in orig_string:
        if letter in allowed:
            new_str = new_str + letter
    return new_str



if __name__ == '__main__':
    print(remove_special_characters('Thi§ is a test: test?'))