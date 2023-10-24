##
# @author Yamao Cuzou <yamao.cuzou@ynov.com>
 # @file Description
 # @desc Created on 2023-10-17 12:53:19 pm
 # @copyright Cuzou Corporation
 #

import sqlite3
import random
import numpy as np
from csv import reader

conn = sqlite3.connect('database/company.db')
cursor = conn.cursor()

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
    CREATE TABLE IF NOT EXISTS beerTypes
    (
        idBeerType INTEGER NOT NULL PRIMARY KEY,
        Type VARCHAR(50)
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

def insertDepType():
    depType = ["Production", "Marketing", "HumainRessources", "WeaponTraffic"]
    for i in range(0, 4):
        dType = depType[i]
        cursor.execute('INSERT INTO departmentsType (idDepartmentType, Title) VALUES (?, ?);', (i, dType))

def insertDep():
    depName = ["Business&Co", "LikeU", "WeAreUpon", "DrinkAlot", "AssaultCompany"]
    depidtype = [1, 2, 0, 0, 3]
    for i in range(0, 5):
        dName = depName[i]
        dIdType = depidtype[i]
        cursor.execute('INSERT INTO departments (idDepartment, Name, idType) VALUES (?, ?, ?);', (i, dName, dIdType))

def insertPosts():
    postsName = ["Marketing Manager", "HR Manager", "Production Manager", "Delivery Person", "Production Worker", "Developper", "Coach leaderShip", "Coach Hapiness"]
    listDescription = ["He/She has to negociate all the contract and take care about the comany image", "He/She has to take care about the recrutement of new rookies or expert"
    , "He/She has to take care about the proper functioning of the factory and the deliveries", "They have to deliver packages around the world"
    , "They have to create all the items for the company","They have to developpe the website and the application of the company"
    , "They have to train new manager", "They have to keep everyone happy"]
    for i in range(0, 8):
        pName = postsName[i]
        listDesc = listDescription[i]
        cursor.execute('INSERT INTO posts (idPost, Name, Description) VALUES (?, ?, ?);', (i, pName, listDesc))

def switch_post(i):
    if (0 <= i < 15):
        return(i % 3)
    elif (15 <= i <= 75):
        return(4)
    elif (76 <= i <= 150):
        return(5)
    elif (150 < i < 200):
        return(random.randint(5, 8))

def switch_dep(i):
    if (0 <= i < 15):
        return(i % 5)
    elif (15 <= i <= 200):
        return(random.randint(0, 4))

def insertEmpDep():
    listidEmpl = []
    isFind = False
    for i in range(0, 200):
        isFind = False
        idEmpl = random.randint(0, 200)
        idPost = switch_post(i)
        idDep = switch_dep(i)
        while (isFind != True):
            if idEmpl in listidEmpl:
                idEmpl = random.randint(0, 200)
            else:
                isFind = True
                listidEmpl.append(idEmpl)
        cursor.execute('INSERT INTO employeeDepartments (idEmployeeDepartement, idEmployee, idPost, idDepartments) VALUES (?, ?, ?, ?);', (i, idEmpl, idPost, idDep))

def getDataFromFile(filepath, flag, tab, isName):
    with open(filepath, flag) as file:
        file_reader = reader(file)
        for row in file:
            for i in file_reader:
                if (isName == True):
                    tab.append(i[0][:1] + i[0][1:].lower())
                else:
                    tab.append(i[0])
    file.close()
    return (tab)

def get_distinct_data(data, tab, csv_tab, i):
    isFind = False
    data = random.choice(csv_tab[i])
    while not isFind:
        if data in tab:
            data = random.choice(csv_tab[i])
        else:
            isFind = True
            tab.append(data)
    return data, tab

def insertEmployees(FirstName, LastName, PhoneNumbers, BirthDates, HireDates):
    HireTab = []
    BirthTab = []
    PhonesTab = []
    Phone = 0
    HireData = 0
    BirthData = 0
    csv_tab = [PhoneNumbers, BirthDates, HireDates]
    for i in range(0, 200):
        First = random.choice(FirstName)
        Last = random.choice(LastName)
        Salary = random.randint(1600, 3500)
        Phone, PhonesTab = get_distinct_data(Phone, PhonesTab, csv_tab, 0)
        HireData, HireTab = get_distinct_data(HireData, HireTab, csv_tab, 1)
        BirthData, BirthTab = get_distinct_data(BirthData, BirthTab, csv_tab, 2)
        cursor.execute('INSERT INTO employees (idEmployee, FirstName, LastName, PhoneNumber, Salary, HireDate, BirthDate) VALUES (?, ?, ?, ?, ?, ?, ?);', (i, First, Last, Phone, Salary, HireData, BirthData))

def insertClients(FirstName, LastName):
    for i in range(0, 3500):
        FirstNC = FirstName[random.randint(0, 209309)]
        LastNC = LastName[random.randint(0, 879421)]
        cursor.execute('INSERT INTO clients (idClient, FirstName, LastName) VALUES (?, ?, ?);', (i, FirstNC, LastNC))

def insertBeerType():
    beerType = ["The beers to keep", "Lager beers", "Triple beers", "Abbey beers", "Barrel-aged beers", "India Pale Ale beers", "White beers"]
    for i in range(0, 7):
        cursor.execute('INSERT INTO beerTypes (idBeerType, Type) VALUES (?, ?);', (i, beerType[i]))

def insertProducts(Products):
    for i in range(len(Products)):
        Price = random.randint(25, 90)
        cursor.execute('INSERT INTO products (idProduct, Name, Price, salesDate, idBeerType, Stock) VALUES (?, ?, ?, ?, ?, ?);', (i, Products[i], Price))

def main():
    FirstName, LastName, PhoneNumber, HireDate, BirthDate, Products = [], [], [], [], [], []
    insertDepType()
    insertDep()
    insertPosts()
    insertEmpDep()
    FirstName = getDataFromFile("csv/prenom.csv", "r", FirstName, True)
    LastName = getDataFromFile("csv/patronymes.csv", "r", LastName, True)
    PhoneNumber = getDataFromFile("csv/phonesFr.csv", "r", PhoneNumber, False)
    BirthDate = getDataFromFile("csv/birthDates.csv", "r", BirthDate, False)
    HireDate = getDataFromFile("csv/hireDates.csv", "r", HireDate, False)
    Products = getDataFromFile("csv/products.csv", "r", Products, False)
    insertEmployees(FirstName, LastName, PhoneNumber, BirthDate, HireDate)
    insertClients(FirstName, LastName)
    insertBeerType()
    # insertProducts()

main()
# for i in range(0, 10000):
#     cursor.execute('INSERT INTO invoices (idInvoice, idProduct, idClient) VALUES (?, ?, ?);', (i, FirstNC, LastNC))
conn.commit()
conn.close()

print("Data insertion completed.")
