import sqlite3

conn = sqlite3.connect("reviews.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    review_text TEXT,
    sentiment_score INTEGER,
    sentiment_label TEXT
)
""")

conn.commit()
