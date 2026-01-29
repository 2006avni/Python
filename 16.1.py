a = 10
b = 0

try:
    d = a / b
    print(d)
except ZeroDivisionError as obj:
    print(obj)
except NameError as obj1:
    print(obj1)

