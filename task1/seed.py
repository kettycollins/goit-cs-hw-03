from faker import Faker
import psycopg2
from psycopg2 import Error
from connect import create_connection, close_connection

def seed_data():
    fake = Faker()
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()

        # Вставка користувачів
        for _ in range(10):
            fullname = fake.name()
            email = fake.unique.email()
            insert_query = f"INSERT INTO users (fullname, email) VALUES (%s, %s)"
            cursor.execute(insert_query, (fullname, email))
        connection.commit()
        print("Дані користувачів вставлено успішно.")

        # Вставка завдань
        status_ids = [1, 2, 3]  # ID статусів ('new', 'in progress', 'completed')
        for _ in range(20):
            title = fake.sentence(nb_words=3)
            description = fake.text()
            status_id = fake.random_element(elements=status_ids)
            user_id = fake.random_int(min=1, max=10)  # 10 користувачів, ID від 1 до 10
            insert_query = f"INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (title, description, status_id, user_id))
        connection.commit()
        print("Дані завдань вставлено успішно.")

    except (Exception, Error) as error:
        print("Помилка під час вставки даних у PostgreSQL", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    seed_data()
