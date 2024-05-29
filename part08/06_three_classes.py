class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries


class Customer:
    def __init__(self, c_id: str, balance: float, discount: int) -> None:
        self.id = c_id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional