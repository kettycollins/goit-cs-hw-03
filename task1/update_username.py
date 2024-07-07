from connect import create_connection, close_connection

def update_user_name(user_id, new_fullname):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        
        # отримати старе ім'я користувача
        select_query = "SELECT fullname FROM users WHERE id = %s"
        cursor.execute(select_query, (user_id,))
        old_fullname = cursor.fetchone()[0]

        # оновити ім'я користувача
        update_query = "UPDATE users SET fullname = %s WHERE id = %s"
        cursor.execute(update_query, (new_fullname, user_id))
        connection.commit()
        
        print(f"Ім'я користувача оновлено успішно. Старе ім'я: {old_fullname}, Нове ім'я: {new_fullname}")
    except Exception as error:
        print("Помилка під час оновлення імені користувача", error)
    finally:
        close_connection(connection)

if __name__ == "__main__":
    user_id = 1  # потрібний user_id
    new_fullname = 'New Full Name'  # потрібне ім'я
    update_user_name(user_id, new_fullname)
