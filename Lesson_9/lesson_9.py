import json

database = {}  # База данных пользователей


def save_users():
    with open('db.json', 'w') as file:
        json.dump(database, file)


def load_database():
    global database
    try:
        with open('db.json', 'r') as file:
            database = json.load(file)
    except FileNotFoundError:
        pass


def register_user():
    username = input("Введите ваш ник: ")
    if username in database:
        print("Пользователь уже существует! ")
        return
    password = input("Введите ваш пароль ")
    age = int(input("Введите ваш возраст "))
    database[username] = {'password': password, 'age': age}
    save_users()
    print("Регистрация прошла успешно")


def login():
    username = input("Введите ваш ник: ")
    password = input("Введите ваш пароль: ")
    if database[username]['password'] == password:
        print(f"Добро пожаловать, {username}!")
        return username
    else:
        print("Неверный логин или пароль")


def change_age(username):
    new_age = input("Введите возраст: ")
    database[username]['age'] = new_age
    save_users()
    print("Возраст успешно изменен")


load_database()

authenticated_user = None

while True:
    if authenticated_user:
        print("1. Изменить возраст")
        print("2. Разлогиниться")
        choice = input("Выберите действие ")

        if choice == '1':
            change_age(authenticated_user)
        elif choice == '2':
            authenticated_user = None
            print("Успешно разлогинился! ")
    else:
        print("1. Зарегистрироваться")
        print("2. Войти")
        print("3. Выход из программы")
        choice = input("Выберите действие ")

        if choice == '1':
            register_user()
        elif choice == '2':
            authenticated_user = login()
        elif choice == '3':
            break
