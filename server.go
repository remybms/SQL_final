package SQL

import (
	"database/sql"
	"fmt"
	"net/http"
	"text/template"

	_ "github.com/mattn/go-sqlite3"
)

func Server() {
	http.HandleFunc("/", displayEmployees)
	http.HandleFunc("/createremployee", createEmployee)
	fileServer := http.FileServer(http.Dir("templates/assets/"))
	http.Handle("/assets/", http.StripPrefix("/assets", fileServer))
	fmt.Println("http://localhost:8000/  Server is running in port 8000")
	http.ListenAndServe(":8000", nil)
}

func createEmployee(w http.ResponseWriter, r *http.Request) {
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

func displayEmployees(w http.ResponseWriter, r *http.Request) {
	tmpl, error := template.ParseGlob("templates/*.html")
	if error != nil {
		panic(error)
	}
	employees := getEmployeesFromDB()

	tmpl.ExecuteTemplate(w, "main", employees)
}
