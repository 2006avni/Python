filename = "anvy.txt"
with open(filename, 'r') as file:
    lines = len(file.readlines())
    print(f"The file {filename} has {lines} lines.")
