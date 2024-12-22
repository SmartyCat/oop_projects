class BankAccount:
    """Класс для аккаунта банка"""

    def __init__(self, owner, balance=0):
        """Инициализация имени владельца и балана"""
        self.history = []
        self.owner = owner
        self.check_balance(balance)
        self.balance = balance

    def deposite(self, amount):
        """Метод для пополнени счета"""
        if amount <= 0:
            raise ValueError("You need to use integers bigger than 0")
        self.balance += amount
        self.history.append(f"Deposited {amount}. Your balance is {self.balance}")

    def withdraw(self, amount):
        """Метод для снятия счета"""
        self.check_amount(self.balance, amount)
        self.balance -= amount
        self.history.append(f"Withdraw {amount}. Your balance is {self.balance}")

    def transfer(self, amount, other_account):
        "Метод для первода денег"
        self.check_amount(self.balance, amount)
        other_account.balance += amount
        self.balance -= amount
        self.history.append(
            f"Transfer {amount} on {other_account.owner}. Your balance is {self.balance}"
        )
        other_account.history.append(
            f"Transfer from {self.owner}.Your balance is {other_account.balance}"
        )

    def apply_interest(self, p):
        """Метод начисления процентов. Проценты принимаються в виде десятичной дроби"""
        if not isinstance(p, (int, float)) or p < 0:
            raise ValueError
        interest = self.balance * p

        self.check_balance(self.balance + interest)
        self.balance += interest
        self.history.append(f"Applied interest rate: {p}")

    def show_history(self):
        """Метод для отобржения истории"""
        return self.history

    @staticmethod
    def check_amount(dep, amount):
        """Метод для проверки счета"""
        if dep < amount:
            raise ValueError("Amount must ve less than balance")

    @staticmethod
    def check_balance(b):
        """Метод для проверки баланса"""
        if b > 1000000:
            raise ValueError("you cant keep over milion")
        elif b < 0:
            raise ValueError("Balance cannot be negative")

    def __str__(self):
        return f"{self.owner}, {self.balance}"
