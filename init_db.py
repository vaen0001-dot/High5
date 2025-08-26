# init_db.py
import sqlite3

with open("schema.sql", "r", encoding="utf-8") as f:
    schema = f.read()

conn = sqlite3.connect("database.db")
conn.executescript(schema)
conn.commit()
conn.close()
print("database.db created with users and messages tables.")
