class BankAccount:
    def __init__(self, account_name, int_rate, balance):
        self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print("insufficient funds; charging a $5 feee \n",
            "new balance:", self.balance)
            return self
        else:
            self.balance -= amount
            return self
# ---------------------------------------------------------------------------- #

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {}

    def new_account(self, account_title, int_rate = .02, balance = 0):
        self.account[account_title] = BankAccount(account_title, int_rate, balance)
        return self

    def transfer_money_self(self, account1, amount, account2):
        if amount <= self.account[account1].balance:
            self.account[account1].withdraw(amount)
            self.account[account2].deposit(amount)
        else:
            print("error: insufficient funds")
            pass

    def transfer_money_other(self, account1, amount, other_user, account2):
        if amount <= self.account[account1].balance:
            self.account[account1].withdraw(amount)
            other_user.account[account2].deposit(amount)
        else:
            print("error: insufficient funds")
            pass


    def account_balances(self):
        for key, value in self.account.items():
            print(
                key, "info:\n"
                'account balance:', value.balance, '\n',
            )  

user_benji = User("benji hix", 'benji.hix@outlook.com')
user_benji.new_account('chime_bank').new_account('chase_bank')


user_benji.account['chime_bank'].deposit(100)
user_benji.transfer_money_self('chime_bank', 50, 'chase_bank')

user_liz = User('liz hix', 'liz.hix@outlook.com')
user_liz.new_account('sofi_bank').new_account('capital_one_bank')

user_benji.transfer_money_other('chime_bank', 25, user_liz, 'sofi_bank')
user_benji.account_balances()
user_liz.account_balances()