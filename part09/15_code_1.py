class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'


class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
        self.curr_weight = 0

    def add_item(self, item: Item):
        if self.max_weight - self.curr_weight >= item.weight():
            self.items.append(item)
            self.curr_weight += item.weight()

    def print_items(self):
        for item in self.items:
            print(item)

    def weight(self):
        return self.curr_weight
    
    def heaviest_item(self):
        if len(self.items) == 0:
            return None
        heaviest_weight = 0
        heaviest_item = self.items[0]
        for item in self.items:
            if item.weight() > heaviest_weight:
                heaviest_weight = item.weight()
                heaviest_item = item
        return heaviest_item


    def __str__(self):
        if len(self.items) == 1:
            return f'{len(self.items)} item ({self.curr_weight} kg)'
        return f'{len(self.items)} items ({self.curr_weight} kg)'


class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.suitcases = []
        self.curr_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.max_weight - suitcase.weight() >= self.curr_weight:
            self.suitcases.append(suitcase)
            self.curr_weight += suitcase.weight()

    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(item)


    def __str__(self):
        if len(self.suitcases) == 1:
            return f'{len(self.suitcases)} suitcase, space for {self.max_weight - self.curr_weight} kg'
        return f'{len(self.suitcases)} suitcases, space for {self.max_weight - self.curr_weight} kg'



if __name__ == '__main__':
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()