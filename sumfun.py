def sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
num = int(input("Enter a number: "))
print("Sum of digits:", sum(num))
