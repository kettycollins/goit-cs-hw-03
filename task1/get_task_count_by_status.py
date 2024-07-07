from connect import create_connection, close_connection

def get_task_count_by_status():
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = """
        SELECT s.name, COUNT(t.id) 
        FROM tasks t
        JOIN status s ON t.status_id = s.id
        GROUP BY s.name
        """
        cursor.execute(select_query)
        status_counts = cursor.fetchall()
        for status_count in status_counts:
            print(status_count)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    get_task_count_by_status()
