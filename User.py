from CurrentAccount import CurrentAccount 
from SavingsAccount import SavingsAccount
from hash import hash_password

class User:
    
    def __init__(self, name, password):
        self.name = name
        self.__password = hash_password(password)
        self.numbers_savings_account = 0
        self.numbers_current_account = 0
        self.savings_Account = None
        self.current_Account = None
    
    @property
    def password(self):
        return self.__password    
    
    def create_savings_acc(self):
        if self.numbers_savings_account==0:
            self.savings_Account = SavingsAccount(self.name, 3.5)
            self.numbers_savings_account+=1
            return True
        else:
            print("One user can only create 1 savings account")
            return False
            
    def create_current_acc(self):
        if self.numbers_current_account==0:
            overdraft_limit = int(input("Enter Overdraft Limit: "))
            self.current_Account = CurrentAccount(self.name, overdraft_limit)
            return True
        else:
            print("One user can only create 1 current account")
            return False