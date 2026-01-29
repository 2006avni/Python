matrix1 = [[10, 11, 12], 
           [13, 14, 15], 
           [16, 17, 18]] 

matrix2 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]] 

rmatrix = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]] 

print("Addition") 
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] + matrix2[i][j]
for r in rmatrix: 
    print(r) 

print("Subtraction") 
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] - matrix2[i][j] 
for r in rmatrix: 
    print(r) 

print("Multiplication") 
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] * matrix2[i][j] 
for r in rmatrix:
    print(r) 

print("Division") 
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] / matrix2[i][j] 
for r in rmatrix: 
    print(r)
