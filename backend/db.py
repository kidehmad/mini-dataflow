import sqlite3

DB_NAME = "jobs.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        status TEXT NOT NULL,
        output TEXT
    )
    """)

    conn.commit()
    conn.close()
def create_job(code):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO jobs (code, status)
        VALUES (?, ?)
        """,
        (code, "PENDING")
    )

    conn.commit()
    conn.close()