numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))

    if index == -1:
        break
    if index < 0 or index >= len(numbers):
        print("Out of range")
        continue
    new_value = int(input("New value: "))
    numbers[index] = new_value
    print(numbers)