from pymongo import MongoClient
from pymongo.server_api import ServerApi

def create_database_and_collection():
    try:
        client = MongoClient(
            "mongodb+srv://kpankieieva:Test1@clustertest.0ttcdib.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest",
            server_api=ServerApi('1'),
            tlsAllowInvalidCertificates=True
        )

        # Перевірка підключення до сервера MongoDB
        client.admin.command('ping')
        print("Підключення до MongoDB успішне!")

        db = client['cats']  # Створюємо базу даних з назвою 'cats'
        collection = db['cats_collection']  # Створюємо колекцію 'cats_collection' у базі даних 'cats'

        # Додаємо перший документ для прикладу
        initial_cat = {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"]
        }
        collection.insert_one(initial_cat)
        print("Створено базу даних 'cats' та колекцію 'cats_collection'")

    except Exception as e:
        print(f"Помилка під час створення бази даних: {e}")

    finally:
        client.close()
        print("З'єднання з MongoDB закрито")

if __name__ == "__main__":
    create_database_and_collection()
