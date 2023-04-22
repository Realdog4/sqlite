import sqlite3
from faker import Faker

fake = Faker()

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

try:
    cur.execute("CREATE TABLE Customers(name, address, email)")
    for x in range(0, 11):
        names = fake.first_name()
        address = fake.address()
        email = fake.email()
        cur.execute("""
        INSERT INTO Customers(name, address, email) VALUES (?, ?, ?)
    """, (names, address, email))
except:
    for x in range(0, 11):
        names = fake.first_name()
        address = fake.address()
        email = fake.email()
        cur.execute("""
        INSERT INTO Customers(name, address, email) VALUES (?, ?, ?)
    """, (names, address, email))
con.commit()
con.close()




