import sqlite3

def getSingleRows():
    try:
        #connection = sqlite3.connect('sqlite_python_boobs.db')
        connection = sqlite3.connect('base2.db')
        cursor = connection.cursor()
        print("Connected to database")
        
        # sqlite_select_query = """SELECT * from new_employee"""
        sqlite_select_query = """SELECT * from MutationCornea"""
        cursor.execute(sqlite_select_query)
        
        # print("Fetching single row")
        # record = cursor.fetchone()
        # print(record)
        
        # print("Fetching next row")
        # record = cursor.fetchone()
        # print(record)
        
        print(cursor.fetchmany(size=100))
        
             
        # while(cursor.fetchone()[0] != None):
                       
            # record = cursor.fetchone()
            # print(record)
        
        cursor.close()
        
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The Sqlite connection is closed")
            
getSingleRows()