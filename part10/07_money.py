
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def _string_helper(self):
        return f"{self._euros}.{self._cents:02d}"
    
    def __str__(self):
        return f'{self._string_helper()} eur'
    
    def __eq__(self, another):
        return self._string_helper() == another._string_helper()
    
    def __gt__(self, another):
        return self._string_helper() > another._string_helper()

    def __lt__(self, another):
        return self._string_helper() < another._string_helper()

    def __ne__(self, another):
        return self._string_helper() != another._string_helper()
    
    def __add__(self, another):
        new_euros = self._euros + another._euros
        new_cents = self._cents + another._cents
        if new_cents >= 100:
            new_euros += 1
            new_cents -= 100
        return Money(new_euros, new_cents)

    def __sub__(self, another):
        if self._cents < another._cents:
            self._cents += 100
            self._euros -= 1
        new_euros = self._euros - another._euros
        new_cents = self._cents - another._cents
        if new_cents < 0 or new_euros < 0:
            raise ValueError('a negative result is not allowed')
        return Money(self._euros - another._euros, self._cents - another._cents)


if __name__ == '__main__':
    money1 = Money(2, 0)
    money2 = Money(1, 35)

    print(money1 - money2)