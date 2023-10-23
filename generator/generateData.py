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

conn = sqlite3.connect('database/company.db')
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

depType = ["Production", "Marketing", "HumainRessources", "WeaponTraffic"]
for i in range(1, 3):
    dType = depType[i - 1]
    cursor.execute('INSERT INTO departmentsType (idDepartmentType, Title) VALUES (?, ?);', (i, dType))

depName = ["Business&Co", "LikeU", "WeAreUpon", "DrinkAlot", "AssaultCompany"]
depidtype = [1, 2, 0, 0, 3]
for i in range(1, 5):
    dName = depName[i - 1]
    dIdType = depidtype[i - 1]
    cursor.execute('INSERT INTO departments (idDepartment, Name, idType) VALUES (?, ?, ?);', (i, dName, dIdType))

postsName = ["Developper", "Marketing Manager", "HR Manager", "Production Manager", "Company Chief", "Delivery Person", "Production Worker", "Coach leaderShip", "Coach Hapiness"]
listDescription = ["They have to developpe the website and the application of the company", "He/She has to negociate all the contract and take care about the comany image"
                   , "He/She has to take care about the recrutement of new rookies or expert", "He/She has to take care about the proper functioning of the factory and the deliveries"
                   , "He/She has to lead the company and take all the decisions", "They have to deliver packages around the world", "They have to create all the items for the company"
                   , "They have to train new manager", "They have to keep everyone happy"]
for i in range(1, 9):
    pName = postsName[i - 1]
    listDesc = listDescription[i - 1]
    cursor.execute('INSERT INTO posts (idPost, Name, Description) VALUES (?, ?, ?);', (i, pName, listDesc))

conn.commit()
conn.close()

print("Data insertion completed.")
