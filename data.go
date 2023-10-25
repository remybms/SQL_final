package SQL

import (
	"database/sql"

	_ "github.com/mattn/go-sqlite3"
)

type Employee struct {
	id        int
	firstName string
	lastName  string
}

func getEmployeesFromDB() ([]Employee, error) {
	db, err := sql.Open("sqlite3", "database/company.db")
	if err != nil {
		return nil, err
	}
	rows, err := db.Query("SELECT idEmployee, FirstName, LastName FROM employees")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var employees []Employee
	for rows.Next() {
		var employee Employee
		err := rows.Scan(&employee.id, &employee.firstName, &employee.lastName)
		if err != nil {
			return nil, err
		}
		employees = append(employees, employee)
	}

	if err = rows.Err(); err != nil {
		return nil, err
	}

	return employees, nil
}
