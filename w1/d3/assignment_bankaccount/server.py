class BankAccounts:
    balance=0
    
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        BankAccounts.balance+=balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdrawal(self, amount):
        self.balance-=amount
        return self

    def display_account_info(self):
        print(f"{self.int_rate}, ${self.balance} ")
        return self

    def yield_int(self):
        self.balance+=(self.balance * self.int_rate)
        return self

    @classmethod
    def total_bal(cls):
        print(f"The bank has a total of ${cls.balance} deposited year to date.")

bamlak=BankAccounts(0.1, 2500000)
tesfaye=BankAccounts(.06, 25000)

bamlak.deposit(30000).deposit(50000).deposit(100000).withdrawal(10000).yield_int().display_account_info()
tesfaye.deposit(10000).deposit(6000000).withdrawal(500000).withdrawal(50000).withdrawal(25000).withdrawal(75000).yield_int().display_account_info()

BankAccounts.total_bal()