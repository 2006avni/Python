class degree: 
    def getdegree(self): 
        print("I got a degree") 
 
class undergraduate(degree): 
    def getdegree(self):
        print("I am undergraduate") 
class postgraduate(degree):
    def getdegree(self):
        print("I am postgraduate") 
a=degree() 
b=undergraduate() 
c=postgraduate() 
a.getdegree() 
b.getdegree() 
c.getdegree()
