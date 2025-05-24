class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private attributes
    
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited, now current balance is {self.__balance}.")
        else:
            print("Invalid Amount!")
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print(f"{amount} withdraw successfully. Current Balance is {self.__balance}.")
        else:
            print("Insufficent Balance! Pleace try again.")


    def get_balance(self):
        return self.__balance
    
acc1 = BankAccount("Sagar", 70000)
print(f"Balance Inquery: {acc1.get_balance()}")
acc1.deposite(1500)
acc1.withdraw(500)
print(f"Balance Inquery: {acc1.get_balance()}")

        