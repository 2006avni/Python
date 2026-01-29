sum1 = 0
num = int(input("Enter number"))
while (num != 0):
    rem = num % 10
    sum1 = sum1 + rem
    num = num // 10
print("Sum of number =",sum1)
