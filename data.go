package SQL

import (
	"database/sql"

	_ "github.com/mattn/go-sqlite3"
)

type Employee struct {
	Id         int
	FirstName  string
	LastName   string
	Post       string
	Department string
}

type EmployeesArray struct {
	Employees []Employee
}

type Post struct {
	PostName string
}

type Department struct {
	DepartmentName string
}

type PostAndDepartment struct {
	Posts       []Post
	Departments []Department
}

func getPostFromDB() PostAndDepartment {
	db, err := sql.Open("sqlite3", "database/company.db")
	if err != nil {
		panic(err)
	}
	posts, err := db.Query("SELECT Name FROM posts")
	if err != nil {
		panic(err)
	}
	defer posts.Close()

	dept, err := db.Query("SELECT Name FROM departments")
	if err != nil {
		panic(err)
	}
	defer dept.Close()

	var postsAndDepartments PostAndDepartment
	for posts.Next() {
		var post Post
		err := posts.Scan(&post.PostName)
		if err != nil {
			panic(err)
		}
		postsAndDepartments.Posts = append(postsAndDepartments.Posts, post)
	}

	if err = posts.Err(); err != nil {
		panic(err)
	}

	for dept.Next() {
		var department Department
		err := dept.Scan(&department.DepartmentName)
		if err != nil {
			panic(err)
		}
		postsAndDepartments.Departments = append(postsAndDepartments.Departments, department)
	}

	if err = dept.Err(); err != nil {
		panic(err)
	}

	return postsAndDepartments
}

func getEmployeesFromDB() EmployeesArray {
	db, err := sql.Open("sqlite3", "database/company.db")
	if err != nil {
		panic(err)
	}
	rows, err := db.Query("SELECT employees.idEmployee, employees.FirstName, employees.LastName, posts.Name, departments.Name FROM employees INNER JOIN posts ON employees.idPost = posts.idPost INNER JOIN departments ON employees.idDepartment = departments.idDepartment")
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	var employees EmployeesArray
	for rows.Next() {
		var employee Employee
		err := rows.Scan(&employee.Id, &employee.FirstName, &employee.LastName, &employee.Post, &employee.Department)
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
	if post == "MarketingManager" {
		return 0
	} else if post == "HRManager" {
		return 1
	} else if post == "ProductionManager" {
		return 2
	} else if post == "DeliveryPerson" {
		return 3
	} else if post == "ProductionWorker" {
		return 4
	} else if post == "Developper" {
		return 5
	} else if post == "CoachLeadership" {
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
