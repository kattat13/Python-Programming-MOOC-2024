class NumberStats:
    def __init__(self):
        self.numbers = []
        self.how_many = 0

    def add_number(self, number: int):
        self.how_many += 1
        self.numbers.append(number)

    def count_numbers(self):
        return self.how_many
    
    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.how_many == 0:
            return 0
        else:
            avg = sum(self.numbers) / self.how_many
            return avg


numbers = NumberStats()
evens   = NumberStats()
odds    = NumberStats()

while True:
    user = int(input('Please type in integer numbers: '))

    if user == -1:
        print('Sum of numbers:', numbers.get_sum())
        print('Mean of numbers:', numbers.average())
        print('Sum of even numbers:', evens.get_sum())
        print('Sum of odd numbers:', odds.get_sum())
        break
    else:
        numbers.add_number(user)
        if user % 2 == 0:
            evens.add_number(user)
        else:
            odds.add_number(user)


