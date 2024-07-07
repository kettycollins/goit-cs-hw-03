from connect import create_connection, close_connection

def get_tasks_by_user_email_domain(email_domain):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = """
        SELECT t.* FROM tasks t
        JOIN users u ON t.user_id = u.id
        WHERE u.email LIKE %s
        """
        cursor.execute(select_query, (email_domain,))
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    email_domain = '%@example.com'  # потрібний email domain
    get_tasks_by_user_email_domain(email_domain)
