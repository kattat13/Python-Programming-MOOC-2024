
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]
    
    def __iter__(self):
        self.n = 0
        # the method returns a reference to the object itself 
        # as the iterator is implemented within the same class def
        return self
    
    def __next__(self):
        if self.n < len(self.products):
            # select the current item from the list within the object
            prod = self.products[self.n]
            # increase the counter
            self.n += 1
            # return the current item
            return prod
        else:
            # all products have been traversed
            raise StopIteration


if __name__ == '__main__':
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")
        