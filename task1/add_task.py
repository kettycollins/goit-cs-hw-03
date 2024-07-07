from connect import create_connection, close_connection

def add_task(title, description, status_name, user_id):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        # статус ID за назвою
        status_query = "SELECT id FROM status WHERE name = %s"
        cursor.execute(status_query, (status_name,))
        status_id = cursor.fetchone()[0]

        insert_query = """
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (%s, %s, %s, %s) RETURNING id
        """
        cursor.execute(insert_query, (title, description, status_id, user_id))
        task_id = cursor.fetchone()[0]
        connection.commit()
        print("Нове завдання додано успішно. ID нового завдання:", task_id)

        # отримати та вивести нове завдання
        select_query = "SELECT * FROM tasks WHERE id = %s"
        cursor.execute(select_query, (task_id,))
        new_task = cursor.fetchone()
        print("Додане завдання:", new_task)

    except Exception as error:
        print("Помилка під час додавання завдання", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    title = 'New Task Title'  # потрібна назва завдання
    description = 'New Task Description'  # потрібний опис
    status_name = 'new'  # зпотрібний статус
    user_id = 1  # потрібний user_id
    add_task(title, description, status_name, user_id)
