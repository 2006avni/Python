with open("anvy.txt", "r") as file:
    contents = file.read()

with open("a1.txt", "w") as file:
    file.write(contents)
print("successfully read and write the content")
