from database import get_connection
from colorama import Fore

def add_customer():

    conn = get_connection()
    cur = conn.cursor()

    name = input("Customer Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    cur.execute(
        "INSERT INTO customers(name,phone,email) VALUES(?,?,?)",
        (name,phone,email)
    )

    conn.commit()
    conn.close()

    print(Fore.GREEN + "Customer Added")


def view_customers():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()

    for r in rows:
        print(r)

    conn.close()
