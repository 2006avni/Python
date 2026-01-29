file = open("anvy.txt", "r")
data = file.read()
for char in set(data):
    print(char, ":", data.count(char))
file.close()
