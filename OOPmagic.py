class Money:

    def __init__(self,amount):
        self.amount=amount
        self.tasks=[]

    def __str__(self):
        return f"Баланс = {self.amount} руб."
    
    def __eq__(self, other):
        return self.amount==other.amount
    
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __len__(self):
        return self.amount
    
a = Money(500)
b = Money(300)
print(a)           # 500 руб.
print(a == b)      # False
c = a + b
print(c)           # 800 руб.
print(len(c))      # 800