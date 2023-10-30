package SQL

import (
	"database/sql"
	"fmt"
	"net/http"

	_ "github.com/mattn/go-sqlite3"
)

func createEmployeeForm(w http.ResponseWriter, r *http.Request) {
	if r.Method == "POST" {
		firstName := r.FormValue("firstName")
		lastName := r.FormValue("lastName")
		phoneNumber := r.FormValue("phoneNumber")
		salary := r.FormValue("salary")
		hireDate := r.FormValue("hireDate")
		birthDate := r.FormValue("birthDate")
		post := r.FormValue("post")
		department := r.FormValue("department")
		fmt.Println(post)

		idPost := convertPostToId(post)
		idDepartment := convertDeptToId(department)

		db, err := sql.Open("sqlite3", "database/company.db")
		if err != nil {
			panic(err)
		}
		defer db.Close()

		stmt, err := db.Prepare("INSERT INTO employees (FirstName, LastName, PhoneNumber, Salary, HireDate, BirthDate, idPost, idDepartment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
		if err != nil {
			panic(err)
		}
		defer stmt.Close()

		_, err = stmt.Exec(firstName, lastName, phoneNumber, salary, hireDate, birthDate, idPost, idDepartment)
		if err != nil {
			panic(err)
		}
		defer db.Close()
		displayEmployees(w, r)
	}
}
