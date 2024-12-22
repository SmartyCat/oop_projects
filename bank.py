class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposite(self, amount):
        if amount <= 0:
            raise ValueError("You need to use ntegers bigger than 0")
        self.balance += amount

    def withdraw(self, amount):
        self.check_amount(self.balance, amount)
        self.balance -= amount

    def transfer(self, amount, other_account):
        self.check_amount(self.balance, amount)
        other_account.balance += amount
        self.balance -= amount

    @staticmethod
    def check_amount(dep, amount):
        if dep < amount:
            raise ValueError("Amount must ve less than balance")

    def __str__(self):
        return f"{self.owner}, {self.balance}"
