#Base class 
class BankAccount: 
    
    #variables
    

    
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount): 
        self.balance += amount 

    def withdraw(self, amount): 
        if amount <= self.balance: 
            self.balance -= amount
        else: 
            print("Insifficient funds")
    

    def account_info(self): 
        return f"Account holder: {self.account_holder}, Balance ${self.balance:.2f}"
    

#Derived Class1  
class SavingsAccount(BankAccount): 

    #Variables
    interest_rate = 0.02     

    #Methods
    def apply_interest(self): 
        self.balance *= (1 + SavingsAccount.interest_rate)


#Derived Class2 
class CheckingAccount(BankAccount): 
    #attributes
    transaction_fee = 1 

    #Methods:
    def withdraw(self, amount) : 
    
        if amount <= (self.balance - CheckingAccount.transaction_fee): 
            #Withdraw the amount and transaction fee from the balance
            self.balance -= (amount+CheckingAccount.transaction_fee)
        else: 
            print("Insifficient funds")
        
 

SA1 = SavingsAccount("George")
SA1.deposit(100)
print(SA1.balance)
SA1.apply_interest()
print(SA1.balance)
print(SA1.account_info())


'''
BA1 = BankAccount("Frederic")
BA1.deposit(100)
print(BA1.balance)
BA1.withdraw(50)
print(BA1.balance)

CA1 = CheckingAccount("Daniel")
CA1.deposit(100)
print(CA1.balance)
CA1.withdraw(50)
print(CA1.balance)
'''
