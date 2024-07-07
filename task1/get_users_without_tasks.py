from connect import create_connection, close_connection

def get_users_without_tasks():
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = """
        SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)
        """
        cursor.execute(select_query)
        users = cursor.fetchall()
        for user in users:
            print(user)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    get_users_without_tasks()
