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

func convertPostToId(post string) int {
	if post == "Marketing Manager" {
		return 0
	} else if post == "HR Manager" {
		return 1
	} else if post == "Production Manager" {
		return 2
	} else if post == "Delivery Person" {
		return 3
	} else if post == "Production Worker" {
		return 4
	} else if post == "Developper" {
		return 5
	} else if post == "Coach Leadership" {
		return 6
	}
	return 7
}

func convertDeptToId(dept string) int {
	if dept == "Business&Co" {
		return 0
	} else if dept == "LikeU" {
		return 1
	} else if dept == "WeAreUpon" {
		return 2
	} else if dept == "DrinkAlot" {
		return 3
	}
	return 4
}
