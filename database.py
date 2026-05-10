 

# BANKING DATABASE MANAGEMENT SYSTEM

import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="akshat@123",
    database="Bank"
)

cursor = mydb.cursor()


def createcustomertable():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers
    (
        user VARCHAR(20),
        password VARCHAR(20),
        name VARCHAR(20),
        age INTEGER,
        city VARCHAR(20),
        balance INTEGER NOT NULL,
        account_number INTEGER,
        status BOOLEAN
    )
    """)

    mydb.commit()


def db_query(query):

    cursor.execute(query)

    try:
        result = cursor.fetchall()
        return result

    except:
        return None


if __name__ == "__main__":
    createcustomertable()