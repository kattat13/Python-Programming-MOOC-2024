# Write your solution here
atempts = 0
while True:
    pin = int(input("PIN: "))
    atempts += 1
    if pin == 4321:
        break
    print("Wrong")
if atempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {atempts} attempts")