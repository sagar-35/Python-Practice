class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Deposited Successfully. Current balance is {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} Withdraw Successfully. Current Balance is {self.balance}")
        else:
            print("Insuficient Balance! Please Try Again After Deposit Amount.")
    
    def show_amount(self):
        print(f"{self.owner}'s Accounts Balance is {self.balance}")
    
    def transfer_amount(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"{amount} Transfered Successfully to {other_account.owner}")
        else: 
            print("Insufficient Balance!")

acc1 = BankAccount("Sagar", 10000)
acc2 = BankAccount("Ratul", 8000)

acc1.transfer_amount(1000, acc2)
acc2.deposit(2000)
acc2.withdraw(500)
acc1.deposit(500)
acc1.show_amount()
acc2.show_amount()