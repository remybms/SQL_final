package SQL

import (
	"database/sql"

	_ "github.com/mattn/go-sqlite3"
)

type Employee struct {
	Id        int
	FirstName string
	LastName  string
}

type EmployeesArray struct {
	Employees []Employee
}

func getEmployeesFromDB() EmployeesArray {
	db, err := sql.Open("sqlite3", "database/company.db")
	if err != nil {
		panic(err)
	}
	rows, err := db.Query("SELECT idEmployee, FirstName, LastName FROM employees")
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	var employees EmployeesArray
	for rows.Next() {
		var employee Employee
		err := rows.Scan(&employee.Id, &employee.FirstName, &employee.LastName)
		if err != nil {
			panic(err)
		}
		employees.Employees = append(employees.Employees, employee)
	}

	if err = rows.Err(); err != nil {
		panic(err)
	}

	return employees
}
