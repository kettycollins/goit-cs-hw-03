from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

def connect_to_mongodb():
    client = MongoClient(
        "mongodb+srv://kpankieieva:Test1@clustertest.0ttcdib.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest",
        server_api=ServerApi('1'),
        tlsAllowInvalidCertificates=True
    )
    return client

def close_connection(client):
    client.close()
    print("З'єднання з MongoDB закрито")

def read_all_cats(collection):
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(collection, name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений")

def update_cat_age(collection, name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Вік кота '{name}' оновлено")
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений")

def add_feature_to_cat(collection, name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count > 0:
        print(f"Додано нову характеристику '{new_feature}' коту '{name}'")
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений")

def delete_cat_by_name(collection, name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям '{name}' видалено")
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений")

def delete_all_cats(collection):
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} котів")

def main_menu():
    print("\nОберіть операцію:")
    print("1. Вивести усіх котів")
    print("2. Пошук кота за ім'ям")
    print("3. Оновити вік кота за ім'ям")
    print("4. Додати нову характеристику коту за ім'ям")
    print("5. Видалити кота за ім'ям")
    print("6. Вийти з програми")
    choice = input("Ваш вибір: ")
    return choice

if __name__ == "__main__":
    client = connect_to_mongodb()
    db = client['cats']
    collection = db['cats_collection']

    while True:
        choice = main_menu()

        if choice == '1':
            read_all_cats(collection)
        elif choice == '2':
            cat_name = input("\nВведіть ім'я кота для пошуку: ")
            read_cat_by_name(collection, cat_name)
        elif choice == '3':
            cat_name_to_update = input("\nВведіть ім'я кота для оновлення віку: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(collection, cat_name_to_update, new_age)
        elif choice == '4':
            cat_name_to_update_features = input("\nВведіть ім'я кота для додавання нової характеристики: ")
            new_feature = input("Введіть нову характеристику: ")
            add_feature_to_cat(collection, cat_name_to_update_features, new_feature)
        elif choice == '5':
            cat_name_to_delete = input("\nВведіть ім'я кота для видалення: ")
            delete_cat_by_name(collection, cat_name_to_delete)
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    close_connection(client)