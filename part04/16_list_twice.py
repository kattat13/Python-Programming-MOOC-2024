lst = []

while True:
    number = int(input("New item: "))
    if number == 0:
        break
    lst.append(number)
    print(f"The list now: {lst}")
    print(f"The list in order: {sorted(lst)}")
print("Bye!")