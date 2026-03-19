import sqlite3
import pandas as pd
from colorama import Fore

def export_sales_excel():

    try:

        conn = sqlite3.connect("inventory.db")

        query = "SELECT * FROM sales"
        df = pd.read_sql_query(query, conn)

        if df.empty:
            print("❌ No sales data available")
            conn.close()
            return

        # always update same file
        filename = "Sales_Report.xlsx"

        df.to_excel(filename, index=False)

        conn.close()

        print(Fore.GREEN + "✅ Excel Report Updated Successfully")
        print(Fore.YELLOW + "📄 File: Sales_Report.xlsx")

    except Exception as e:
        print(Fore.RED + f"❌ Error exporting report: {e}")
