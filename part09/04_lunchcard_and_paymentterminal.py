
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
             self.balance -= amount
             return True
        return False
        

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment >= 2.50:
            self.funds += 2.5
            self.lunches += 1
            return payment - 2.50
        return payment

    def eat_special(self, payment: float):
        if payment >= 4.30:
            self.funds += 4.3
            self.specials += 1
            return payment - 4.30
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >= 2.50:
            self.lunches += 1
            card.balance -= 2.50
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance >= 4.30:
            self.specials += 1
            card.balance -= 4.30
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        self.funds += amount




if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)