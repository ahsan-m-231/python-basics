from schoolManagement_package.SchoolManagement import SchoolManagement
SchoolManagement.school_name = "Global school"
SchoolManagement.school_address = "Chennai"

Student_1 = SchoolManagement(1001,"jack","jack@gmail.com",45.2)
Student_2 = SchoolManagement(1002,"peter","peter@gmail.com",85.2)
Student_3 = SchoolManagement(1003,"mark","mark@gmail.com",56.5)

SchoolManagement.print_student_details(Student_1)