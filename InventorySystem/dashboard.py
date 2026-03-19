import sqlite3
from colorama import Fore


def show_dashboard():

    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()

    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.GREEN + "             📊 LIVE DASHBOARD")
    print(Fore.CYAN + "="*50)

    # ---------------- TOTAL PRODUCTS ----------------
    cur.execute("SELECT COUNT(*) FROM inventory")
    total_products = cur.fetchone()[0]

    # ---------------- TOTAL STOCK ----------------
    cur.execute("SELECT SUM(quantity) FROM inventory")
    stock = cur.fetchone()[0]

    if stock is None:
        stock = 0

    # ---------------- TOTAL SALES ----------------
    cur.execute("SELECT SUM(total) FROM sales")
    sales = cur.fetchone()[0]

    if sales is None:
        sales = 0

    # ---------------- TOTAL ORDERS ----------------
    cur.execute("SELECT COUNT(*) FROM sales")
    orders = cur.fetchone()[0]

    # ---------------- TOTAL CUSTOMERS ----------------
    cur.execute("SELECT COUNT(*) FROM customers")
    customers = cur.fetchone()[0]

    print(Fore.YELLOW + "\n📦 INVENTORY STATUS")
    print("-"*40)
    print(f"Total Products : {total_products}")
    print(f"Total Stock    : {stock}")

    print(Fore.YELLOW + "\n💰 SALES STATUS")
    print("-"*40)
    print(f"Total Orders   : {orders}")
    print(f"Total Sales ₹  : {sales}")

    print(Fore.YELLOW + "\n👥 CUSTOMER STATUS")
    print("-"*40)
    print(f"Total Customers: {customers}")

    # ---------------- TOP SELLING PRODUCT ----------------
    cur.execute("""
        SELECT item, SUM(qty)
        FROM sales
        GROUP BY item
        ORDER BY SUM(qty) DESC
        LIMIT 1
    """)

    top = cur.fetchone()

    if top:
        print(Fore.YELLOW + "\n🏆 Top Selling Product")
        print("-"*40)
        print(f"{top[0]} (Sold: {top[1]})")

    # ---------------- LOW STOCK ALERT ----------------
    cur.execute("SELECT name, quantity FROM inventory WHERE quantity < 5")
    low = cur.fetchall()

    if low:
        print(Fore.RED + "\n⚠ LOW STOCK ITEMS")
        print("-"*40)
        for item in low:
            print(f"{item[0]} (Stock: {item[1]})")

    print(Fore.CYAN + "\n" + "="*50)

    conn.close()
