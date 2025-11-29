import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('online_sales.db')

# Read SQL query from file
with open('sql/sales_trend.sql', 'r') as f:
    query = f.read()

# Run query and load result into DataFrame
df = pd.read_sql_query(query, conn)

# Save results into CSV file
df.to_csv('results/monthly_sales.csv', index=False)

# Show result in terminal
print(df)

conn.close()
print("\nResults saved to results/monthly_sales.csv")