import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


    """таблица для данных пользователя при подписке"""
def create_tables():
     cursor.execute(
        """
        DROP TABLE IF EXISTS user
        """
     )
     cursor.execute(
        """
        CREATE TABlE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id INTEGER, 
        user_name TEXT )
        """
     )
     # таблица для магазина
     cursor.execute(
            """
            DROP TABLE IF EXISTS category
            """
        )
     cursor.execute(
            """
            DROP TABLE IF EXISTS products
            """
        )

     cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT)
            """
        )
     # таблица для опросника
     cursor.execute(
         """
       CREATE TABLE IF NOT EXISTS Questionaire (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            country TEXT,
            book TEXT,
            film TEXT,
            serial TEXT
        )  
         """
     )
     cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DEMICAL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category (id)
            )
            """
        )
     db.commit()


def subscribe_user(user_id: int, user_name: str):
    cursor.execute(
        """
        INSERT INTO user  (user_id, user_name) VALUES (?,?) 
        """,  (user_id, user_name)
    )
def populate_tables():
     cursor.execute(
            """
            INSERT INTO category (name) VALUES 
            ('крем'),
            ('тонер'),
            ('сыворотка')
            """
        )
     cursor.execute(
            """
            INSERT INTO products (name, price ,category_id) VALUES
            ('ELLO', 1400, 1),
            ('Dr. Althea', 1799, 2),
            ('SKIN 1004 CENTELLA', 1350, 1),
            ('Beauty of Jesoun', 1200, 2),
            ('Pyunkang Yul', 1990, 3),
            ('ROUND LAB с березовым соком', 799, 3)
            """
        )
     db.commit()


def get_user_id():
    cursor.execute(
        """
        SELECT * FROM user
        """
    )
    return cursor.fetchall()


def get_product_by_category_id(category_id: int):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = :cat_id
        """, {"cat_id": category_id}
    )
    return cursor.fetchall()


def get_product_by_category_name(cat_name: str):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = 
        (
            SELECT id FROM category WHERE name = :cat_name
        )
        """, {"cat_name": cat_name}
    )
    return cursor.fetchall()


def get_products_with_category():
    cursor.execute(
        """
        SELECT p.name, c.name FROM products AS p JOIN category AS c ON p.category_id = c.id
        """
    )
    return cursor.fetchall()


def save_questionaire(data):
    print(data)
    cursor.execute(
        """
        INSERT INTO Questionaire (name, age, country, book, film, serial) VALUES
        (:name, :age, :country, :book, :film, :serial)
        """, data
    )
    db.commit()


def get_products():
    cursor.execute(
        """
        SELECT * FROM products
        """
    )
    return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_products())