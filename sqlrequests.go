package SQL

import (
	"database/sql"
	"net/http"

	_ "github.com/mattn/go-sqlite3"
)

var erreur string

func createEmployeeForm(w http.ResponseWriter, r *http.Request) {
	if r.Method == "POST" {
		firstName := r.FormValue("firstName")
		lastName := r.FormValue("lastName")
		phoneNumber := r.FormValue("phoneNumber")
		salary := r.FormValue("salary")
		hireDate := r.FormValue("hireDate")
		birthDate := r.FormValue("birthDate")

		db, err := sql.Open("sqlite3", "database/company.db")
		if err != nil {
			panic(err)
		}
		defer db.Close()

		stmt, err := db.Prepare("INSERT INTO employees (FirstName, LastName, PhoneNumber, Salary, HireDate, BirthDate) VALUES (?, ?, ?, ?, ?, ?)")
		if err != nil {
			panic(err)
		}
		defer stmt.Close()

		_, err = stmt.Exec(firstName, lastName, phoneNumber, salary, hireDate, birthDate)
		if err != nil {
			panic(err)
		}
		defer db.Close()
		displayEmployees(w, r)
	}
}
