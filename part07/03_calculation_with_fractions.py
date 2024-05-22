from fractions import Fraction


def fractionate(amount: int):
    result = []
    for n in range(amount):
        result.append(Fraction(1, amount))
    return result