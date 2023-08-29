class Bank_Account:
    
    all_accounts = []

    def __init__(self, account_name, int_rate, balance): 
        self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_accounts.append(self)

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

    def display_account_info(self):
        print(
            self.account_name,"info:\n",
            "interest rate:", self.int_rate,"%\n",
            "balance:", self.balance, "\n",
        )
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate / 100)
            return self
        else:
            print("no yield interest")
            return self

    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(
                account.account_name, "info:\n"
                'account balance:', account.balance, '\n',
                'account interest rate:', account.int_rate, '\n'
            )  
# ---------------------------------------------------------------------------- #

account_chime = Bank_Account('chime', 2, 500)
account_sofi = Bank_Account('sofi', 4.5, 4000)

account_chime.deposit(50).deposit(50).deposit(50).withdraw(5).yield_interest().display_account_info()
account_sofi.deposit(1000).deposit(1000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()

# bonus
Bank_Account.all_accounts_info()