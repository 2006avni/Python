def palindrome(s):
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]

str = input("Enter a string: ")
if palindrome(str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
