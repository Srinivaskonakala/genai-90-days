class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
           self.balance -= amount

    def check_balance(self):
        return self.balance

b = BankAccount("Srinivas",1000)

b.deposit(500)
print("Balance after deposit:", b.check_balance())

b.withdraw(200)
print("Balance after withdrawal:",b.check_balance())
