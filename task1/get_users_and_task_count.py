from connect import create_connection, close_connection

def get_users_task_count():
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = """
        SELECT u.id, u.fullname, COUNT(t.id) 
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.id, u.fullname
        """
        cursor.execute(select_query)
        user_task_counts = cursor.fetchall()
        for user_task_count in user_task_counts:
            print(user_task_count)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    get_users_task_count()
