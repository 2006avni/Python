import sqlite3


# DATABASE CONNECTION
def get_connection():
    return sqlite3.connect("inventory.db")


# CREATE TABLES
def create_tables():

    conn = get_connection()
    cur = conn.cursor()

    # USERS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # INVENTORY TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS inventory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    # SALES TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT NOT NULL,
        item TEXT NOT NULL,
        qty INTEGER NOT NULL,
        total REAL NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # CUSTOMERS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()


# ADD DEFAULT USERS
def add_default_users():

    conn = get_connection()
    cur = conn.cursor()

    users = [
        ("admin", "admin123", "admin"),
        ("staff", "staff123", "staff"),
        ("customer", "cust123", "customer")
    ]

    for user in users:
        try:
            cur.execute(
                "INSERT INTO users(username,password,role) VALUES(?,?,?)",
                user
            )
        except sqlite3.IntegrityError:
            # User already exists
            pass

    conn.commit()
    conn.close()
