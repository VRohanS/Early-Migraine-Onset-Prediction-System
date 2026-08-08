import sqlite3
from datetime import datetime

conn = sqlite3.connect("migraine.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    photophobia INTEGER,
    phonophobia INTEGER,
    typing REAL,
    result TEXT,
    time TEXT
)
""")
conn.commit()

def insert_record(p, ph, t, r):
    cursor.execute(
        "INSERT INTO records (photophobia, phonophobia, typing, result, time) VALUES (?,?,?,?,?)",
        (p, ph, t, r, datetime.now())
    )
    conn.commit()

def get_records():
    cursor.execute("SELECT * FROM records ORDER BY id DESC")
    return cursor.fetchall()