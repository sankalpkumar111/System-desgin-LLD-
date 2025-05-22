from abc import ABC ,abstractmethod
class Depositaccount(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass

class Withdrwalaccount(ABC):
    @abstractmethod
    def withdrawal(self,amount):
        pass

class CurrentAccount(Withdrwalaccount,Depositaccount):
    def __init__(self,balance):
        self.balance=balance
    def current_acc_balance(self,balance):
        self.balance=0
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposit amount {amount} RS in Current account. Current balance is {self.balance} RS")
    
    def withdrawal(self, amount):
        if(self.balance>=amount):
            self.balance=self.balance-amount
            print(f"Withdrawal amount {amount} RS in Current account. Current balance is {self.balance} RS")
        else:
            print("Insufficient balance")

class SavingAccount(Withdrwalaccount,Depositaccount):
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self, amount):
        self.balance=self.balance+amount
        print(f"Deposit amount {amount} RS in Saving account. Current balance is {self.balance} RS")
    
    def withdrawal(self, amount):
        if(self.balance>=amount):
            self.balance=self.balance-amount
            print(f"Withdrawal amount {amount} RS in Saving account. Current balance is {self.balance} RS")
        else:
            print("Insufficient balance")


class Fixed_AC(Depositaccount):
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposited: {amount} in fixed term long. New Balance: {self.balance}")

class BankClient:
    def __init__(self,withdrawable_accounts, deposit_only_accounts):
        self.withdrawable_accounts=withdrawable_accounts
        self.deposit_only_accounts=deposit_only_accounts
    
    def processTransaction(self):
            for acc in self.withdrawable_accounts:
                acc.deposit(1000)
                acc.withdrawal(500)
            for acc in self.deposit_only_accounts:
                acc.deposit(5000)


ca = CurrentAccount(1000)
sa = SavingAccount(2000)
fd = Fixed_AC(5000)

client = BankClient(
        withdrawable_accounts=[ca, sa],
        deposit_only_accounts=[fd]
    )

client.processTransaction()
