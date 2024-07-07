import psycopg2
from psycopg2 import Error
import os

def create_db():
    sql_file = os.path.abspath('/Users/katya/Desktop/Master/comp_fund/hw_3/venv/database.sql')

    with open(sql_file, 'r') as f:
        sql = f.read()

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Test123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres") 

        cursor = connection.cursor()

        cursor.execute(sql)
        connection.commit()
        print("Базу даних PostgreSQL створено успішно!")

    except (Exception, Error) as error:
        print("Помилка під час створення бази даних PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("З'єднання з PostgreSQL закрито")

if __name__ == "__main__":
    create_db()
