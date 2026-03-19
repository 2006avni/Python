import sqlite3
from datetime import datetime
from pdf_invoice import generate_invoice

def billing():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    customer_name = input("Customer Name: ")

    bill_items = []
    total_amount = 0

    while True:

        item_name = input("Item Name (0 to stop): ")

        if item_name == "0":
            break

        cursor.execute(
            "SELECT price, quantity FROM inventory WHERE name=?",
            (item_name,)
        )

        item = cursor.fetchone()

        if item is None:
            print("❌ Item not found")
            continue

        price = item[0]
        stock = item[1]

        qty = int(input("Quantity: "))

        if qty > stock:
            print("❌ Not enough stock available")
            continue

        cost = price * qty
        total_amount += cost

        # update stock
        new_stock = stock - qty
        cursor.execute(
            "UPDATE inventory SET quantity=? WHERE name=?",
            (new_stock, item_name)
        )

        # save sale to database
        cursor.execute(
            "INSERT INTO sales (customer,item,qty,total,date) VALUES (?,?,?,?,?)",
            (customer_name, item_name, qty, cost, datetime.now())
        )

        bill_items.append({
            "name": item_name,
            "qty": qty,
            "price": cost
        })

        print(f"✅ Added {item_name} x {qty}")

    conn.commit()   # VERY IMPORTANT
    conn.close()

    if len(bill_items) == 0:
        print("No items billed")
        return

    print("\n------- BILL SUMMARY -------")

    for item in bill_items:
        print(item["name"], "x", item["qty"], "= ₹", item["price"])

    print("Total Amount: ₹", total_amount)

    # generate invoice
    generate_invoice(customer_name, bill_items, total_amount)
