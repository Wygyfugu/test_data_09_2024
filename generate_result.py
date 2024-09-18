import csv
import json


# Функция для чтения данных из CSV файла
def read_books_from_csv(file_path):
    books = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({
                "title": row["title"],
                "author": row["author"],
                "pages": int(row["pages"]),
                "genre": row["genre"]
            })
    return books


# Функция для чтения данных из JSON файла
def read_users_from_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)


# Основная функция для распределения книг между пользователями
def distribute_books(books, users):
    result = []
    num_users = len(users)

    # Распределяем книги между пользователями
    for i, user in enumerate(users):
        user_books = []
        for j in range(i, len(books), num_users):
            if j < len(books):
                user_books.append(books[j])
        user_data = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": user_books
        }
        result.append(user_data)

    return result


# Запись результата в JSON файл
def write_result_to_json(file_path, result):
    with open(file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(result, jsonfile, indent=4)


def main():
    books = read_books_from_csv('books.csv')
    users = read_users_from_json('users.json')
    result = distribute_books(books, users)
    write_result_to_json('result.json', result)


if __name__ == "__main__":
    main()
