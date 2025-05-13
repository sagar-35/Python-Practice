# Creating the BankAccount class
class BankAccount:
    # Constructor: sets the account owner and initial balance
    def __init__(self, owner, balance):
        self.owner = owner # Assign owner's name to the object
        self.blance = balance # Assign initial balance to the object
    
    # Method for depositing money
    def deposit(self, amount): 
        self.blance += amount   # Add the deposit amount to current balance
        print(f"{amount} Deposited Successfully. Current Balance is {self.blance}")
    
    # Method for withdrawing money
    def withdraw(self, amount):
        if amount <= self.blance: 
            self.blance -= amount # Subtract the withdrawal amount
            print(f"{amount} withdraw succesfully. Current Balance is {self.blance}")
        else:
            print("Account has not enough money!")

    # Method to show current balance
    def show_balance(self):
        print(f"{self.owner}'s Account Balance is {self.blance}")

# ✅ Creating an object of BankAccount
acc1 = BankAccount("Sagar", 5000)

# ✅ Calling methods
acc1.deposit(6000)  # Deposit 6000
acc1.withdraw(1000) # Withdraw 1000
acc1.show_balance() # Show final balance