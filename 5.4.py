term = 5
t1 = 0
t2 = 1

print(t1)
print(t2)

i = 0
while i <= term - 3:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    i = i + 1
