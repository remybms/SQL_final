##
# @author Yamao Cuzou <yamao.cuzou@ynov.com>
 # @file Description
 # @desc Created on 2023-10-17 12:53:19 pm
 # @copyright Cuzou Corporation
 #

import sqlite3
import random
import numpy as np

# import csv
 
# with open("Dictionary/Prenoms.csv", "r") as fsrce:
#     with open("PrenomsTable.csv", "w", newline='') as fdest:
#         my_reader = csv.reader(fsrce, delimiter = ';')
#         my_writer = csv.writer(fdest, delimiter = ';')
#         for ligne in my_reader:
#             my_writer.writerow([ligne[0]])

conn = sqlite3.connect('Database/tests.db')
cursor = conn.cursor()

# df = pandas.read_csv('Dictionary/Prenom.csv', header=2)
# print(df['aapeli'])

def generate_clients():
    clients = ["USA", "Canada", "UK", "Australia", "Germany", "France", "Japan", "China", "India", "Brazil", "Mexico"]
    return random.choice(clients)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees
    (
        idEmployee INTEGER NOT NULL PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        PhoneNumber VARCHAR(50),
        Salary INTEGER NOT NULL,
        HireDate DATE,
        BirthDate DATE
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS departmentsType
    (
        idDepartmentType INTEGER NOT NULL PRIMARY KEY,
        Title VARCHAR(50)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments
    (
        idDepartment INTEGER NOT NULL PRIMARY KEY,
        Name VARCHAR(50),
        idType INTEGER NOT NULL,
        FOREIGN KEY(idType) REFERENCES departmentsType(idDepartmentType)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts
    (
        idPost INTEGER NOT NULL PRIMARY KEY,
        Name VARCHAR(50),
        Description VARCHAR(150)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employeeDepartments
    (
        idEmployeeDepartement INTEGER NOT NULL PRIMARY KEY,
        idEmployee INTEGER NOT NULL,
        idPost INTEGER NOT NULL,
        idDepartments INTEGER NOT NULL,
        FOREIGN KEY(idEmployee) REFERENCES employees(idEmployee),
        FOREIGN KEY(idPost) REFERENCES posts(idPost),
        FOREIGN KEY(idDepartments) REFERENCES departments(idDepartment)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients
    (
        idClient INTEGER NOT NULL PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoices
    (
        idInvoice INTEGER NOT NULL PRIMARY KEY,
        idProduct INTEGER NOT NULL,
        idClient INTEGER NOT NULL,
        FOREIGN KEY(idProduct) REFERENCES products(idProduct),
        FOREIGN KEY(idClient) REFERENCES clients(idClient)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS beerTypes
    (
        idBeerType INTEGER NOT NULL PRIMARY KEY,
        Type VARCHAR(50)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products
    (
        idProduct INTEGER NOT NULL PRIMARY KEY,
        Name VARCHAR(50),
        Price INTEGER NOT NULL,
        SalesDate DATE,
        idBeerType INTEGER NOT NULL,
        Stock INTEGER
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weapons
    (
        idWeapon INTEGER NOT NULL PRIMARY KEY,
        Name VARCHAR(50),
        Price INTEGER NOT NULL,
        SalesDate DATE,
        Stock INTEGER
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS easterEgg
    (
        idEasterEgg INTEGER NOT NULL PRIMARY KEY,
        idClient INTEGER NOT NULL,
        idWeapon INTEGER NOT NULL,
        FOREIGN KEY(idWeapon) REFERENCES weapons(idWeapon),
        FOREIGN KEY(idClient) REFERENCES clients(idClient)
    );
''')

nationalities = ["USA", "Canada", "UK", "Australia", "Germany", "France", "Japan", "China", "India", "Brazil", "Mexico", "Spanish", "Swiss", "Belgium", "Netherlands", "Finland", "Italia"]
for i in range(1, 18):
    country = nationalities[i - 1]
    cursor.execute('INSERT INTO nationality (idNationality, Country) VALUES (?, ?);', (i, country))

conn.commit()
conn.close()

print("Data insertion completed.")
