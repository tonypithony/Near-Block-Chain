# Получение изображения и файла, сохраненных в виде BLOB


import sqlite3, os

def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    with open(filename, 'wb') as file:
        file.write(data)
    print("Данный из blob сохранены в: ", filename, "\n")

def read_blob_data_jpg(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python_boobs.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            
            print("Сохранение изображения сотрудника и резюме на диске \n")
            photo_path = os.path.join(name + ".jpg")
            
            write_to_file(photo, photo_path)
            
        cursor.close()
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

read_blob_data_jpg(1)
read_blob_data_jpg(2)

def read_blob_data_png(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python_boobs.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            
            print("Сохранение изображения сотрудника и резюме на диске \n")
            photo_path = os.path.join(name + ".png")
            
            write_to_file(photo, photo_path)
            
        cursor.close()
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            
read_blob_data_png(1)
read_blob_data_png(2)

def read_blob_data_gif(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python_boobs.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            
            print("Сохранение изображения сотрудника и резюме на диске \n")
            photo_path = os.path.join(name + ".gif")
            
            write_to_file(photo, photo_path)
            
        cursor.close()
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            
read_blob_data_gif(3)

def read_blob_data_mp4(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python_boobs.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            
            print("Сохранение изображения сотрудника и резюме на диске \n")
            photo_path = os.path.join(name + ".mp4")
            
            write_to_file(photo, photo_path)
          
        cursor.close()
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            
read_blob_data_mp4(4)