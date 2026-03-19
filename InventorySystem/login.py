import sqlite3
from getpass import getpass
from colorama import Fore


def login():

    print("\n===== LOGIN =====")

    username = input("Username: ")
    password = getpass("Password: ")

    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT id, username, password, role FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    conn.close()

    if user:
        print(Fore.GREEN + f"\nLogin Successful! Welcome {user[1]} ({user[3]})")
        return user
    else:
        print(Fore.RED + "Invalid Login")
        return None
