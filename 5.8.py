rev = 0
num = int(input("Enter number"))
copy = num
while (num != 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if (copy == rev):
    print("Number is palindrome")
else:
    print("Not palindrome")
