import sqlite3

conn = sqlite3.connect('online_sales.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER,
    order_date TEXT,
    amount REAL,
    product_id INTEGER
)
''')

conn.commit()
conn.close()

print("Database and orders table created successfully.")