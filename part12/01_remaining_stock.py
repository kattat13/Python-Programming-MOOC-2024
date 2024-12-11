def sort_by_remaining_stock(items: list):

    def order_by_remaining_stock(items: tuple):
        return items[-1]
    
    return sorted(items, key=order_by_remaining_stock)