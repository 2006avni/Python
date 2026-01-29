class test: 
    def testci(self,c,i): 
        self.c=c 
        self.i=i 
        print("character==",self.c) 
        print("Integer==",self.i) 
 
    def testci(self,i,c): 
        self.c=c 
        self.i=i 
        print("character==",self.c) 
        print("Integer==",self.i) 
a=test() 
a.testci('a',12)
