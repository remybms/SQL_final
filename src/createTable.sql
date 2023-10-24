
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

CREATE TABLE IF NOT EXISTS departmentsType
(
    idDepartmentType INTEGER NOT NULL PRIMARY KEY,
    Title VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS departments
(
    idDepartment INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(50),
    idType INTEGER NOT NULL,
    FOREIGN KEY(idType) REFERENCES departmentsType(idDepartmentType)
);

CREATE TABLE IF NOT EXISTS posts
(
    idPost INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(50),
    Description VARCHAR(150)
);

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

CREATE TABLE IF NOT EXISTS clients
(
    idClient INTEGER NOT NULL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS beerTypes
(
    idBeerType INTEGER NOT NULL PRIMARY KEY,
    Type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS products
(
    idProduct INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(50),
    Price INTEGER NOT NULL,
    SalesDate DATE,
    idBeerType INTEGER NOT NULL,
    Stock INTEGER
);

CREATE TABLE IF NOT EXISTS invoices
(
    idInvoice INTEGER NOT NULL PRIMARY KEY,
    idProduct INTEGER NOT NULL,
    idClient INTEGER NOT NULL,
    FOREIGN KEY(idProduct) REFERENCES products(idProduct),
    FOREIGN KEY(idClient) REFERENCES clients(idClient)
);

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

CREATE TABLE IF NOT EXISTS easterEgg
(
    idEasterEgg INTEGER NOT NULL PRIMARY KEY,
    idClient INTEGER NOT NULL,
    idWeapon INTEGER NOT NULL,
    FOREIGN KEY(idWeapon) REFERENCES weapons(idWeapon),
    FOREIGN KEY(idClient) REFERENCES clients(idClient)
);

INSERT INTO IF NOT EXISTS