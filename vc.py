v = ("aeiouAEIOU")
f = open("anvy.txt",'r')
vc = 0
for i in f.read():
    if i in v:
        vc = vc+1
print(vc)
f.close()
