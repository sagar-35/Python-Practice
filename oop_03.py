class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposite(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully. Current Balance is {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} Withdraw Successfully. Current Balance is {self.balance}")
        else:
            print("Not Enough Money!")
    
    def show_balance(self):
        print(f"{self.owner}'s account balance is {self.balance}")


acc1 = BankAccount("Sagar", 5000)

acc1.show_balance()
acc1.deposite(300)
acc1.withdraw(2500)
acc1.deposite(10000)   
        
        
    
