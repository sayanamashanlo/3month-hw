import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_table():
     cursor.execute(
            """
            DROP TABLE IF EXISTS beauty
            """
        )
     cursor.execute(
            """
            DROP TABLE IF EXISTS answers_for_ask
            """
        )
     cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS beauty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT)
            """
        )
     cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS answers_for_ask (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            image TEXT,
            beauty_id INTEGER,
            FOREIGN KEY (beauty_id) REFERENCES beauty (id)
            )
            """
        )
     db.commit()

def added_beauty():
     cursor.execute(
            """
            INSERT INTO beauty (name) VALUES 
            ('чувствительная кожа'),
            ('сухая кожа'),
            ('жирная кожа'),
            ('комбинированная кожа'),
            ('нормальная кожа')
            """
        )
     cursor.execute(
            """
            INSERT INTO answers_for_ask (name, image, beauty_id) VALUES
            ('гидрофильное масло-Beauty of Joseon','beauty_images\\choson-_4_-_1_.png' ,1),
            ('гидрофильное масло-SIORIS', 'beauty_images\\49968387.jpg',2),
            ('гидрофильное масло-Dr.Althea', 'beauty_images\\2-e42d2b73e52cc160f2c2ae3dd8b939ef.jpg',3),
            ('гидрофильное масло-SKIN 1004 centella','beauty_images\\гидрофильное-масло-skin-1004-centella-легчайшее-гидрофильное',4),
            ('гидрофильное масло-SIORIS', 'beauty_images\\49968387.jpg',5 )
            """
        )
     db.commit()


def get_answer():
    cursor.execute(
        """
        SELECT * FROM answers_for_ask
        """
    )
    return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    create_table()
    added_beauty()
    pprint(get_answer())