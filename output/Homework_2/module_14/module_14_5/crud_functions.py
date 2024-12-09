import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INT NOT NULL
        )   
        ''')
    # for i in range(1, 5):
    #     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    #                    (f"{i}", f"Продукт {i}", f"Описание {i}", str(i * 100)))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
        ''')
    cursor.execute("DELETE FROM Users WHERE id = 0")
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products



def add_user(username, email, age):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    balance = 1000
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))

    if check_user.fetchone() is None:
        cursor.execute(F'''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
        ''', (username, email, age, balance))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))

    if check_user.fetchone() is None:
        return True
    else:
        connection.close()
        return False


# initiate_db()
