class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return self.__balance

        self.__balance += amount

        return self.__balance

    def withdraw(self,amount):
        if amount > self.__balance:
            print('Insufficient balance')
            return self.__balance
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

## inheritance
class SavingAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount

        return self.balance,interest_amount        

account_holder = BankAccount('Ronak', 50000)