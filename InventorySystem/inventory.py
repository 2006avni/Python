from database import get_connection
from colorama import Fore

def add_item():

    conn = get_connection()
    cur = conn.cursor()

    name = input("Item Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    try:
        cur.execute(
            "INSERT INTO inventory(name,price,quantity) VALUES(?,?,?)",
            (name,price,qty)
        )
        conn.commit()
        print(Fore.GREEN + "Item Added Successfully")

    except:
        print(Fore.RED + "Item already exists")

    conn.close()


def view_items():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()

    print("\nID  Name   Price   Quantity")

    for r in rows:
        print(r)

    conn.close()


def restock_item():

    conn = get_connection()
    cur = conn.cursor()

    item_id = input("Item ID: ")

    try:
        qty = int(input("Quantity to Add: "))
    except:
        print(Fore.RED + "Enter number only")
        return

    cur.execute(
        "UPDATE inventory SET quantity = quantity + ? WHERE id=?",
        (qty,item_id)
    )

    conn.commit()

    print(Fore.GREEN + "Stock Updated")

    conn.close()


def low_stock():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM inventory WHERE quantity < 5")

    rows = cur.fetchall()

    print("\nLow Stock Items")

    for r in rows:
        print(r)

    conn.close()
