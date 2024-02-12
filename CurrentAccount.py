from Account import Account

class CurrentAccount(Account):
    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if self.overdraft_limit + self.balance < amount:
            print("Insufficient Balance")
            return False
        else:
            self._balance -= amount
            return True
