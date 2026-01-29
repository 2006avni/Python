
class InvalidPassword(Exception):
    pass


def check(password):
    if len(password) < 6:
        raise InvalidPassword("Password too short!")
    return "Password is valid!"

user_password = input("Enter your password: ")
try:
    print(check(user_password)) 
except InvalidPassword as e:
    print(e) 
