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
    FOREIGN KEY(idDepartement) REFERENCES department(idDepartment)
);