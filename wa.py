with open('anvy.txt', 'w') as file:
    file.write("This is the initial content.\n")

with open('anvy.txt', 'a') as file:
    file.write("This is the appended content.\n")

print("File has been written and appended successfully.")
