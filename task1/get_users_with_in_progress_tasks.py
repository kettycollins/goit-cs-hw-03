from connect import create_connection, close_connection

def get_users_with_in_progress_tasks():
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = """
        SELECT u.id, u.fullname, t.id, t.title, t.description
        FROM users u
        JOIN tasks t ON u.id = t.user_id
        JOIN status s ON t.status_id = s.id
        WHERE s.name = 'in progress'
        """
        cursor.execute(select_query)
        results = cursor.fetchall()
        for result in results:
            print(result)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    get_users_with_in_progress_tasks()
