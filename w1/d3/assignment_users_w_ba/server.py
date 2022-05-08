class User:
    def __init__(self, f_name, l_name ):
        self.f_name = f_name
        self.l_name = l_name
        self.account = BankAccounts(int_rate=.01, balance=0)

    def make_deposit(self, deposit):
        self.account.balance += deposit

    def make_withdrawal(self, withdrawal):
        self.account.balance -= withdrawal

    def show_accbal(self):
        print(f"${self.account.balance}")

    def tranfer_money(self, transfer, transfer_to):
        self.account.balance -= transfer
        transfer_to.account.balance += transfer

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


