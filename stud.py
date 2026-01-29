class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def __str__(self):
        return f"{self.name}({self.rollno})"

s1 = Student("anvy", 26)
print(s1)
