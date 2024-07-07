from connect import create_connection, close_connection

def update_task_status(task_id, new_status_name):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        status_query = "SELECT id FROM status WHERE name = %s"
        cursor.execute(status_query, (new_status_name,))
        status_id = cursor.fetchone()[0]

        update_query = "UPDATE tasks SET status_id = %s WHERE id = %s"
        cursor.execute(update_query, (status_id, task_id))
        connection.commit()
        print("Статус завдання оновлено успішно")
    except Exception as error:
        print("Помилка під час оновлення статусу завдання", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    task_id = 1  # потрібний task_id
    new_status_name = 'in progress'  # потрібний статус
    update_task_status(task_id, new_status_name)
