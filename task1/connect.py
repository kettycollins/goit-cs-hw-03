import psycopg2
from psycopg2 import Error

def create_connection():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Test123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        print("Підключення до бази даних PostgreSQL успішне")
        return connection
    except (Exception, Error) as error:
        print("Помилка під час підключення до PostgreSQL", error)
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("З'єднання з PostgreSQL закрито")

if __name__ == "__main__":
    conn = create_connection()
    close_connection(conn)
