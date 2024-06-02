class ListHelper:
    def __init__(self) -> None:
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        element = my_list[0]
        frequency = 1
        for el in my_list:
            if my_list.count(el) > frequency:
                element = el
                frequency = my_list.count(el)
        return element

    @classmethod
    def doubles(cls, my_list: list):
        doubles = []
        for el in my_list:
            if my_list.count(el) > 1 and el not in doubles:
                doubles.append(el)
        return len(doubles)
        