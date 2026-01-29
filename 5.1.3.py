n = 7
for i in range(n, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces, end="")  
    for j in range(i):
        print(j % 2, end=" ")  
    print()  
