class User:
    def __init__(self,name):
        self.name = name
        self.account_balance = 100

    def make_withdrawal(self,amount):
        self.account_balance -= amount 

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self,transfer_to,amount):
        self.account_balance-=amount 
        transfer_to.account_balance+=amount

user1=User('Chuck')
user2=User('Larry')

user1.transfer_money(user2,100)

print(user2.account_balance)
print(user1.account_balance)