from string import ascii_lowercase, digits
from random import sample, randint


def generate_strong_password(length: int, numbers: bool, special: bool):
    password = sample(ascii_lowercase, length)
    
    if numbers:
        num_index = randint(0, length-1)
        password[num_index] = sample(digits, 1)[0]
    if special:
        specials = ['!', '?', '=', '+', '-', '(', ')', '#']
        spec_index = randint(0, length-1)
        if numbers:
            while spec_index == num_index:
                spec_index = randint(0, length-1)
        password[spec_index] = sample(specials, 1)[0]
    return ''.join(password)


if __name__ == "__main__":
    print(generate_strong_password(8, False, False))
