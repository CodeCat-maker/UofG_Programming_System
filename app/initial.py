import sqlite3
from loguru import logger
db = sqlite3.connect("database.db")
cursor = db.cursor()



def ensure_success(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            logger.success("users table has created successfully")
            return True
        except Exception as e:
            if "already exists" in str(e):
                logger.error("Table already exists")
            else:
                logger.error("An error occurred:", e)
    return wrapper

@ensure_success
def create_user_table():
    cursor.execute("""
        CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT,
        phone_number INTEGER,
        status BOOLEAN DEFAULT 0, 
        role TEXT
    );
        """)


def initial():
    create_user_table()

if __name__ == '__main__':
    initial()


