class User:
    def __init__(self, f_name, l_name, accbal):
        self.f_name = f_name
        self.l_name = l_name
        self.accbal = accbal


    def make_deposit(self, deposit):
        self.accbal += deposit
        return self

    def make_withdrawal(self, withdrawal):
        self.accbal -= withdrawal
        return self

    def show_accbal(self):
        print(f"${self.accbal}")
        return self

    def tranfer_money(self, transfer, transfer_to):
        self.accbal -= transfer
        transfer_to.accbal += transfer
        return self



chuck = User("Chuck","kendrick",1000000)
larry = User("James", "Cepak", 1000000)
mayla = User("Mayla", "Poppins", 100000000)

chuck.make_deposit(50000).make_deposit(25000).make_deposit(100000).show_accbal()

larry.make_deposit(80000).make_deposit(1200000).make_withdrawal(3000).make_withdrawal(50000).show_accbal()

mayla.make_deposit(100000000).make_withdrawal(1500).make_withdrawal(100).make_withdrawal(70).show_accbal()

chuck.tranfer_money(600, mayla)

larry.show_accbal()
chuck.show_accbal()
mayla.show_accbal()