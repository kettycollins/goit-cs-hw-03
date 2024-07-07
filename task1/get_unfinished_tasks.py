from connect import create_connection, close_connection

def get_uncompleted_tasks():
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = """
        SELECT t.* FROM tasks t
        JOIN status s ON t.status_id = s.id
        WHERE s.name != 'completed'
        """
        cursor.execute(select_query)
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    get_uncompleted_tasks()
