class Account():
    owner = ""
    balance = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    
    def str(self):
        print(f"Owner: {self.owner}\nBalance: {self.balance}$")
    
    def deposit(self, count):
        self.balance += count
        print(f"Deposited: {count}$\nBalance: {self.balance}$")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawed: {amount}$\nBalance: {self.balance}$")
        else: 
            print(f"{self.balance}$ is less than {amount}$")
        

acc1 = Account("Adilet", 1768)
print(acc1)
acc1.deposit(50)
acc1.withdraw(2000)
print(acc1.balance)