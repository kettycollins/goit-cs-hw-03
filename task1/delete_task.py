from connect import create_connection, close_connection

def delete_task(task_id):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(delete_query, (task_id,))
        connection.commit()
        print("Завдання видалено успішно")
    except Exception as error:
        print("Помилка під час видалення завдання", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    task_id = 1  # потрібний task_id
    delete_task(task_id)
