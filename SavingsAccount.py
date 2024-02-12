from Account import Account

class SavingsAccount(Account):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.__interest_rate = interest_rate
        
    @property
    def interest_rate(self):
        return self.__interest_rate
    
    def deposit(self, amount):
        if amount > 0:
            new_amount = self.balance + (amount * (1+self.interest_rate/100))
            self._balance = new_amount
            return True
        else:
            print("Invalid deposit amount. Please enter a positive amount.")
            return False
