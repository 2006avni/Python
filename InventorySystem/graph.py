import matplotlib.pyplot as plt
from database import get_connection

def sales_graph():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT item,SUM(qty) FROM sales GROUP BY item")

    data = cur.fetchall()

    items = [x[0] for x in data]
    qty = [x[1] for x in data]

    plt.bar(items,qty)

    plt.title("Sales Graph")
    plt.xlabel("Items")
    plt.ylabel("Quantity Sold")

    plt.show()

    conn.close()
