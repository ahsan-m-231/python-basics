class SchoolManagement:
    school_name = None
    school_address = None

    def __init__(self, student_rollno, student_name, student_mailid, student_percentage):
        self.student_rollno = student_rollno
        self.student_name = student_name
        self.student_mailid = student_mailid
        self.student_percentage = student_percentage

    def print_student_details(self):
        print("Student Roll No", self.student_rollno)
        print("Student Name", self.student_name)
        print("Student Mail", self.student_mailid)
        print("Student Percentage", self.student_percentage)
        print("School Name", SchoolManagement.school_name)
        print("School Address", SchoolManagement.school_address)
