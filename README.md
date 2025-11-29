# Task 6 – Sales Trend Analysis Using Aggregations



## 📘 Objective

Analyze monthly revenue and monthly order volume from the `orders` table using SQL aggregation functions.



## 📂 Dataset

Table: `orders`

Columns:

\- order\_id

\- order\_date

\- amount

\- product\_id



## 🧠 SQL Logic Used

\- `SUM(amount)` → Monthly Revenue

\- `COUNT(DISTINCT order\_id)` → Monthly Order Volume

\- `strftime('%Y', order\_date)` → Extract year

\- `strftime('%m', order\_date)` → Extract month

\- `GROUP BY year, month` → Required by task

\- `ORDER BY year, month` → Sort chronologically



## 📝 Final SQL Query (SQLite)

```sql

SELECT

&nbsp;   strftime('%Y', order\_date) AS year,

&nbsp;   strftime('%m', order\_date) AS month,

&nbsp;   SUM(amount) AS monthly\_revenue,

&nbsp;   COUNT(DISTINCT order\_id) AS monthly\_order\_volume

FROM orders

GROUP BY year, month

ORDER BY year, month;


