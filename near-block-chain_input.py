# Вставка изображений и файлов в таблицу
import sqlite3

def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_blob(emp_id, name, photo):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python_boobs.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS new_employee
              (id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL)''')

        sqlite_insert_blob_query = """INSERT INTO new_employee
                                  (id, name, photo) VALUES (?, ?, ?)"""

        emp_photo = convert_to_binary_data(photo)
        
        # Преобразование данных в формат кортежа
        data_tuple = (emp_id, name, emp_photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение успешно вставленo как BLOB в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

insert_blob(1, "test1", "1.png")
insert_blob(2, "test2", "1.jpg")
insert_blob(3, "test3", "1.gif")
insert_blob(4, "test4", "1.mp4")
