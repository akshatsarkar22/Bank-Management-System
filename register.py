# user Registration Signup and signIn
 

from database import db_query
from Customers import *
from bank import Bank
import random


def Signup():
    username = input("Create Username: ")
    
    temp = db_query(f"SELECT user FROM Customers WHERE user = '{username}';")
    
    
    if temp :
        print("Username Already Exists")
        Signup()
    else:
        print("Username Available Please Proceed")
        password = input("Enter Your Password:  ")
        name = input("Enter your Name: ")
        age = input("Enter your age: ")
        city = input("Enter your City: ")

        while True:
            account_number = random.randint(10000000 , 99999999)

            temp = db_query(f"SELECT account_number FROM Customers WHERE account_number= '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break
        # temp = db_query(f"")


        cobj = Customers(username , password,name,age , city , account_number)
        cobj.createuser()
        bobj = Bank(username,account_number)
        # bobj.create_transaction_table()

def SignIn():
 
    username = input("Enter Username: ")

    temp = db_query(
        f"SELECT user FROM Customers WHERE user = '{username}';"
    )

    if temp:

        password = input(
            f"Welcome {username.capitalize()}, Enter Password: "
        )

        temp = db_query(
            f"SELECT password FROM Customers WHERE user = '{username}';"
        )

        if temp[0][0] == password:
            print("Login Successful")
            return username

        else:
            print("Wrong Password")

    else:
        print("Enter correct Username")
