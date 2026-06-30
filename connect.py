import pymysql
#database connection
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="dha_crud"
)
cursor=conn.cursor()

#Employee data Added
def Add_employ():
    name=input("Enter Employee Name")
    dept=input("Enter Department")
    salary=float(input("Enter Salary"))

    sql="insert into employees(emp_name,department,salary) values(%s,%s,%s)"
   
    cursor.execute(sql,(name,dept,salary))
    conn.commit()
    print("Employee data Added Successfully")

#List EMployees
def view_employ():
    cursor.execute("select * from employees")
    rows=cursor.fetchall()
    print("\nID\tName\tDepartment\tsalary")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")



#update Employ
def update_employ():
    emp_id=int(input("Enter Employee ID"))

    name=input("Enter Employee Name")
    dept=input("Enter Department")
    salary=float(input("Enter Salary"))

    sql="""
    update employees
    set emp_name=%s,department=%s,salary=%s
    where emp_id=%d"""

    cursor.execute(sql,(name,dept,salary,emp_id))
    conn.commit()
    print("Emplyee Update Successfully")
def Delete_employ():
    emp_id=int(input("Enter Emplyee ID"))
    sql="delete from employees where emp_id=%s"
    cursor.execute(sql,(emp_id))
    conn.commit()
    print("DELETED SUCCESSFULLY")


#Menu
while True:
    print("\n------------EMPLOYEE SYSTEM------------")
    print("1.Add Employ")
    print("2.View Employ")
    print("3.Update Employ")
    print("4.Delete Employ")
    print("5.Exit")

    option=input("Enter The Option of below list")
    if option == "1":
        Add_employ()
    elif option == "2":
        view_employ()
    elif option == "3":
        update_employ()
    elif option == "4":
        Delete_employ()
    elif option == "5":
        print("Thank you tata bYE BYEE")
        break;
    else:
        print("INVALID OPTION")
cursor.close()        
conn.close()
                


