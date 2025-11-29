import sqlite3

conn = sqlite3.connect('online_sales.db')
cur = conn.cursor()

cur.execute("DELETE FROM orders")  # clear table before inserting

data = [
    (1, '2023-01-05', 120.00, 2),
    (2, '2023-01-11', 90.00, 3),
    (3, '2023-02-09', 150.00, 2),
    (4, '2023-02-21', 80.00, 1),
    (5, '2023-03-15', 200.00, 4),
    (6, '2023-03-18', 300.00, 1)
]

cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", data)

conn.commit()
conn.close()

print("Sample data inserted successfully.")