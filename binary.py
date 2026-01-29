binary=list(input("enter a binary no"))
value=0
for i in range(len(binary)):
    digit=binary.pop()
    if digit=="1":
        value=value+pow(2,i)
print("The decimal value of the num is=",value)        
