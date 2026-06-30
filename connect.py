import pymysql

# Database Connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="dha_crud"
)

cursor = conn.cursor()

# Add Employee
def add_employee():
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    sql = "INSERT INTO employees(emp_name, department, salary) VALUES(%s,%s,%s)"
    cursor.execute(sql, (name, dept, salary))
    conn.commit()

    print("Employee Added Successfully")


# View Employees
def view_employee():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\nID\tName\tDepartment\tSalary")
    print("-" * 50)

    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")


# Update Employee
def update_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter New Name: ")
    dept = input("Enter New Department: ")
    salary = float(input("Enter New Salary: "))

    sql = """
    UPDATE employees
    SET emp_name=%s, department=%s, salary=%s
    WHERE emp_id=%s
    """

    cursor.execute(sql, (name, dept, salary, emp_id))
    conn.commit()

    print("Employee Updated Successfully")


# Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    sql = "DELETE FROM employees WHERE emp_id=%s"

    cursor.execute(sql, (emp_id,))
    conn.commit()

    print("Employee Deleted Successfully")


# Menu
while True:
    print("\n===== OFFICE EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employee()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

cursor.close()
conn.close()