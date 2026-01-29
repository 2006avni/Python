class Employee: 
    def get(self): 
        self.name = input("Enter name: ") 
        self.dept = input("Enter department: ") 
        self.salary = int(input("Enter salary: ")) 

    def put(self): 
        print("NAME =", self.name) 
        print("DEPT =", self.dept) 
        print("SALARY =", self.salary) 

ob = Employee() 
ob.get() 
ob.put()
