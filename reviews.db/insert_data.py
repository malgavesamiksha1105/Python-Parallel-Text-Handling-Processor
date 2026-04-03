import csv

with open("amazon.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
        INSERT INTO reviews (id, review_text, sentiment_score, sentiment_label)
        VALUES (?, ?, ?, ?)
        """, (row['review_id'], row['review_text'], row['sentiment_score'], row['sentiment_label']))

conn.commit()
conn.close()
