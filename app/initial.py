import sqlite3
from loguru import logger
# db = sqlite3.connect("database.db")
# cursor = db.cursor()

with sqlite3.connect("database.db") as db:
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


def create_vehicle_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vehicle(
        vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        type INTEGER NOT NULL,
        longitude INTEGER NOT NULL,
        latitude INTEGER NOT NULL,
        status TEXT NOT NULL,
        battery FLOAT NOT NULL
        );
        """)
    db.commit()

def create_order_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders(
        order_id TEXT PRIMARY KEY ,
        userid TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL,
        price FLOAT NOT NULL,
        time TIMESTAMP NOT NULL,
        status BOOLEAN NOT NULL,
        destination TEXT NOT NULL
        );
    """)
    db.commit()

def create_report_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Report(
        report_id TEXT PRIMARY KEY ,
        type INTEGER NOT NULL,
        time TIMESTAMP NOT NULL,
        status BOOLEAN NOT NULL
        );
    """)
    db.commit()


def initial():
    create_user_table()
    create_vehicle_table()
    create_order_table()
    create_report_table()


if __name__ == '__main__':
    initial()
    db.close()


