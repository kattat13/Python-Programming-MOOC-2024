
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, area: int):
        self.width = area
        self.height = area

    def __str__(self):
        return f"square {self.width}x{self.height}"

    def area(self):
        return self.width * self.height