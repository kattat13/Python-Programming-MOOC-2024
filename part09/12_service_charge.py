class BankAccount:
    def __init__(self, name: str, account_no: str, balance: float):
        self.__name = name
        self.__account_no = account_no
        self.__balance = balance

    def __service_charge(self):
        # decreases the balance on the account by one percent
        self.__balance *= 0.99

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance


if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)