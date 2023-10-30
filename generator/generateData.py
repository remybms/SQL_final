##
# @author Yamao Cuzou <yamao.cuzou@ynov.com>
 # @file Description
 # @desc Created on 2023-10-17 12:53:19 pm
 # @copyright Cuzou Corporation
 #

import sqlite3
import random
import numpy as np
import csv
from csv import reader

conn = sqlite3.connect('database/company.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts
    (
        idPost INTEGER NOT NULL PRIMARY KEY,
        Name VARCHAR(50),
        Description VARCHAR(150)
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
    CREATE TABLE IF NOT EXISTS employees
    (
        idEmployee INTEGER NOT NULL PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        PhoneNumber VARCHAR(50),
        Salary INTEGER NOT NULL,
        HireDate DATE,
        BirthDate DATE,
        idPost INTEGER NOT NULL,
        idDepartment INTEGER NOT NULL,
        FOREIGN KEY(idPost) REFERENCES posts(idPost),
        FOREIGN KEY(idDepartment) REFERENCES departments(idDepartment)
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
        ReferenceRGA VARCHAR(50),
        WeaponType VARCHAR(50),
        FabCountry VARCHAR(50),
        Family VARCHAR(50),
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
    postsName = ["MarketingManager", "HRManager", "ProductionManager", "DeliveryPerson", "ProductionWorker", "Developper", "CoachLeadership", "CoachHapiness"]
    listDescription = ["He/She has to negociate all the contract and take care about the comany image", "He/She has to take care about the recrutement of new rookies or expert"
    , "He/She has to take care about the proper functioning of the factory and the deliveries", "They have to deliver packages around the world"
    , "They have to create all the items for the company","They have to developpe the website and the application of the company"
    , "They have to train new manager", "They have to keep everyone happy"]
    for i in range(0, 8):
        pName = postsName[i]
        listDesc = listDescription[i]
        cursor.execute('INSERT INTO posts (idPost, Name, Description) VALUES (?, ?, ?);', (i, pName, listDesc))

def switchPost(i):
    if (0 <= i < 15):
        return(i % 3)
    elif (15 <= i <= 75):
        return(4)
    elif (76 <= i <= 150):
        return(5)
    elif (150 < i < 200):
        return(random.randint(5, 8))

def switchDep(i):
    if (0 <= i < 15):
        return(i % 5)
    elif (15 <= i <= 200):
        return(random.randint(0, 4))

def getDataFromFile(filepath, flag, tab, isName, col):
    with open(filepath, flag) as file:
        file_reader = reader(file)
        for row in file:
            for data in file_reader:
                if (isName == True):
                    tab.append(data[col][:1] + data[col][1:].lower())
                else:
                    tab.append(data[col])
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
    listidEmpl = []
    isFind = False
    for i in range(0, 200):
        First = random.choice(FirstName)
        Last = random.choice(LastName)
        Salary = random.randint(1600, 3500)
        Phone, PhonesTab = get_distinct_data(Phone, PhonesTab, csv_tab, 0)
        HireData, HireTab = get_distinct_data(HireData, HireTab, csv_tab, 1)
        BirthData, BirthTab = get_distinct_data(BirthData, BirthTab, csv_tab, 2)
        isFind = False
        idEmpl = random.randint(0, 200)
        idPost = switchPost(i)
        idDep = switchDep(i)
        while (isFind != True):
            if idEmpl in listidEmpl:
                idEmpl = random.randint(0, 200)
            else:
                isFind = True
                listidEmpl.append(idEmpl)
        cursor.execute('INSERT INTO employees (idEmployee, FirstName, LastName, PhoneNumber, Salary, HireDate, BirthDate, idPost, idDepartment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);', (i, First, Last, Phone, Salary, HireData, BirthData, idPost, idDep))

def insertClients(FirstName, LastName):
    for i in range(0, 3500):
        FirstNC = FirstName[random.randint(0, 209309)]
        LastNC = LastName[random.randint(0, 879421)]
        cursor.execute('INSERT INTO clients (idClient, FirstName, LastName) VALUES (?, ?, ?);', (i, FirstNC, LastNC))

def insertBeerType():
    beerType = ["Blonde", "Special Blonde", "Dark/Black", "Amber", "White", "Fruit"]
    for i in range(0, 6):
        cursor.execute('INSERT INTO beerTypes (idBeerType, Type) VALUES (?, ?);', (i, beerType[i]))

def insertProducts(Products, SalesDate, TypeBeer):
    SalesTab = []
    Sales = 0
    csv_tab = [SalesDate]
    for i in range(0, 250):
        Prod = Products[i % 40]
        Type = TypeBeer[i % 40]
        Price = random.randint(25, 90)
        Sales, SalesTab = get_distinct_data(Sales, SalesTab, csv_tab, 0)
        Stock = random.randint(1000, 25000)
        cursor.execute('INSERT INTO products (idProduct, Name, Price, salesDate, idBeerType, Stock) VALUES (?, ?, ?, ?, ?, ?);', (i, Prod, Price, Sales, Type, Stock))

def insertWeapons(Weapons, SalesDate):
    SalesTab = []
    Sales = 0
    csv_tab = [SalesDate]
    for i in range(0, 200):
        Ref = Weapons[0][i % 56107]
        Type = Weapons[2][i % 56107]
        Family = Weapons[1][i % 56107]
        FabCo = Weapons[6][i % 56107]
        Price = random.randint(25000, 90000)
        Sales, SalesTab = get_distinct_data(Sales, SalesTab, csv_tab, 0)
        Stock = random.randint(10000, 250000)
        cursor.execute('INSERT INTO weapons (idWeapon, ReferenceRGA, WeaponType, Family, FabCountry, Price, SalesDate, Stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', (i, Ref, Type, Family, FabCo, Price, Sales, Stock))

def getWeaponsFromFile(filepath, tab, i):
    with open(filepath, newline='', encoding='ISO-8859-1') as file:
        file_reader = csv.reader(file, delimiter=';')
        for row in file:
            for data in file_reader:
                tab.append(data[i])
    return (tab)

def insertInvoices():
    for i in range(0, 200):
        idProd = random.randint(0, 249)
        idCli = random.randint(0, 3500)
        cursor.execute('INSERT INTO invoices (idInvoice, idProduct, idClient) VALUES (?, ?, ?);', (i, idProd, idCli))

def insertEasterEgg():
    for i in range(0, 200):
        idWeapon = random.randint(0, 200)
        idCli = random.randint(0, 3500)
        cursor.execute('INSERT INTO easterEgg (idEasterEgg, idClient, idWeapon) VALUES (?, ?, ?);', (i, idCli, idWeapon))

def main():
    FirstName, LastName, PhoneNumber, HireDate, BirthDate = [], [], [], [], []
    Products, SalesDate, TypeBeer = [], [], []
    ref, family, WeaponType, brand, model, fab, coFab = [], [], [], [], [], [], []
    Weapons = [ref, family, WeaponType, brand, model, fab, coFab]
    insertDepType()
    insertDep()
    insertPosts()
    FirstName = getDataFromFile("csv/prenom.csv", "r", FirstName, True, 0)
    LastName = getDataFromFile("csv/patronymes.csv", "r", LastName, True, 0)
    PhoneNumber = getDataFromFile("csv/phonesFr.csv", "r", PhoneNumber, False, 0)
    BirthDate = getDataFromFile("csv/birthDates.csv", "r", BirthDate, False, 0)
    HireDate = getDataFromFile("csv/hireDates.csv", "r", HireDate, False, 0)
    Products = getDataFromFile("csv/products.csv", "r", Products, False, 0)
    SalesDate = getDataFromFile("csv/salesDates.csv", "r", SalesDate, False, 0)
    TypeBeer = getDataFromFile("csv/productType.csv", "r", TypeBeer, False, 0)
    for i in range(0, 7):
        Weapons[i].append([getWeaponsFromFile("csv/weapons.csv", Weapons[i], i)])
    insertEmployees(FirstName, LastName, PhoneNumber, BirthDate, HireDate)
    insertClients(FirstName, LastName)
    insertBeerType()
    insertProducts(Products, SalesDate, TypeBeer)
    insertWeapons(Weapons, SalesDate)
    insertInvoices()
    insertEasterEgg()

main()
conn.commit()
conn.close()

print("Data insertion completed.")
