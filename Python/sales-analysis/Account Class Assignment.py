class Account:
    def __init__(self):
        self.account_number = int(input("Enter account number: "))
        self.name = input("Enter name: ")
        self.balance = 0
        print("Account created successfully")
        
    def print_details(self):
        print("Account Details are")
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance: Rs.", self.balance)
        
    def deposit(self):
        amount = float(input("Enter the amount to deposit: Rs. "))
        self.balance += amount
        print(f"Rs. {amount} is deposted successfully")
        print(f"Current balance: Rs. {self.balance}")
        
    def withdraw(self):
        if self.balance > 0:
            amount = float(input("Enter the amount to withdraw: Rs. "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Rs. {amount} is withdrawn successfully")
                print(f"Current Balance: Rs. {self.balance}")
            else:
                print("Insufficient balance")              
        else:
            print("No balance to withdraw")
        
print("Welcome to Our Bank App")
a = Account()
while True:
    print("Enter v to view account details")
    print("Enter d to deposit an amount")
    print("Enter w to withdraw an amount")
    print("Enter e to exit")
    choice = input("Enter your choice: ")
    if choice == 'v':
        a.print_details()
    elif choice == 'd':
        a.deposit()
    elif choice == 'w':
        a.withdraw()
    elif choice == 'e':
        break
    else:
        print("Wrong choice entered")
print("Thank you for using our app")