import sqlite3
from loguru import logger
# db = sqlite3.connect("database.db")
# cursor = db.cursor()

with sqlite3.connect("database.db") as db:
    cursor = db.cursor()

def ensure_success(func):
    def wrapper(*args, **kwargs):
        try:
            name = func(*args, **kwargs)
            logger.success(f"{name} has created successfully")
            return True
        except Exception as e:
            if "already exists" in str(e):
                logger.error(f"{name}Table already exists")
            else:
                logger.error(f"An error occurred:{e}")
    return wrapper

@ensure_success
def create_user_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT,
        phone_number INTEGER,
        status BOOLEAN DEFAULT 0, 
        role TEXT
    );
        """)
    return "User"


def initial():
    create_user_table()

if __name__ == '__main__':
    initial()
    db.close()


