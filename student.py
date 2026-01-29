class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.department = ""
        self.mobile_no = ""

    def read_info(self):
        self.name = input("Enter student's name: ")
        self.roll_no = input("Enter roll number: ")
        self.department = input("Enter department: ")
        self.mobile_no = input("Enter mobile number: ")

    def display_info(self):
        print("\nStudent Information:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Department:", self.department)
        print("Mobile No:", self.mobile_no)


stud = Student()
stud.read_info()
stud.display_info()
