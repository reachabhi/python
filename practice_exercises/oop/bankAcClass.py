class BankAccount:

    bankbalance = 100000

    def __init__(self, name, balance=0.0):
        self.owner = name
        self.balance = balance
        
    def balance(self):
        return self.balance
        
    def deposit(self,amount):
        BankAccount.bankbalance += amount   #class variable-it does not require a self . self is only to refer to instance variables. It can be accessed using ClassName from inside all instance methods
        self.balance = self.balance + amount 
        return self.balance
    
    def withdraw(self,amount):
        BankAccount.bankbalance -= amount
        self.balance = self.balance - amount
        return self.balance



acct = BankAccount('Darcy')

print(acct.owner)
print(acct.balance)
acct.deposit(5000)
print(acct.balance)
print(BankAccount.bankbalance)
acct.withdraw(2000)
print(acct.balance)
print(BankAccount.bankbalance)
print(acct.bankbalance)  #It will GET the balance though it is a class variable but ideally we should implement in the class not to SET it to something

BankAccount.bankbalance = 200000 
acct.bankbalance = 200000 #It is allowed but it will not actually set the value to 200000. Instead use BankAccount.bankbalance = 200000 which actually does that
print(acct.bankbalance)
acct.deposit(5000)
print(acct.balance)
print(BankAccount.bankbalance)
acct.withdraw(2000)
print(acct.balance)

