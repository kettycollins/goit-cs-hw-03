from connect import create_connection, close_connection

def get_tasks_without_description():
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM tasks WHERE description IS NULL OR description = ''"
        cursor.execute(select_query)
        tasks = cursor.fetchall()
        
        if not tasks:
            print("Завдань без опису не знайдено.")
        else:
            for task in tasks:
                print(task)
    except Exception as error:
        print("Помилка під час виконання запиту", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    get_tasks_without_description()
