class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient balance')
            return self.balance
        self.balance -= amount

        return self.balance

holder = BankAccount('Ronak', 50000)

print('Before deposit balance :',holder.balance)

holder.deposit(25000)

print('After deposit balance :',holder.balance)

holder.withdraw(80000)

print('After Withdrawl balance :', holder.balance)
