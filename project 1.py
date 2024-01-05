

# MINI PROJECT

class BankAccount:
    def __init__(self,account_number, pin, balance = 0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def display_baalnce (self):
        print("display_balance",self.balance)

    def deposit (self,amount):
        if amount > 0:
            self.balance += amount
            print("deposit",self.balance)
            self.display_baalnce()
        else:
            print("invalid amount for deposit. ")

    def withdraw (self,amount):
        if amount > 0 and amount <=self.balance:
            self.balance -= amount
            print("withdraw",self.balance)
            self.display_baalnce()

        else:
            print("invalid amount for withdraw. ")

def main():
    account =BankAccount(account_number="123456789", pin="12345", balance=10000)

    enter_account_number =input("Enter Your Account Number: ")
    enter_pin =input("Enter Your Pin: ")

    if enter_account_number == account.account_number and enter_pin == account.pin:
        print("Login successfully.")
        while True:
            print("1.display balance")
            print("2.deposit")
            print("3.withdraw")
            print("4.exit")

            choice = input("Enter your choice Number (1 to 4) :  ")

            if choice == "1":
                account.display_baalnce()
            elif choice == "2":
                amount = float(input("Enter amount for deposit: "))
                account.deposit(amount)
            elif choice == "3":
                amount =float(input("Enter amount for withdraw: "))
                account.withdraw(amount)
            elif choice =="4":
                print("exit. ")
                break
            else:
                print("exit to the program good by. ")
    else:
        print("Invalid account number or pin  login failed please try again.")

main()