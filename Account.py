import uuid

class Account:
    def __init__(self, account_holder):
        self.account_number = str(uuid.uuid4());
        self.account_holder = account_holder
        self.__balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance+=amount
            # print(f"Rs.{amount} deposited successfully.")
            return True
        else:
            print("Invalid deposit amount. Please enter a positive amount.")
            return False
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawn amount. Please enter a positive amount.")
            return False
        elif self.__balance < amount:
            print("Insufficient Balance")
            return False
        else:
            self.__balance-=amount
            # print(f"Rs.{amount} credited from the account successfully.")
            return True
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def _balance(self, amount):
        self.__balance = amount