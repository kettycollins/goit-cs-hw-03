from connect import create_connection, close_connection

def get_tasks_by_status(status_name):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = """
        SELECT t.* FROM tasks t
        JOIN status s ON t.status_id = s.id
        WHERE s.name = %s
        """
        cursor.execute(select_query, (status_name,))
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    status_name = 'new'  # потрібний статус
    get_tasks_by_status(status_name)
