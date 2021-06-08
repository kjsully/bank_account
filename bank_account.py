class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print("insufficient funds: charging a $5 fee haha")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance - self.balance * self.int_rate
        return self

bob = BankAccount(0.01, 0)
fred = BankAccount(0.01, 0)

bob.deposit(500).deposit(500).deposit(500).withdraw(300).display_account_info()
fred.deposit(200).deposit(200).withdraw(150).withdraw(150).withdraw(150).withdraw(150).display_account_info()
