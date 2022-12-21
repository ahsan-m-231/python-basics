from employee_package.employee_module import Employee
Employee.company_location = "Pune"
Employee.company_name = "TTL"
Employee.print_author_name()
emp_1 = Employee(101, "Saul bing FUN", 50000)
emp_2 = Employee(102, "TIM", 60000)
emp_3 = Employee(103, "Kiara", 70000)
print(emp_1.emp_id, emp_1.emp_name, emp_1.emp_salary, Employee.company_location, Employee.company_name)
print(emp_2.emp_id, emp_2.emp_name, emp_2.emp_salary, Employee.company_location, Employee.company_name)
print(emp_3.emp_id, emp_3.emp_name, emp_3.emp_salary, Employee.company_location, Employee.company_name)
print("-------------------")
emp_1.print_employee_detail()
print("--------")
emp_2.print_employee_detail()
print("--------")
emp_3.print_employee_detail()
print("get Name - ", emp_1.getcapitalize_emp_name)
