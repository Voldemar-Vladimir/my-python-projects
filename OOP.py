class BankAccount:

    def __init__(self,owner="Владимир", balance=0):

        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        self.balance-=amount
        
    def __str__(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}"
    
class SavingsAccount(BankAccount):

    def __init__(self,owner="Владимир", balance=0,interest_rate=0):
        super().__init__(owner,balance)
        self.interest_rate=interest_rate

    def add_interest(self,interest_rate=0):
        self.balance+=self.balance/100*self.interest_rate
        
a = BankAccount("Олег", 500)
b = SavingsAccount("Олег", 500, 10)
print(a)
print(b)