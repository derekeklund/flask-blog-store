import sqlite3

# Connect to database
conn = sqlite3.connect('products.db')

with open('queries.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO averageReviews (productID, productName, avgReview) VALUES (?, ?, ?)",
            (3, 'Lehman_Mug', 0.0)
            )

conn.commit()
conn.close()