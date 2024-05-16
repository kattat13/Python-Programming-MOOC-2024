size = int(input("How many items: "))
numbers = []
i = 1 
while i <= size:
    item = int(input(f"Item {i}:"))
    numbers.append(item)
    i += 1
print(numbers)