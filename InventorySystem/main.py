from colorama import Fore, Style, init
import time

from database import create_tables, add_default_users
from login import login

from inventory import add_item, view_items, restock_item, low_stock
from billing import billing
from dashboard import show_dashboard
from graph import sales_graph
from file_handler import export_sales_excel
from customer import add_customer, view_customers

init(autoreset=True)


# ---------------- UI FUNCTIONS ---------------- #

def clear():
    print("\n" * 40)


def pause():
    input(Fore.YELLOW + "\nPress Enter to continue...")


def loading():
    print(Fore.YELLOW + "\nLoading System", end="")
    for i in range(5):
        time.sleep(0.3)
        print(".", end="")
    print("\n")


def header():
    print(Fore.CYAN + "======================================================")
    print(Fore.GREEN + "        📦 INVENTORY MANAGEMENT SYSTEM")
    print(Fore.CYAN + "======================================================")
    print(Fore.YELLOW + "     Stock | Billing | Dashboard | Reports")
    print(Fore.CYAN + "======================================================")


def main_menu():
    print(Fore.MAGENTA + """
🟢 MAIN MENU

1  Inventory Management
2  Billing System
3  Customer Management
4  Live Dashboard
5  Sales Graph
6  Export Reports
0  Exit
""")


def inventory_menu():
    print(Fore.BLUE + """
📦 INVENTORY MENU

1 Add Item
2 View Inventory
3 Restock Item
4 Low Stock Report
0 Back
""")


def customer_menu():
    print(Fore.GREEN + """
👥 CUSTOMER MENU

1 Add Customer
2 View Customers
0 Back
""")


# ---------------- MAIN PROGRAM ---------------- #

def main():

    loading()

    # Create DB tables
    create_tables()
    add_default_users()

    # Login
    user = login()

    if not user:
        print(Fore.RED + "Login Failed")
        return

    role = user[3]

    while True:

        clear()
        header()
        main_menu()

        choice = input(Fore.YELLOW + "Enter your choice: ")

        # ---------- INVENTORY ----------

        if choice == "1":

            if role not in ["admin", "staff"]:
                print(Fore.RED + "Access Denied! Only Admin and Staff allowed.")
                pause()
                continue

            while True:

                clear()
                header()
                inventory_menu()

                ch = input("Enter choice: ")

                if ch == "1":

                    if role != "admin":
                        print(Fore.RED + "Only Admin can add items")
                    else:
                        add_item()

                elif ch == "2":
                    view_items()

                elif ch == "3":

                    if role != "admin":
                        print(Fore.RED + "Only Admin can restock items")
                    else:
                        restock_item()

                elif ch == "4":
                    low_stock()

                elif ch == "0":
                    break

                else:
                    print(Fore.RED + "Invalid Choice")

                pause()

        # ---------- BILLING ----------

        elif choice == "2":

            if role in ["admin", "staff", "customer"]:
                billing()
            else:
                print(Fore.RED + "Access Denied")

            pause()

        # ---------- CUSTOMER ----------

        elif choice == "3":

            if role not in ["admin", "staff"]:
                print(Fore.RED + "Access Denied! Only Admin and Staff allowed.")
                pause()
                continue

            while True:

                clear()
                header()
                customer_menu()

                ch = input("Enter choice: ")

                if ch == "1":
                    add_customer()

                elif ch == "2":
                    view_customers()

                elif ch == "0":
                    break

                else:
                    print(Fore.RED + "Invalid Choice")

                pause()

        # ---------- DASHBOARD ----------

        elif choice == "4":

            if role != "admin":
                print(Fore.RED + "Only Admin can view Dashboard")
            else:
                show_dashboard()

            pause()

        # ---------- GRAPH ----------

        elif choice == "5":

            if role != "admin":
                print(Fore.RED + "Only Admin can view Sales Graph")
            else:
                sales_graph()

            pause()

        # ---------- EXPORT ----------

        elif choice == "6":

            if role != "admin":
                print(Fore.RED + "Only Admin can export reports")
            else:
                export_sales_excel()

            pause()

        # ---------- EXIT ----------

        elif choice == "0":

            print(Fore.GREEN + "\nThank you for using Inventory System 🚀")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "Invalid Choice")
            pause()


# Run Program
if __name__ == "__main__":
    main()
