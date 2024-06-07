
class LotteryNumbers:
    def __init__(self, week_number: int, seven_numbers: list):
        self.week_number = week_number
        self.seven_numbers = seven_numbers

    def number_of_hits(self, numbers: list):
        return sum([1 for n in numbers if n in self.seven_numbers])
    
    def hits_in_place(self, numbers: list):
        return [i if i in self.seven_numbers else -1 for i in numbers]