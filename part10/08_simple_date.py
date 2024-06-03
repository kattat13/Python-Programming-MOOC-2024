class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __add__(self, days):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year
        mult = new_day // 30
        if new_day > 30:
            new_month = self.month + mult
            new_day = new_day - mult * 30
        if new_month > 12:
            new_year += new_month//12
            new_month -= 12 * (new_month//12)
        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, another):
        if self > another:
            diff_years = self.year - another.year
            diff_months = self.month - another.month
            diff_days = self.day - another.day
        elif self < another:
            diff_years = another.year - self.year
            diff_months = another.month - self.month
            diff_days = another.day - self.day
        else:
            return 0
        return diff_days + diff_months * 30 + diff_years * 360


    def __eq__(self, another):
        return f'{self.day}.{self.month}.{self.year}' == f'{another.day}.{another.month}.{another.year}'

    def __ne__(self, another):
        return not self.__eq__(another)
        
    def __gt__(self, another):
        if self.year != another.year:
            return self.year > another.year
        elif self.month != another.month:
            return self.month > another.month
        else:
            return self.day > another.day

    def __lt__(self, another):
        greater = self > another
        return not greater
