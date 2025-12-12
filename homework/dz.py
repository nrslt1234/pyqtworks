class Finance:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, dep):
        self.balance += dep

    def withdraw(self, wd):
        if wd <= self.balance:
            self.balance -= wd
        else:
            print("Недостаточно средств")

class Account(Finance):
    def __init__(self, balance, account_number):
        super().__init__(balance)
        self.account_number = account_number

    def deposit(self, dep):
        super().deposit(dep)

    def withdraw(self, wd):
        super().withdraw(wd)

class Investment(Finance):
    def __init__(self, balance, portfolio):
        super().__init__(balance)
        self.portfolio = portfolio

    def deposit(self, dep):
        super().deposit(dep)

    def withdraw(self, wd):
        super().withdraw(wd)

class CreditCard(Finance):
    def __init__(self, balance, credit_limit):
        super().__init__(balance)
        self.credit_limit = credit_limit

    def deposit(self, dep):
        super().deposit(dep)

    def withdraw(self, wd):
        if self.balance + self.credit_limit >= wd:
            self.balance -= wd
        else:
            print("Недостаточно средств")



account = Account(1000, "12345")
investment = Investment(5000, "Портфель Акции")
credit_card = CreditCard(2000, 5000)

account.deposit(500)
account.withdraw(200)
investment.deposit(1000)
investment.withdraw(800)
credit_card.deposit(300)
credit_card.withdraw(2500)

print(account.balance, account.account_number)
print(investment.balance, investment.portfolio)
print(credit_card.balance, credit_card.credit_limit)