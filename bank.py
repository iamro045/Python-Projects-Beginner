class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("💰 Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Not enough balance")
        self.balance -= amount
        print("💸 Withdrawn:", amount)

acc = BankAccount("Rohit", 5000)

try:
    acc.withdraw(6000)
except InsufficientFunds as e:
    print(e)
