def test(s): 
    up = 0 
    lo = 0 
    for i in s: 
        if i.islower(): 
            lo += 1 
        elif i.isupper(): 
            up += 1 
    print("Lower case =", lo) 
    print("Upper case =", up) 

s = input("Enter string: ") 
test(s)
