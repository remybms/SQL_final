package SQL

import (
	"fmt"
	"net/http"
	"text/template"

	_ "github.com/mattn/go-sqlite3"
)

func Server() {
	http.HandleFunc("/", displayEmployees)
	http.HandleFunc("/createEmployee", createEmployee)
	http.HandleFunc("/createemployee-form", createEmployeeForm)
	http.HandleFunc("/employeesSorted", displayEmployeesSorted)
	fileServer := http.FileServer(http.Dir("templates/assets/"))
	http.Handle("/assets/", http.StripPrefix("/assets", fileServer))
	fmt.Println("http://localhost:8000/  Server is running in port 8000")
	http.ListenAndServe(":8000", nil)
}

func createEmployee(w http.ResponseWriter, r *http.Request) {
	tmpl, error := template.ParseGlob("templates/*.html")
	if error != nil {
		panic(error)
	}
	postsAndDepartments := getPostFromDB()
	tmpl.ExecuteTemplate(w, "create", postsAndDepartments)
}

func displayEmployees(w http.ResponseWriter, r *http.Request) {
	tmpl, error := template.ParseGlob("templates/*.html")
	if error != nil {
		panic(error)
	}
	employees := getEmployeesFromDB()

	tmpl.ExecuteTemplate(w, "main", employees)
}

func displayEmployeesSorted(w http.ResponseWriter, r *http.Request) {
	sort := r.FormValue("sort")
	tmpl, error := template.ParseGlob("templates/*.html")
	if error != nil {
		panic(error)
	}
	employees := getEmployeesSortedFromDB(sort)
	tmpl.ExecuteTemplate(w, "sorted", employees)

}
