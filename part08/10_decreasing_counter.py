class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.init_value = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value == 0:
            pass
        else:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.init_value


if __name__ == '__main__':
    counter = DecreasingCounter(2)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()