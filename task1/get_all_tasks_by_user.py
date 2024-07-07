from connect import create_connection, close_connection

def get_tasks_by_user(user_id):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM tasks WHERE user_id = %s"
        cursor.execute(select_query, (user_id,))
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    user_id = 1  # ID користувача
    get_tasks_by_user(user_id)
