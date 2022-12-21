class Employee():
    company_name = "TTL"
    company_location = "Pune"

    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def print_employee_detail(self):
        print("Employee ID ", self.emp_id)
        print("Employee Name ", self.emp_name)
        print("Employee Salary ", self.emp_salary)
        print("Company Name ", Employee.company_name)
        print("Company Location ", Employee.company_location)

    @staticmethod
    def print_author_name():
        print("Mohd Ahsan")

    def get_employee_name(self):
        return str(self.emp_name).upper()

    @property
    def getcapitalize_emp_name(self):
        return str(self.emp_name).capitalize()
