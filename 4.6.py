php = int(input("Enter the marks for PHP: "))
py = int(input("Enter the marks for Python: "))
mad = int(input("Enter the marks for MAD: "))
java = int(input("Enter the marks for Java: "))
EDI = int(input("Enter the marks for EDI: "))

avg = (php + py + mad + java + EDI) / 5

if avg >= 75:
    print("Distinction")
elif avg >= 60:
    print("First class")
elif avg >= 45:
    print("Second class")
else:
    print("Fail")
