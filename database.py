import sqlite3
from datetime import datetime

DB_NAME = "chat_logs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_chat(user_message, bot_response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_logs (user_message, bot_response, timestamp)
    VALUES (?, ?, ?)
    """, (user_message, bot_response, datetime.now().isoformat()))

    conn.commit()
    conn.close()