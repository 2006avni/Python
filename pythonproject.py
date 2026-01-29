# Inventory Stock Analysis System using Arrays

# Arrays (Lists)
item_names = ["Pen", "Notebook", "Pencil", "Eraser", "Marker"]
stock = [100, 80, 150, 60, 40]
price = [10, 50, 5, 3, 25]
reorder_level = [20, 15, 30, 10, 10]
sales = [0, 0, 0, 0, 0]

def display_items():
    print("\nItem List")
    print("------------------------------------------------")
    print("ID\tItem\t\tStock\tPrice")
    for i in range(len(item_names)):
        print(i, "\t", item_names[i], "\t\t", stock[i], "\t", price[i])
    print("------------------------------------------------")

def sell_item():
    display_items()
    item_id = int(input("Enter Item ID to sell: "))
    qty = int(input("Enter Quantity: "))

    if qty <= stock[item_id]:
        stock[item_id] -= qty
        sales[item_id] += qty
        print("Sale Successful!")
    else:
        print("Not enough stock!")

def restock_alert():
    print("\nRestocking Alerts")
    print("----------------------------")
    for i in range(len(stock)):
        if stock[i] <= reorder_level[i]:
            print(item_names[i], "needs restocking (Stock:", stock[i], ")")

def item_summary():
    print("\nItem-wise Summary")
    print("------------------------------------------------------")
    print("Item\t\tStock\tSold\tRevenue")
    total_revenue = 0
    for i in range(len(item_names)):
        revenue = sales[i] * price[i]
        total_revenue += revenue
        print(item_names[i], "\t\t", stock[i], "\t", sales[i], "\t", revenue)
    print("------------------------------------------------------")
    print("Total Revenue = Rs.", total_revenue)

while True:
    print("\n📦 Inventory Stock Analysis System")
    print("1. Display Items")
    print("2. Sell Item")
    print("3. Restocking Alerts")
    print("4. Item-wise Summary")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_items()
    elif choice == 2:
        sell_item()
    elif choice == 3:
        restock_alert()
    elif choice == 4:
        item_summary()
    elif choice == 5:
        print("Thank you for using Inventory System")
        break
    else:
        print("Invalid choice")
