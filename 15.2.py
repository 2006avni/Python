class Student: 
    def get(self): 
        self.name = input("Enter name: ") 
        self.dept = input("Enter department: ") 

class Display(Student): 
    def put(self): 
        print("NAME =", self.name) 
        print("DEPT =", self.dept) 

ob = Display() 
ob.get() 
ob.put()
