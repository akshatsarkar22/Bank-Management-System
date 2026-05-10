 

# Bank Services
from database import *
import datetime

class Bank:

    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        self.create_transaction_table()



    def create_transaction_table(self):
        db_query(f"""CREATE TABLE IF NOT EXISTS {self.__username}_transaction (
            timedate VARCHAR(30),
            account_number INTEGER,
            remarks VARCHAR(30),
            amount INTEGER
        )""")

    def balanceenquiry(self):
        temp =db_query(f"SELECT balance,account_number FROM Customers WHERE user = '{self.__username}'")
        print(f"{self.__username} balance is {temp[0][0]}")


    def deposit(self, amount):
        temp =db_query(f"SELECT balance,account_number FROM Customers WHERE user = '{self.__username}'")
        test = amount + temp[0][0]
        db_query(f"UPDATE Customers SET balance = '{test}' WHERE user = '{self.__username}';")
        self,self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                f"'{datetime.datetime.now()}',"
                f"'{self.__account_number}',"
                f"'Amount Deposit',"
                f"'{amount}'"
                f")")
        print(f"{self.__username} Amount is Successfully Depositted into Your Amount {self.__account_number}")


    def withdraw(self, amount):
        temp =db_query(f"SELECT balance,account_number FROM Customers WHERE user = '{self.__username}'")
        if amount > temp [0][0]:
           print("Insufficent Balance Please Deposit Money")
        else:
            test= temp[0][0] - amount
            db_query(f"UPDATE Customers SET balance = '{test}'WHERE user = '{self.__username}';")
            self.balanceenquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                f"'{datetime.datetime.now()}',"
                f"'{self.__account_number}',"
                f"'Amount Withdraw',"
                f"'{amount}'"
                f")")
        print(f"{self.__username} Amount is Successfully Withdram From Your Amount {self.__account_number}")


    def fundtransfer(self, receive,amount):
        temp =db_query(f"SELECT balance,account_number FROM Customers WHERE user = '{self.__username}'")
        if amount > temp [0][0]:
           print("Insufficent Balance Please Deposit Money")
        else:
            temp2 =db_query(f"SELECT balance,account_number FROM Customers WHERE user = '{self.__username}'")
            test1 = temp[0][0] - amount
            test2 = amount + temp2[0][0]
            db_query(f"UPDATE Customers SET balance = '{test1}'WHERE user = '{self.__username}';")
            db_query(f"UPDATE Customers SET balance = '{test2}'WHERE account_number = '{receive}';")
            receiver_username = db_query(f"SELECT user FROM Customers where account_number = '{receive}';")
            self.balanceenquiry()
            db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                f"'{datetime.datetime.now()}',"
                f"'{self.__account_number}',"
                f"'Fund Transfer From {self.__account_number}',"
                f"'{amount}'"
                f")")

            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                f"'{datetime.datetime.now()}',"
                f"'{self.__account_number}',"
                f"'Fund Transfer -> {receive}',"
                f"'{amount}'"
                f")")
        print(f"{self.__username} Amount is Successfully Transaction From Your Amount {self.__account_number}")