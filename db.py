import sqlite3

def get_db_connection():
    conn = sqlite3.connect('sports_manager.db')
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    conn = get_db_connection()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sport_type TEXT NOT NULL,
                location TEXT NOT NULL
            )
        """)
    conn.close()

setup_database()
