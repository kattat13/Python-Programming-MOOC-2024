
class Task:
    _id = 0
    @classmethod
    def generate_id(cls):
        Task._id += 1
        return Task._id

    def __init__(self, description: str, programmer: str, workload: int, finished=False):
        Task._id += 1
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.finished = finished
        self.id = Task.generate_id()

    def __str__(self) -> str:
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {"FINISHED" if self.finished else "NOT FINISHED"}'

    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return list(set([order.programmer for order in self.orders]))

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError()
    
    def finished_orders(self):
        return [order for order in self.orders if order.finished]
    
    def unfinished_orders(self):
        return [order for order in self.orders if order.finished == False]
    
    def status_of_programmer(self, programmer: str):
        num_finished = 0
        num_unfinished = 0
        sum_finished = 0
        sum_unfinished = 0
        programmer_found = False
        for order in self.orders:
            if order.programmer == programmer:
                programmer_found = True
                if order.finished:
                    num_finished += 1
                    sum_finished += order.workload
                else:
                    num_unfinished += 1
                    sum_unfinished += order.workload
        if not programmer_found:
            raise ValueError()
        return num_finished, num_unfinished, sum_finished, sum_unfinished
    


if __name__ == '__main__':
    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    t.add_order("program mobile gane", "Eric", 5)
    t.mark_finished(1)
    t.mark_finished(2)
    t.all_orders()