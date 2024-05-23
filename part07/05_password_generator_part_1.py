from string import ascii_lowercase
from random import sample


def generate_password(length: int):
    return ''.join(sample(ascii_lowercase, length))