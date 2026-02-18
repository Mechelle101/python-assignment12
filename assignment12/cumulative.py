
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 2: Line PLot with Pandas
SQL = """
  SELECT
  o.order_id,
  SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

with sqlite3.connect("../db/lesson.db") as conn:
  df = pd.read_sql_query(SQL, conn)
  
df["cumulative"] = df["total_price"].cumsum()

ax = df.plot(
  kind="line",
  x="order_id",
  y="cumulative",
  title="Cumulative Revenue by Order"
)

ax.set_xlabel("Order ID")
ax.set_ylabel("Cumulative Revenue ($)")
plt.tight_layout()
plt.show()
