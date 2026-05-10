from register import *
from bank import *

status = False
print("Welcome to Akshat Banking Project")

while True:
    try:
        register = int(input(
            "\n1. SignUp"
            "\n2. SignIn"
            "\nEnter Your Choice: "
        ))

        if register == 1:
            Signup()

        elif register == 2:
            user = SignIn()

            if user:
                status = True
                break
            else:
                print("Login Failed. Try Again.")

        else:
            print("Please Enter Valid Input from Option")

    except ValueError:
        print("Invalid Input Try Again With Number")


account_number = db_query(f"SELECT account_number FROM Customers WHERE user = '{user}';")

if not account_number:
    print("Account number not found.")
    status = False

while status:
    print(f"\nWelcome {user.capitalize()} Choose Your Banking Service")

    try:
        facility = int(input(
            "\n1. Balance Enquiry"
            "\n2. Cash Deposit"
            "\n3. Cash Withdraw"
            "\n4. Fund Transfer"
            "\nEnter Your Choice: "
        ))

        if facility == 1:
            bobj = Bank(user, account_number[0][0])
            bobj.balanceenquiry()

        elif facility == 2:
            try:
                amount = int(input("Enter Amount to Deposit: "))
                bobj = Bank(user, account_number[0][0])
                bobj.deposit(amount)
                mydb.commit()
                status=False
            except ValueError:
                print("Enter Valid Input ie. Number")

        elif facility == 3:
            try:
                amount = int(input("Enter Amount to Withdraw: "))
                bobj = Bank(user, account_number[0][0])
                bobj.withdraw(amount)
                mydb.commit()
                status=False
            except ValueError:
                print("Enter Valid Input ie. Number")

        elif facility == 4:
            try:
                receive = int(input("Enter Receiver Account Number: "))
                amount = int(input("Enter Money to Transfer: "))
                bobj = Bank(user, account_number[0][0])
                bobj.fundtransfer(receive, amount)
                mydb.commit()
                status=False
            except ValueError:
                print("Enter Valid Input ie. Number")

        else:
            print("Please Enter Valid Input from Option")

    except ValueError:
        print("Invalid Input Try Again With Number")