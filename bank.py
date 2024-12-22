class BankAccount:

    def __init__(self, owner, balance=0):
        self.history = []
        self.owner = owner
        self.check_balnce(balance)
        self.balance = balance

    def deposite(self, amount):
        if amount <= 0:
            raise ValueError("You need to use ntegers bigger than 0")
        self.balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        self.check_amount(self.balance, amount)
        self.balance -= amount
        self.history.append(f"Withdraw {amount}")

    def transfer(self, amount, other_account):
        self.check_amount(self.balance, amount)
        other_account.balance += amount
        self.balance -= amount
        self.history.append(f"Transfer {amount} on {other_account.owner}")

    def apply_interest(self, p):
        if isinstance(p, (int, float)) is not True or p < 0:
            raise ValueError
        interest = self.balance * p
        self.balance += interest

    def show_history(self):
        return self.history

    @staticmethod
    def check_amount(dep, amount):
        if dep < amount:
            raise ValueError("Amount must ve less than balance")

    @staticmethod
    def check_balance(b):
        if b > 1000000:
            raise ValueError("you cant keep over milion")
        elif b < 0:
            raise ValueError("Balance cannot be negative")

    def __str__(self):
        return f"{self.owner}, {self.balance}"
