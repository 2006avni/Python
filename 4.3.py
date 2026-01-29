a = int(input("Enter 1 number"))
b = int(input("Enter 2 number"))
c = int(input("Enter 3 numbers"))
if (a > b):
    if (a > c):
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if (b > c):
        print("b is greatest")
    else:
        print("c is greatest")
