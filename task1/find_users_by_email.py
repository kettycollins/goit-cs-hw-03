from connect import create_connection, close_connection

def find_users_by_email(email_pattern):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM users WHERE email LIKE %s"
        cursor.execute(select_query, (email_pattern,))
        users = cursor.fetchall()
        for user in users:
            print(user)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    email_pattern = '%@example.com'  # замініть на потрібний email domain
    find_users_by_email(email_pattern)
